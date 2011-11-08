import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify
from dashboard.lib.base import BaseController, render

from dashboard.model.member import Member
import shutil
from mimetypes import guess_type
import simplejson
import os

from pylons import config
import hashlib
import stat
from PIL import Image
import cStringIO

log = logging.getLogger(__name__)

MAXSIZEX = 350 # this is the maximum width of the images
MAXSIZEY = 412 # this is the maximum height of the images
ratio = 1. * MAXSIZEX / MAXSIZEY

class ApiController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/api.mako')
        # or, return a string
        return 'Nothing in here'

    @jsonify
    def is_available(self):       
        if 'field' not in request.params or 'value' not in request.params:
            abort(401)
        
        field = request.params['field']
        value = request.params['value']
        if Member.objects(**{field: value}).count():
            return False
        else:
            return True
    
    def photo(self, filename):
        permanent_file = open(
            os.path.join(
                config['app_conf']['permanent_store'],
                filename
            ),
            'r'
        )    
        data = permanent_file.read()
        permanent_file.close()
        response.content_type = guess_type(filename)[0] or 'text/plain'
        return data
        
    def tmp_photo(self):
        filename = request.GET['filename']
        permanent_file = open(
            os.path.join(
                config['app_conf']['tmp_store'],
                filename
            ),
            'r'
        )    
        data = permanent_file.read()
        permanent_file.close()
        response.content_type = guess_type(filename)[0] or 'text/plain'
        return data
    
    def photo_upload(self):
        myfile = request.params['qqfile']
        extension = myfile[myfile.rfind('.'):]
        max_upload_size = int(config['app_conf']['max_upload_size'])
        
        if len(request.body) > max_upload_size * 1024: #convert to kb
            return simplejson.dumps({'success': False, 'reason': 'File exceeded the %sk limit' % max_upload_size})
        
        #filename is the SHA1 for efficient storage usage
        algo = hashlib.sha1()
        algo.update(request.body)
        new_name = algo.hexdigest() + extension
        #buffer the file in memory after are are sure that it's not
        #more than the max-size
        tmp_file = cStringIO.StringIO(request.body)


        im = Image.open(tmp_file) # open the input file
        (width, height) = im.size        # get the size of the input image
        
        if width > height * ratio:
            # crop the image on the left and right side
            newwidth = int(height * ratio)
            left = width / 2 - newwidth / 2
            right = left + newwidth
            # keep the height of the image
            top = 0
            bottom = height
        elif width < height * ratio:
            # crop the image on the top and bottom
            newheight = int(width * ratio)
            top = height / 2 - newheight / 2
            bottom = top + newheight
            # keep the width of the impage
            left = 0
            right = width
        if width != height * ratio:
            im = im.crop((left, top, right, bottom))
            
        im = im.resize((MAXSIZEX, MAXSIZEY), Image.ANTIALIAS)
        fout = open(os.path.join(
                config['app_conf']['tmp_store'],
                new_name
            ), 'wb')
        im.save(fout, "jpeg", quality = 90) # save the image
        fout.close()
        tmp_file.close()
        return simplejson.dumps({'success': True, 'filename': new_name})