# Scrapy settings for yeeyan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'yeeyan'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['yeeyan.spiders']
NEWSPIDER_MODULE = 'yeeyan.spiders'
DEFAULT_ITEM_CLASS = 'yeeyan.items.YeeyanItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

