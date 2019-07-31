# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.randint(2,4)
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie':'thw=cn; t=66a2a0725840f97b7632f908fb6bcca8; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _m_h5_tk=8c2b6b32537cdf5825b738d68a9c7597_1564551044603; _m_h5_tk_enc=569fd72953bc52aa98576426c1e636d8; cookie2=10bc86b7dd88334fe632141f46de5d28; _tb_token_=ef63f8adee36b; cna=F3grFYSUI3cCAXAYEoprUyzK; v=0; unb=3316996195; uc3=id2=UNN8HulXUM%2BVWw%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&vt3=F8dBy32nLPk4RLD4ZL0%3D&nk2=ogVZTAoWGtIMAALD5tnLuiny; csg=83d68b1b; lgc=%5Cu6D41%5Cu901D%5Cu7684%5Cu65F6%5Cu514952997069; cookie17=UNN8HulXUM%2BVWw%3D%3D; dnk=%5Cu6D41%5Cu901D%5Cu7684%5Cu65F6%5Cu514952997069; skt=50b0bb7fe3204260; existShop=MTU2NDU2MTk1NA%3D%3D; uc4=id4=0%40UgQ0prV48LysjJRBTa%2BEovh5ryN0&nk4=0%40oAekTO52Jf9U3SHIjBYi3Qhw45m8XdIoLThZkZE%3D; tracknick=%5Cu6D41%5Cu901D%5Cu7684%5Cu65F6%5Cu514952997069; _cc_=URm48syIZQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=951; _nk_=%5Cu6D41%5Cu901D%5Cu7684%5Cu65F6%5Cu514952997069; cookie1=BYK21v%2FWovOIgmDu65bIZafpmqMqaSOZW2ToOh7c7Wo%3D; mt=ci=8_1; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=UtASsssme%2BBq&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTaHP3OMMvRZQ%3D%3D&tag=8&lng=zh_CN; enc=wVVYiFml3MWvNJzop1aC6n378RTV%2BNpf%2BqqrVCb%2FsMVazyyH%2FO7kR0UQKV%2BtK27K7TUnujCXg3fld9j2hws3Kw%3D%3D; JSESSIONID=AB0BFC771CC33509033ADE29DA4E148A; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=278558; isg=BMzMmV5D_V5wq-hI6hwwwiGLnSo-rXCmYlrD6CaNhncqsWy7ThTGPy8DUfks_qgH; l=cBEFZeMPvn7HPlq9BOCwnurza77OLIRA_uPzaNbMi_5QP6YSI-QOkSMc-Fv6cjWd928B4k6UXwp9-etkiDgP9P--g3fP.; whl=-1%260%260%261564561971203',
    'pragma': 'no-cache',
    'referer': 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E9%9E%8B%E5%AD%90&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao.pipelines.TaobaoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
