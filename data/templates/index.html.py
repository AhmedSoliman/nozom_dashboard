# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1320789752.582667
_template_filename='/Users/ahmed/workspace/personal/nozom/dashboard/dashboard/templates/index.html'
_template_uri='/index.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n\t\t\t<div class="container">\n\t\t\t\t<div class="content">\n\t\t\t\t\t<div class="page-header">\n\t\t\t\t\t\t<h1>Management Dashboard <small>just awesome!</small></h1>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="row">\n\t\t\t\t\t\t<div class="span10">\n\t\t\t\t\t\t    <div id="form-alert"></div>\n\t\n\t\t\t\t\t\t\t<ul class="tabs clearfix" data-tabs="tabs">\n\t\t\t\t\t\t\t\t<li class="active">\n\t\t\t\t\t\t\t\t\t<a href="#add">Add Member</a>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t<a href="#search">Search</a>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t<a href="#log">Log Activity</a>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t\t<li>\n\t\t\t\t\t\t\t\t\t<a href="#renew">Renew Subscription</a>\n\t\t\t\t\t\t\t\t</li>\n\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t<!-- Tab Contents -->\n\t\t\t\t\t\t\t<div class="pill-content clearfix">\n\t\t\t\t\t\t\t\t<div class="active" id="add">\n\t\t\t\t\t\t\t\t\t<form id="newMember" action="/members" method="post">\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="username">Username</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="input-append">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<input placeholder="hamada" id="username" name="username" type="text" class="xlarge" />\n\t\t\t\t\t\t\t\t\t\t\t\t\t<label id="username-indicator" class="add-on hidden"></label>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div> <!-- end of username block -->\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="name">Name</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<input placeholder="Hamada Emam" id="name" name="name" type="text" class="xlarge" />\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of Name block -->\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="email">E-Mail</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t<div class="input-append">\n\t\t\t\t\t\t\t\t\t\t\t\t<input placeholder="sample@domain.com" name="email" id="email" type="text" class="xlarge" />\n\t\t\t\t\t\t\t\t\t\t\t\t<label id="email-indicator" class="add-on hidden"></label>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\t\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of email block -->\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="photo">Personal Photo</label>\n\t\t\t\t\t\t\t\t\t\t\t<input name="photo" type="hidden" value="" />\n\t\t\t\t\t\t\t\t\t\t\t<div id="file-uploader" class="input">\n\t\t\t\t\t\t\t\t\t\t\t    <noscript>          \n\t\t\t\t\t\t\t\t\t\t\t        <p>Please enable JavaScript to use file uploader.</p>\n\t\t\t\t\t\t\t\t\t\t\t        <!-- or put a simple form for upload here -->\n\t\t\t\t\t\t\t\t\t\t\t    </noscript>         \n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t<div id="photoPreview"></div>\n\t\t\t\t\t\t\t\t\t\t\t</div><!-- end of Photo block -->\n\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="national-id" class="required">National ID</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="input-append">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<input id="national-id" type="text" name="national-id" class="xlarge" />\n\t\t\t\t\t\t\t\t\t\t\t\t\t<label id="national-id-indicator" class="add-on hidden"></label>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of National ID block -->\n\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="faculty">Faculty</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<select id="faculty" name="faculty" class="normalSelect xlarge">\n\t\t\t\t\t\t\t\t\t\t\t\t</select>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of Faculty block -->\n\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="twitter">Twitter</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="input-prepend">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="add-on">@</span>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<input placeholder="nozom_ngo" name="twitter" id="twitter" type="text" class="medium" />\n\t\t\t\t\t\t\t\t\t\t\t\t\t<label id="twitter-indicator" class="add-on hidden"></label>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of twitter block -->\n\t\t\t\t\t\t\t\t\t\t\n \t\t\t\t\t\t\t\t\t\t<div class="clearfix">\n\t\t\t\t\t\t\t\t\t\t\t<label for="type">Membership Type</label>\n\t\t\t\t\t\t\t\t\t\t\t<div class="input">\n\t\t\t\t\t\t\t\t\t\t\t\t<select id="type" name="membership-type" class="normalSelect xlarge">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<option value="Normal">\u0639\u0627\u0645\u0644</option>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<option value="Enrollment">\u0627\u0646\u062a\u0633\u0627\u0628</option>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<option value="Honorary">\u0641\u062e\u0631\u064a</option>\n\t\t\t\t\t\t\t\t\t\t\t\t</select>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div><!-- end of Faculty block -->\n\t\t\t\t\t\t\t\t\t\t<div class="actions">\n\t\t\t\t\t\t\t\t\t\t\t<input class="btn large primary" type="submit" value="Add Member" />\n\t\t\t\t\t\t\t\t\t\t\t<button class="btn large" type="reset">\n\t\t\t\t\t\t\t\t\t\t\t\tCancel\n\t\t\t\t\t\t\t\t\t\t\t</button>\n\t\t\t\t\t\t\t\t\t\t</div> <!-- end of actions block -->\n\t\t\t\t\t\t\t\t\t</form>\n\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div id="search">\n\t\t\t\t\t\t\t\t\t...\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div id="log">\n\t\t\t\t\t\t\t\t\t...\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t<div id="renew">\n\t\t\t\t\t\t\t\t\t...\n\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t<!-- End Tab Contents -->\n\t\t\t\t\t\t</div>\n\t\t\t\t\t\t<div class="span4">\n\t\t\t\t\t\t\t<h3>Notes</h3>\n\t\t\t\t\t\t\tFazee3\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'Management')
        return ''
    finally:
        context.caller_stack._pop_frame()


