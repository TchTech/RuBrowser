const fs = require('fs')

var processing = false

onload = function() {

  document.querySelector('#find').onclick = function(e) {
    e.preventDefault();
    if(!processing){
      SitemapAndSearch(document.querySelector('#location').value);
      processing = true
    }
  };
};

function removeLoading(){
  if(document.querySelector(".center")!= null) document.querySelectorAll(".center").forEach((node)=>{node.remove()})
}

function AddLoading(){
  fs.readFile('./htmls/searchwave.html', (err, html_doc) => {
    if (err) throw err;
    var parser = new DOMParser();
    var wave = parser.parseFromString(html_doc, "text/html");
    document.querySelector("#results").appendChild(wave.documentElement)
  });
}

function SitemapAndSearch(url){
  fs.writeFile('./urls.txt', "", err => {
    if (err) {
      console.error(err)
      return
    }
  })
  fs.writeFile('./ranks.txt', "", err => {
    if (err) {
      console.error(err)
      return
    }
  })
  url = url.replace("&", " ").replace("|", " ")
  removeLoading();
  AddLoading();
  document.querySelectorAll('.card').forEach((node)=>{node.remove()})
    var query = document.querySelector('#query').value;
    var sitemappy = require('child_process').spawn('python', ['./sitemapper.py']);
    sitemappy.stdout.on('data', function (data) {
      data.toString('utf8').split('\n').forEach((link)=>{
        console.log(link)
        if(link.startsWith('http')){
          fs.appendFile('./urls.txt', link, err => {
            if (err) {
              console.error(err)
              return
            }
          })
        }
      })
    });
    sitemappy.stdin.write(url);
    sitemappy.stdin.end();
    sitemappy.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      fs.writeFile('./urls.txt', "", err => {
        if (err) {
          console.error(err)
          return
        }
      })
    });
  
    sitemappy.on('close', (code) => {
      addRanker();
      console.log('completed. now rank.')
      document.querySelector("#status").textContent = "Now Rank..."
    })

  function addRanker() {
    fs.writeFile('./query.txt', query.toString('utf-16'), err => {
      if (err) {
        console.error(err)
        return
      }
    })
    var speller = require('child_process').spawn('python', ['./correction/spellchecking.py']);
    speller.on('close', function (a) {
      fs.readFile('./correction/corrected.txt',(err, data)=> {
        if (err) {
          console.error(err)
          return
        }
        if(data.toString()!=query){
          fs.readFile('./htmls/correction.html', (err, html_doc) => {
            if (err) throw err;
            var parser = new DOMParser();
            var correction = parser.parseFromString(html_doc, "text/html");
            correction.querySelector(".center").textContent=correction.querySelector(".center").textContent.replace('...', data);
            document.querySelector("#results").appendChild(correction.documentElement)
          });
        }
      })
    })
    var ranker = require('child_process').spawn('python', ['./ranker.py']);
    ranker.stdout.on('data', function (data) {
      if(data.toString('utf-8').includes('ready')){
        fs.readFile('./ranks.txt', (err, data) => {
          data = data.toString('utf-8')
          let links_and_ranks = data.split('\n');
          let links = []
          let ranks = []
          links_and_ranks.forEach((value, idx)=>{
            if(idx%2==0)links.push(value)
            else ranks.push(value)
          })
        
          let links_dict = {}

          links.forEach((link, idx)=>{
            links_dict[link] = ranks[idx]
          })

          PrintRanked(links_dict)
        });
      }
    })
    ranker.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      if(!data.toString().startsWith("Some weights of the model checkpoint at")){
        fs.writeFile('./urls.txt', "", err => {
        if (err) {
          console.error(err)
          return
        }
      })
    }
      
    });
    ranker.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
    });
  }
}

function PrintRanked(links_dict){
  var items = Object.keys(links_dict).map(function(key) {
    return [key, links_dict[key]];
  });
  items.sort(function(first, second) {
    return second[1] - first[1];
  });
  removeLoading()
  items.forEach((item)=>{
    if(item[0].length>0){
    fs.readFile('./htmls/pagecard.html', (err, html_doc) => {
      if (err) throw err;
      var parser = new DOMParser();
      var card = parser.parseFromString(html_doc, "text/html");
      card.querySelector(".search-link").textContent=item[0];
      card.querySelector(".search-link").href = item[0]
      document.querySelector("#results").appendChild(card.documentElement)
      console.log(item[0]+"->"+item[1]);
    });
  }
  })
  processing=false
}