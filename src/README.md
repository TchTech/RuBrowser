# Electron-Ru-Browser 
<div id="header" align="center">
<img src="https://media.discordapp.net/attachments/830393925633572894/965901390528540703/rusearch1.png?width=603&height=603"  alt="rusearch-icon" />
</div>
<h1 id="header" align="center"> Dependencies:</h1>
  <br />
  For Node.js: Electron.js.<br /><br />
  For Python: Asyncio, Urlib, BeautifulSoup4, Re, Transformers, Torch, SkLearn, Autocorrect<br /><br />
<h1 id="header" align="center"> Installation:</h1>
  <br />
  1. Install Dependencies.<br />
  2. Make dir "rusbert_large" in "src".<br />
  3. cd rusbert_large.<br />
  4. Run:<br />

```

$ python

$ from transformers import AutoTokenizer, AutoModel

$ model = AutoModel.from_pretrained("sberbank-ai/sbert_large_nlu_ru")

$ model.save_pretrained("rusbert_large") 

```
  5. Use App!<br />
<br />
<h1 id="header" align="center"> Doc:</h1><br />
<p>browser.js renders ui and run all other scripts.<br />
correction folder used to correct users query.<br />
sitemapper.py generates sitemap using rucrawler.py and writes urls to urls.txt<br />
ranker.py makes ranks using ruranker.py (where you can add module functions) and bertscore.py</p>
