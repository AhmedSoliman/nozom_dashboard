import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dashboard.lib.base import BaseController, render

from dashboard.model.member import Member
import simplejson
from mongoengine.base import ValidationError
from mongoengine.queryset import OperationError
import shutil
from pylons import config
import os
import random
import time
from pymongo.errors import DuplicateKeyError
import traceback

log = logging.getLogger(__name__)

def generate_member_id():
    while True:
        randID = time.strftime('%y%d%m') + str(random.randint(1000, 9999))
        if Member.objects(member_id=randID).count() == 0:
            break
    return randID

def get_param(request, param):
    value = request.params.get(param)
    if value:
        return value
    else:
        return None
    
class MembersController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('member', 'members')

    def index(self, format='html'):
        """GET /members: All items in the collection"""
        # url('members')
        return render('/index.html')

    def create(self):
        """POST /members: Create a new item"""
        # url('members')
        log.info("Creating new Member")
        response.content_type = "application/json"
        try:
            member = Member()
            member.username = get_param(request, 'username')
            member.member_id = generate_member_id()
            member.name = get_param(request, 'name')
            member.email = get_param(request, 'email')
            member.national_id = get_param(request, 'national-id') 
            member.faculty = get_param(request, 'faculty')
            member.twitter_id = get_param(request, 'twitter')
            member.membership_type = get_param(request, 'membership-type')
            photo_name = get_param(request, 'photo')
            member.photo = photo_name
            #process photo
            tmp_photo = os.path.join(
                config['app_conf']['tmp_store'],
                photo_name
            )
            if not photo_name or not os.path.exists(tmp_photo):
                response.status = "500 Server Error"
                return simplejson.dumps({'success': False, 'reason': "Missing photo!"})
            shutil.copy(tmp_photo, os.path.join(
                config['app_conf']['permanent_store'],
                photo_name
            ))
            
            member.save(safe=True, force_insert=True, validate=True)
            os.unlink(tmp_photo)
            
        except ValidationError, e:
            response.status = "500 Server Error"
            traceback.print_exc()
            return simplejson.dumps({'success': False, 'reason': "Invalid input!"})
        except (OperationError, DuplicateKeyError), e:
            response.status = "500 Server Error"
            log.error("Error while adding member:" + str(e))
            traceback.print_exc()
            return simplejson.dumps({'success': False, 'reason': "probably trying to add a member with duplicate info"})
        except Exception, e:
            response.status = "500 Server Error"
            log.error("Unknown Error:" + str(e))
            traceback.print_exc()
            return simplejson.dumps({'success': False, 'reason': "Unknown!"})            
            
        response.status = "201 Created"
        return simplejson.dumps({'success': True, 'member_id': str(member.member_id)})


    def new(self, format='html'):
        """GET /members/new: Form to create a new item"""
        # url('new_member')

    def update(self, id):
        """PUT /members/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('member', id=ID),
        #           method='put')
        # url('member', id=ID)

    def delete(self, id):
        """DELETE /members/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('member', id=ID),
        #           method='delete')
        # url('member', id=ID)

    def show(self, id, format='html'):
        """GET /members/id: Show a specific item"""
        # url('member', id=ID)
        member = Member.objects(member_id=id).first()
        if not member:
            abort(404)
        
        c.member = member
        if format == 'html':
            return render('/profile.html')
        else:
            return "Hello World"

    def edit(self, id, format='html'):
        """GET /members/id/edit: Form to edit an existing item"""
        # url('edit_member', id=ID)
