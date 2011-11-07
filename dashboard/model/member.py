from mongoengine.document import Document
from mongoengine.fields import StringField, EmailField

class Member(Document):
	name = StringField(required=True)
	username = StringField(required=True, unique=True)
	email = EmailField(required=True, unique=True)
	national_id = StringField(required=True, unique=True)
	faculty = StringField()
	twitter_id = StringField(unique=True)
	membership_type = StringField(required=True)
