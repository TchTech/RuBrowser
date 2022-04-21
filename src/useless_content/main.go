package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"

	"github.com/anaskhan96/soup"
)

func main() {
	err := ioutil.WriteFile("ranks.txt", []byte(""), 0644)

	if err != nil {
		os.Exit(1)
	}

	var query string
	fmt.Scanf("%s", &query)

	content, err := ioutil.ReadFile("urls.txt")

	err = ioutil.WriteFile("ss.txt", []byte(query), 0644)

	if err != nil {
		os.Exit(1)
	}

	var links = strings.Fields(string(content))

	for _, link := range links {
		resp, err := soup.Get(link)
		if err != nil {
			os.Exit(1)
		}
		doc := soup.HTMLParse(resp).FullText()
		//header := soup.HTMLParse(resp).Find("title").Text()
		score := CustomSearch(doc, query)
		// rubert := exec.Command("python bertforgo.py --header " + header + " --query " + query)
		// var outb, errb bytes.Buffer
		// rubert.Stdout = &outb
		// rubert.Stderr = &errb
		// rubert.Run()
		// fmt.Println(outb.String())
		// stdout, _ := rubert.CombinedOutput()
		// bertscore, _ := strconv.ParseFloat((string(stdout)), 64)
		// fmt.Println(strconv.FormatFloat(bertscore, 'f', -1, 64) + "\n")
		// score += bertscore
		f, err := os.OpenFile("ranks.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
		if err != nil {
			os.Exit(1)
		}
		if _, err := f.Write([]byte(link + "\n" + strconv.Itoa(score) + "\n")); err != nil {
			os.Exit(1)
		}
		if err := f.Close(); err != nil {
			os.Exit(1)
		}
		fmt.Println(link + "\n" + strconv.Itoa(score))
	}

}

func CustomSearch(text string, query string) int {
	return strings.Count(strings.ToLower(text), strings.ToLower(query))
}
