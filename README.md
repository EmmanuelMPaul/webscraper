## About

<p align="left">Learning webscraping using BeautifulSoup library</p>
<p align="left">A simple tool for  
downloading courses from - codecourse (premium account is required to use this tool)
</P>

## Requirements
- [composer](https://getcomposer.org/) 
- [php >=7.1](https://github.com/php/php-src/releases)
- [git](https://git-scm.com)
- [python 3 ](https://www.python.org/downloads)  

## Usage

```bash
    $  git clone https://github.com/EmmanuelMPaul/webscraper.git
    $  cd webscraper
    $  php codecourse auth:me           Check if you're authenticated
    $  php codecourse auth:signin       Sign in with your codecourse.com credentials
    $  pip install                      [pyhon packages(os,re,requests,BeautifulSoup)]
    $  python allscraper.py             to download all types courses + snippet
    $  python cscraper.py               to download courses only
    $  python sscraper.py               to download snippets only
    $  python localscraper.py           to download courses from a file source
```
visit [codecourse](https://codecourse.com) to view the courses

<p align="center"><img src="https://repository-images.githubusercontent.com/206791420/546e5980-d0ca-11e9-9e2a-9b920b7a8304" width="500"></p>
