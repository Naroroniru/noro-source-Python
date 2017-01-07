#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run,template
from bottle import TEMPLATE_PATH, jinja2_template as template
from bottle import static_file

from field import Field


@route('/static/<filepath:path>')
def static(filepath):
  return static_file(filepath, root="./static")

#------以下処理----------------------------------------

tclass = Field()
tclass.start()
tclass.seiretu()

@route('/')
def title():
  # views/syougi.htmlを呼ぶ
  return template("syougi",field = Field.rfield)

run(host='localhost', port=9900, debug=True,reloader=True)