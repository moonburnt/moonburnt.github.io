#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "moonburnt"
# Whatever is displayed in site name and header.
# If not set, will be "A Pelican Blog"
SITENAME = "Moonburnt's Blog"
# This will be used to generate rss feeds. Comment out for testing
SITEURL = "https://moonburnt.github.io"

# Path to articles
PATH = "content"

TIMEZONE = "Europe/Helsinki"

DEFAULT_LANG = "en"

# Replace this with path to custom theme. If certain pages dont have custom style,
# pelican will use default
#THEME = "themes/basic"

# Generate feeds to provided files
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
# {slug} will be replaced with context
#AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
#AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"
#CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
#CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
#TRANSLATION_FEED_ATOM = None

# Toggle exclusion of whole message's content from feed posts
RSS_FEED_SUMMARY_ONLY = False

# Static paths to be used in articles with ({static}/directory/file) syntax
STATIC_PATHS = [
    "images",
]

# Additional links to put on footer
LINKS = (
    ("Github", "https://github.com/moonburnt"),
)

# Same as above, except with different placement and name
#SOCIAL = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
