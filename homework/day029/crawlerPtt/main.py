import scrapy
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    #target_board = ['Gossiping', 'Stock']
    target_board = ['Gossiping']
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('crawlerPTT', board=board)
        process.start()

if __name__ == '__main__':
    main()

    ##cmd:python main.py https://www.ptt.cc/bbs/Gossiping/M.1559788476.A.074.html