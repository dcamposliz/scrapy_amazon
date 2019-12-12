# scrapy_amazon

This repository is based on the following tutorials:

* <https://scrapy.org/>
* [YouTube: Python Scrapy Tutorial - 22 - Web Scraping Amazon](https://www.youtube.com/watch?v=2vcp0fKq3aw&t=102s)

Starting this project:

```
scrapy startproject amazon
scrapy genspider example example.com
```

To run this project:

`cd` into the directory containing the file `scrapy.cfg`, then run:

```
scrapy crawl amazonspider -o data.csv
```