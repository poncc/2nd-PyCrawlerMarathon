import scrapy
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    #target_urls = [
    #    'https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html',
    #    'https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html'
    #]
    target_urls=[]
    for arg in sys.argv[1:]:
        target_urls.append(arg.strip())
    print(target_urls)
    process = CrawlerProcess(get_project_settings())
    process.crawl('crawlerPTT', start_urls=target_urls, filename='test.json')
    process.start()

if __name__ == '__main__':
    main()

    ##cmd:python main.py https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html