# Scrapy settings for yeeyan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import datetime

BOT_NAME = 'yeeyan'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['yeeyan.spiders']
NEWSPIDER_MODULE = 'yeeyan.spiders'
ITEM_PIPELINES = ['yeeyan.pipelines.YeeyanPipeline']
DEFAULT_ITEM_CLASS = 'yeeyan.items.YeeyanItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
LOG_LEVEL='INFO'

log_file = str(datetime.datetime.now()).split(' ')[0]+'.log'
LOG_FILE = log_file
