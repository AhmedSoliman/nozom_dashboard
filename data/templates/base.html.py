# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1320789752.589633
_template_filename=u'/Users/ahmed/workspace/personal/nozom/dashboard/dashboard/templates/base.html'
_template_uri=u'/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.TemplateNamespace('__anon_0x10c377e90', context._clean_inheritance_tokens(), templateuri=u'/header.html', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x10c377e90')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x10c377e90')._populate(_import_ns, [u'header'])
        header = _import_ns.get('header', context.get('header', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!doctype html> <!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->\n<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en"> <![endif]-->\n<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en"> <![endif]-->\n<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en"> <![endif]-->\n<!-- Consider adding an manifest.appcache: h5bp.com/d/Offline -->\n<!--[if gt IE 8]><!-->\n<html class="no-js" lang="en">\n\t<!--<![endif]-->\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<!-- Use the .htaccess and remove these lines to avoid edge case issues.\n\t\tMore info: h5bp.com/b/378 -->\n\t\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t\t<title>noZom Managemnt | ')
        # SOURCE LINE 15
        __M_writer(escape(self.title()))
        __M_writer(u' </title>\n\t\t<meta name="description" content="">\n\t\t<meta name="author" content="Ahmed Soliman">\n\t\t<!-- Mobile viewport optimized: j.mp/bplateviewport -->\n\t\t<meta name="viewport" content="width=device-width,initial-scale=1">\n\t\t<!-- Place favicon.ico and apple-touch-icon.png in the root directory: mathiasbynens.be/notes/touch-icons -->\n\t\t<!-- CSS: implied media=all -->\n\t\t<!-- CSS concatenated and minified via ant build script-->\n\t\t<link rel="stylesheet" href="/css/bootstrap.min.css">\n\t\t<link rel="stylesheet" href="/css/style.css">\n\t\t<link rel="stylesheet" href="/css/fileuploader.css">\n\t\t<!-- end CSS-->\n\t\t<!-- More ideas for your <head> here: h5bp.com/d/head-Tips -->\n\t\t<!-- All JavaScript at the bottom, except for Modernizr / Respond.\n\t\tModernizr enables HTML5 elements & feature detects; Respond is a polyfill for min/max-width CSS3 Media Queries\n\t\tFor optimal performance, use a custom Modernizr build: www.modernizr.com/download/ -->\n\t\t<script src="/js/libs/modernizr-2.0.6.min.js"></script>\n\t</head>\n\t<body>\n\t\t<div class="container">\n\t\t\t')
        # SOURCE LINE 35
        __M_writer(escape(header()))
        __M_writer(u'\n\t\t\t')
        # SOURCE LINE 36
        __M_writer(escape(self.body()))
        __M_writer(u'\n\t\t\t<footer>\n\t\t\t\t<p>\n\t\t\t\t\t&copy; noZom Information Technology 2011\n\t\t\t\t</p>\n\t\t\t</footer>\n\n\t\t</div>\n\t\t<!--! end of #container -->\n\t\t<!-- JavaScript at the bottom for fast page loading -->\n\t\t<!-- Grab Google CDN\'s jQuery, with a protocol relative URL; fall back to local if offline -->\n\t\t<script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>\n\t\t<script>window.jQuery || document.write(\'<script src="/js/libs/jquery-1.6.2.min.js"><\\/script>\')</script>\n\t\t<script src="/js/mylibs/jquery.mockjax.js"></script>\n\t\t\n\t\t<!-- scripts concatenated and minified via ant build script-->\n\t\t<script defer src="/js/plugins.js"></script>\n\t\t\n\t\t<script defer src="/js/script.js"></script>\n\t\t<script defer src="/js/mylibs/bootstrap-alerts.js"></script>\n\t\t<script defer src="/js/mylibs/bootstrap-dropdown.js"></script>\n\t\t<script defer src="/js/mylibs/bootstrap-modal.js"></script>\n\t\t<script defer src="/js/mylibs/bootstrap-tabs.js"></script>\n\t\t<script defer src="/js/mylibs/jquery.form.js"></script>\n\t\t<script defer src="/js/mylibs/jquery.scrollTo-min.js"></script>\n\t\t<script defer src="/js/mylibs/fileuploader.js"></script>\n\t\t<!-- end scripts-->\n\t\t<!-- Change UA-XXXXX-X to be your site\'s ID -->\n\t\t<!-- <script>\n\t\t\twindow._gaq = [[\'_setAccount\', \'UAXXXXXXXX1\'], [\'_trackPageview\'], [\'_trackPageLoadTime\']];\n\t\t\tModernizr.load({\n\t\t\t\tload : (\'https:\' == location.protocol ? \'//ssl\' : \'//www\') + \'.google-analytics.com/ga.js\'\n\t\t\t});\n\n\t\t</script> -->\n\t\t<!-- Prompt IE 6 users to install Chrome Frame. Remove this if you want to support IE 6.\n\t\tchromium.org/developers/how-tos/chrome-frame-getting-started -->\n\t\t<!--[if lt IE 7 ]>\n\t\t<script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>\n\t\t<script>window.attachEvent(\'onload\',function(){CFInstall.check({mode:\'overlay\'})})</script>\n\t\t<![endif]-->\n\n\t</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


