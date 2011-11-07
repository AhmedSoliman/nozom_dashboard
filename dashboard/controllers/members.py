import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dashboard.lib.base import BaseController, render

from dashboard.model.member import Member
import simplejson
from mongoengine.base import ValidationError
from mongoengine.queryset import OperationError

log = logging.getLogger(__name__)

class MembersController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('member', 'members')

    def index(self, format='html'):
        """GET /members: All items in the collection"""
        # url('members')

    def create(self):
        """POST /members: Create a new item"""
        # url('members')
        log.info("Creating new Member")
        response.content_type = "application/json"
        try:
            member = Member()
            member.username = request.params['username']
            member.name = request.params['name']
            member.email = request.params['email']
            member.national_id = request.params['national-id']
            member.faculty = request.params.get('faculty')
            member.twitter_id = request.params.get('twitter')
            member.membership_type = request.params['membership-type']
            member.save()
        except ValidationError, e:
            response.status = "500 Server Error"
            return simplejson.dumps({'success': False, 'reason': "Invalid input!"})
        except OperationError, e:
            response.status = "500 Server Error"
            log.error("Error while adding member:" + e)
            return simplejson.dumps({'success': False, 'reason': "probably trying to add a member with duplicate info"})
        except Exception, e:
            response.status = "500 Server Error"
            log.error(e)
            return simplejson.dumps({'success': False, 'reason': "Unknown!"})            
            
        response.status = "201 Created"
        return simplejson.dumps({'success': True, 'member_id': str(member.id)})


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

    def edit(self, id, format='html'):
        """GET /members/id/edit: Form to edit an existing item"""
        # url('edit_member', id=ID)
