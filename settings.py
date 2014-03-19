AUTHOR = "BA"
SITEURL = "http://bloguze.com"
SITENAME = "Bloguze"
LOCALE = 'en_US.UTF-8'
TIMEZONE = 'Europe/Istanbul'

DISPLAY_PAGES_ON_MENU = True
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

THEME = "pelican-theme"

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
