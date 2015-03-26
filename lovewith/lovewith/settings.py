# -*- coding: utf-8 -*-

# Scrapy settings for lovewith project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lovewith'

SPIDER_MODULES = ['lovewith.spiders']
NEWSPIDER_MODULE = 'lovewith.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lovewith (+http://www.yourdomain.com)'


# DOWNLOADER_MIDDLEWARES = {
#     #'misc.middleware.CustomHttpProxyMiddleware': 400,
#     'misc.middleware.CustomUserAgentMiddleware': 401,
# }

ITEM_PIPELINES = {
    'lovewith.pipelines.LovewithPipeline': 300,
    #'template.pipelines.RedisPipeline': 301,
}

LOG_LEVEL = 'INFO'
