#!/usr/bin/python
# -*- coding: utf-8 -*-

default_application = 'wikilinuxdevel'    # ordinarily set in base routes.py
default_controller = 'default'  # ordinarily set in app-specific routes.py
default_function = 'index'      # ordinarily set in app-specific routes.py

routes_in = (
  ('/$anything', '/wikilinuxdevel/$anything'),
  ('*./favicon.ico', '/wikilinuxdevel/static/images/favicon.ico'),
  ('*./favicon.png', '/wikilinuxdevel/static/images/favicon.png'),
  ('*./robots.txt', '/wikilinuxdevel/static/robots.txt'),
  )

routes_out = [(x, y) for (y, x) in routes_in[:-3]]
