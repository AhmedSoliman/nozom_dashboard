from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, EmailField, ListField,\
	EmbeddedDocumentField, DateTimeField
import datetime

class ActivityLogEntry(EmbeddedDocument):
	datetime = DateTimeField(default=lambda: datetime.datetime.now())
	description = StringField(required=True)

class Member(Document):
	member_id = StringField(required=True, unique=True)
	name = StringField(required=True)
	username = StringField(required=True, unique=True)
	email = EmailField(required=True, unique=True)
	national_id = StringField(required=True, unique=True)
	photo = StringField(required=True, unique=True)
	faculty = StringField()
	twitter_id = StringField(unique=True)
	membership_type = StringField(required=True)
	subscription_valid_until = StringField(required=True, default=lambda: datetime.datetime.now().year + 1)
	special_titles = ListField(StringField) #for any additional titles in noZom, like CEO
	activities_log = ListField(EmbeddedDocumentField(ActivityLogEntry))
	
	