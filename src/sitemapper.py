import sys
from rucrawler import crawler

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    root_url = input()
    exclude_urls = [".pdf", ".jpg", ".zip", ".png", ".css", ".xml"]
    include_urls = []
    with open('robots.txt') as robots:
            robots = robots.read().split("\n")
            for line in robots:
                if(line.startswith("@")):
                    symbol = line.split(" ")[0]
                    if(symbol=='@-:'):
                        exclude_urls.append(line.split(" ")[1])
                    elif(symbol=='@+:'):
                        include_urls.append(line.split(" ")[1])
    print(include_urls)
    include_urls.append(root_url)
    crawler(exclude_urls=exclude_urls, include_urls=include_urls)