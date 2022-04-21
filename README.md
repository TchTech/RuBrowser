# Electron-Ru-Browser
<div id="header" align="center">
<img src="https://media.discordapp.net/attachments/830393925633572894/965901390528540703/rusearch1.png?width=603&height=603"  alt="rusearch-icon" />
</div>
<div id="header" style="align: center;">
<h1>RuSearch: Russian, Modern, Modular and Multipurpose Tool.</h1>
</div>
<h3 align="center">Ru Search Engine for Domains</h3>
<hr />
<h3 align="center">Made with Electron.js and Python.</h3>
<hr />
<h4 align ="center">Introduction!</h4>

<p>
  This is my first hackathon project. Frontend made with Electron.js. Sitemapper and RuSearcher made with Python. RuSearcher use RuBert Tiny (for semantic search) and Custom search algorithm. RuSearch made modulary for easy adding new algorithms to searching system.</p>
<hr />
<h4 align="center">Prerequisites Tools!</h4>
<ul>
  <li>Desktop app: to use this, you need to install Node.js and Electron.js.
  </li>
  <li>Sitemapper: to use this, you need to install Python(with asyncio, urlib, aiohttp and re).
  </li>
  <li>RuSearcher: to use this, you need to install Python libraries: sklearn, transformers, numpy and torch.
  </li>
</ul>
<h4>Setup Instructions!</h4>

<p>Clone the repository:</p>

```console

    $ git clone https://github.com/Dhyeythumar/Search-Engine.git
    
    $ cd Search_Engine
```
<p>Install and Update Node JS Dependency:</p>

```console

$ npm install

$ npm update

```

<p>Install Python Dependency:</p>

```console

$ cd Python_scripts

$ pip install -r requirements.txt

```

<h4>Getting Started!</h4>
<p>
Run this project by just executing this command:
</p>

```console

$ npm start

```

<p>
Now write query and url to input fields in app. 
  if you want to add:
  
  ```
  
  @+: url
  
  ``` 
  
  Or remove:
  
  ```
  
  @-: url
  
  ``` 
  
  Some urls from search, just change robots.txt!
</p>
<hr />
<hr />
<h4 align="center">Future development!</h4>
<p>This tool could be used as PWA, if you need. I will try to continue develop this RuBrowser and make it better.</p>
