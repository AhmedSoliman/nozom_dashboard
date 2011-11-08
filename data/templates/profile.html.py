# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1320791172.526749
_template_filename='/Users/ahmed/workspace/personal/nozom/dashboard/dashboard/templates/profile.html'
_template_uri='/profile.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\t\t\t<div class="container">\n\t\t\t\t<div class="content">\n\t\t\t\t\t<div class="row">\n    \t\t\t\t\t<div class="span3">\n    \t\t\t\t\t    <img width="150" src="')
        # SOURCE LINE 7
        __M_writer(escape(h.url('view_photo', filename=c.member.photo)))
        __M_writer(u'" alt="Ahmed Soliman" />\n    \t\t\t\t\t    <a href="/edit/" class="small-action">Change Avatar</a>\n    \t\t\t\t\t    <ul class="unstyled">\n    \t\t\t\t\t    \t<li><a href="#" >Edit</a></li>\n    \t\t\t\t\t    \t<li><a href="#" >Delete Member</a></li>\n    \t\t\t\t\t    </ul>\n    \t\t\t\t\t</div>\n    \t\t\t\t\t<div class="span10">\n\t        \t\t\t\t<section id="profile-info">\n\t        \t\t\t\t\t<h2 class="pull-right member-id">#')
        # SOURCE LINE 16
        __M_writer(escape(c.member.member_id))
        __M_writer(u'</h2>\n\t        \t\t\t\t\t<h1>')
        # SOURCE LINE 17
        __M_writer(escape(c.member.name))
        __M_writer(u' <small>')
        __M_writer(escape(c.member.username))
        __M_writer(u'</small></h1>\n\t        \t\t\t\t\t<span class="label">\u0639\u0636\u0648 \u0639\u0627\u0645\u0644</span>\n\t        \t\t\t\t\t<ul class="unstyled">\n\t        \t\t\t\t\t\t<li>Mahawees Editor in Chief </li>\n\t        \t\t\t\t\t\t<li>Executive Committe Member </li>\n\t        \t\t\t\t\t</ul>\n\n\t\t        \t\t\t\t<div class="page-header">\n\t\t\t\t\t\t\t\t\t<h2>Personal Information</h2>\n\t\t        \t\t\t\t</div>\n\t        \t\t\t\t\t\n\t        \t\t\t\t\t<form id="personal-info">\n\t        \t\t\t\t\t\t<div class="clearfix">\n\t\t\t        \t\t\t\t\t<label>E-Mail</label>\n\t\t\t        \t\t\t\t\t<div class="input">\n\t\t\t        \t\t\t\t\t\t<span><a href="#">')
        # SOURCE LINE 32
        __M_writer(escape(c.member.email))
        __M_writer(u'</a></span>\n\t\t\t        \t\t\t\t\t\t<button class="btn info">Send Email</button>\n\t\t\t        \t\t\t\t\t</div>\n\t\t        \t\t\t\t\t</div>\n\t\n\t        \t\t\t\t\t\t<div class="clearfix">\n\t\t\t        \t\t\t\t\t<label>National ID</label>\n\t\t\t        \t\t\t\t\t<div class="input">\n\t\t\t        \t\t\t\t\t\t<span>')
        # SOURCE LINE 40
        __M_writer(escape(c.member.national_id))
        __M_writer(u'</span>\n\t\t\t        \t\t\t\t\t</div>\n\t\t        \t\t\t\t\t</div>\n\t\t        \t\t\t\t\t\n\t        \t\t\t\t\t\t<div class="clearfix">\n\t\t\t        \t\t\t\t\t<label>Twitter</label>\n\t\t\t        \t\t\t\t\t<div class="input">\n\t\t\t        \t\t\t\t\t\t<a href="#">')
        # SOURCE LINE 47
        __M_writer(escape(c.member.twitter_id))
        __M_writer(u'</a>\n\t\t\t        \t\t\t\t\t</div>\n\t\t        \t\t\t\t\t</div>\n\t\n\t        \t\t\t\t\t</form>\n        \t\t\t\t\t</section>\n        \t\t\t\t<section id="activity-log">\n\t        \t\t\t\t<div class="page-header">\n\t\t\t\t\t\t\t\t<h2>Activity Log</h2>\n\t        \t\t\t\t</div>\n\t\t\t\t\t\t\t<table>\n\t\t\t\t\t\t\t\t<thead>\n\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t<th>Datetime</th>\n\t\t\t\t\t\t\t\t\t\t<th>Activity</th>\n\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t</thead>\n\t\t\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t<td class="date">24/12/2011 12:30PM</td>\n\t\t\t\t\t\t\t\t\t\t<td>Doing something that matters to the history of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, </td>\n\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t\t<td class="date">24/12/2011 12:30PM</td>\n\t\t\t\t\t\t\t\t\t\t<td>Doing something that matters to the history oadsff data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history oasdff data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to tfhe historadsfy of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, \n\t\t\t\t\t\t\t\t\t\t\tDoing something that matters to the history of data structures, Doing something that matters to the history of data structures, </td>\n\t\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t\t</table>        \t\t\t\t\t\n        \t\t\t\t</section>\n    \t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<!-- /container -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(escape(c.member.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


