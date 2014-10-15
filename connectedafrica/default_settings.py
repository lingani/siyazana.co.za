import os

DEBUG = True
ASSETS_DEBUG = False

FLATPAGES_ROOT = '../pages'
FLATPAGES_EXTENSION = '.md'


APP_NAME = 'Siyazana'

GRANO_HOST = os.environ.get('GRANO_HOST', 'http://beta.grano.cc/')
GRANO_APIKEY = os.environ.get('GRANO_APIKEY')
GRANO_PROJECT = os.environ.get('GRANO_PROJECT', 'southafrica')

WINDEEDS_USER = os.environ.get('WINDEEDS_USER')
WINDEEDS_PASS = os.environ.get('WINDEEDS_PASS')

DOCCLOUD_HOST = os.environ.get('DOCCLOUD_HOST',
                               'http://sourceafrica.net/')
DOCCLOUD_USER = os.environ.get('DOCCLOUD_USER')
DOCCLOUD_PASS = os.environ.get('DOCCLOUD_PASS')
DOCCLOUD_PROJECT = int(os.environ.get('DOCCLOUD_PROJECT', '130'))

SOURCE_NAMES = {
    'za-new-import.popit.mysociety.org': "People's Assembly Data",
    'www.windeedsearch.co.za': "Windeed CIPC Search",
}
