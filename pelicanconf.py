#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "pelican-octopress-theme"

AUTHOR = u'ChenSP'
SITENAME = u'LifeStyle'
SITEURL = ''
SITESUBTITLE= '简约&LifeStyle'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

#Social widget
SOCIAL = (('QQ', 'http://wpa.qq.com/msgrd?v=3&uin=1016395220&site=chensp&menu=yes'),)

DEFAULT_PAGINATION = 10

#show pages
DISPLAY_PAGES_ON_MENU = False
#show categories
DISPLAY_CATEGORIES_ON_MENU = True
#show feed icons (on the very right side) 
DISPLAY_FEEDS_ON_MENU = True 

ARCHIVE_TITLE= "Blog Archive"
FAVICON_FILENAME="favicon.png"

GITHUB_USER = u'ChenSP'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False 
GITHUB_SHOW_USER_LINK = False 

#Adds specified image to sidebar. Example value: "images/author_photo.jpg"

SIDEBAR_IMAGE = "favicon.png"
#SIDEBAR_IMAGE_ALT : Alternative text for sidebar image
#SIDEBAR_IMAGE_WIDTH : Width of sidebar image

#set to true to enable site search box
SEARCH_BOX = True
#[default: 'http://google.com/search'] search engine to which search form should be pointed (optional)
SITESEARCH = 'http://baidu.com/search'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
