import asyncio
import re
import urllib.parse
import aiohttp
import signal
class Crawler:

    exclude_urls = []

    def __init__(self, rooturl, maxtasks=100,
                 todo_queue_backend=set, done_backend=dict):
        self.rooturl = rooturl
        self.todo_queue = todo_queue_backend()
        self.busy = set()
        self.done = done_backend()
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks)
        self.session = aiohttp.ClientSession()

    async def run(self):
        t = asyncio.ensure_future(self.addurls([(self.rooturl, '')]))
        await asyncio.sleep(1)
        while self.busy:
            await asyncio.sleep(1)

        await t
        await self.session.close()

    async def addurls(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if (url.startswith(self.rooturl) and
                    not any(exclude_part in url for exclude_part in self.exclude_urls) and
                    url not in self.busy and
                    url not in self.done and
                    url not in self.todo_queue):
                self.todo_queue.add(url)

                await self.sem.acquire()

                task = asyncio.ensure_future(self.process(url))

                task.add_done_callback(lambda t: self.sem.release())

                task.add_done_callback(self.tasks.remove)

                self.tasks.add(task)

    async def process(self, url):
        print(url)
        self.todo_queue.remove(url)
        self.busy.add(url)

        try:
            resp = await self.session.get(url)
        except Exception as exc:
            print('...', url, 'has error', repr(str(exc)))
            self.done[url] = False
        else:
            if (resp.status == 200 and
                    ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
                asyncio.Task(self.addurls([(u, url) for u in urls]))
            resp.close()
            self.done[url] = True
             

        self.busy.remove(url)
        print(url)

    def set_exclude_url(self, urls_list):
        self.exclude_urls = urls_list


def crawler(maxtasks=100, exclude_urls=None, include_urls=[]):
    for root_url in include_urls:
        loop = asyncio.get_event_loop()
        c = Crawler(root_url, maxtasks=maxtasks)
        if exclude_urls:
            c.set_exclude_url(urls_list=exclude_urls)
        loop.run_until_complete(c.run())
        try:
            loop.add_signal_handler(signal.SIGINT, loop.stop)
        except RuntimeError:
            pass
