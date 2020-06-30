# stf_get_links
Crawls the Brazilian Supreme Federal Court's Database for judicial decisions in ADI cases and corresponding PDF files.

## Requirements

1. Scrapy + Splash:
* Scrapy Installation Guide: https://docs.scrapy.org/en/latest/intro/install.html
* Splash Documentation: https://github.com/scrapy-plugins/scrapy-splash

2. Tesseract:
* Tesseract Documentation: https://github.com/tesseract-ocr/tesseract

## Brief Explanation

This spider scrapes only the case and PDF links for each ADI case in the Database. The fact that the website uses javascript limits the functionality of CrawlSpiders, so I chose to split the task in two:
- stf_get_links scrapes the relevant links and stores them in a CSV file.
- [stf_get_csv](https://github.com/prldc/stf_get_csv) scrapes the actual case information: 

  * case brief
  * court ruling
  * internal case classification
  * relevant legislation
  * related cases
  * scholarship cited
  * decision date
  * plaintiffs
  * further observations.



