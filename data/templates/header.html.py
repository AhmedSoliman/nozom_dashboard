# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1320789308.583139
_template_filename=u'/Users/ahmed/workspace/personal/nozom/dashboard/dashboard/templates/header.html'
_template_uri=u'/header.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\t\t\t<header class="topbar">\n\t\t\t\t<div class="fill">\n\t\t\t\t\t<div class="container">\n\t\t\t\t\t\t<a class="brand" href="#">\u0646\u0638\u0645 \u0644\u062a\u0643\u0646\u0648\u0644\u0648\u062c\u064a\u0627 \u0627\u0644\u0645\u0639\u0644\u0648\u0645\u0627\u062a</a>\n\t\t\t\t\t\t<ul class="nav">\n\t\t\t\t\t\t\t<li class="active">\n\t\t\t\t\t\t\t\t<a href="#">Home</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="#about">About</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t<a href="#contact">Contact</a>\n\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t<form action="" class="pull-right">\n\t\t\t\t\t\t\t<input class="input-small" type="text" placeholder="Username">\n\t\t\t\t\t\t\t<input class="input-small" type="password" placeholder="Password">\n\t\t\t\t\t\t\t<button class="btn" type="submit">\n\t\t\t\t\t\t\t\tSign in\n\t\t\t\t\t\t\t</button>\n\t\t\t\t\t\t</form>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


