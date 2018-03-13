# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	('male', 'Male'),
	('female', 'Female')
)
SEVERITY_CHOICES = (
	('minor','Minor'),
	('major','Major'),
	('critical','Critical')
)

STATUS_CHOICES=(
('pending','Pending'),
('accepted','Accepted'),
('progress','Progress'),
('completed','Completed')
)


BLOOD_GROUP_CHOICES = (
	('apositive', 'A+'),
	('anegative', 'A-'),
	('opositive', 'O+'),
	('bpositive', 'B+'),
	('abpositive', 'AB+'),
	('abnegative', 'AB-'),
	('onegative', 'O-'),
	('bnegative', 'B-'),
)


class UserRequest(models.Model):
	user = models.ForeignKey(User)
	location = models.CharField(max_length=255, blank=True, null=True)
	mobile = models.IntegerField(default=0)
	reason = models.TextField(blank=True, null=True)
	severity = models.CharField(max_length=255, blank=True, null=True, choices=SEVERITY_CHOICES)
 	count_of_persons_injured = models.IntegerField(default=1)
	status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES)
	def __unicode__(self):
		return "%s - %s" % (self.location, self.mobile)


class Address(models.Model):
	address1 = models.CharField(max_length=255, blank=True, null=True)
	address2 = models.CharField(max_length=255, blank=True, null=True)
	landmark = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	state = models.CharField(max_length=255, blank=True, null=True)
	pincode = models.IntegerField(default=0)
	country = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return "%s - %s - %s" % (self.address1, self.city, self.country)


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	dob = models.DateField(blank=True, null=True)
	gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDER_CHOICES)
	mobile_number = models.CharField(max_length=25, blank=True, null=True)
	alternate_number = models.CharField(max_length=25, blank=True, null=True)
	blood_group = models.CharField(max_length=255, blank=True, null=True, choices=BLOOD_GROUP_CHOICES)
	address = models.ForeignKey(Address, blank=True, null=True)

	def __unicode__(self):
		return "%s - %s - %s" % (self.user, self.gender, self.blood_group)
class HospitalProfile(models.Model):
	user = models.OneToOneField(User)
	hos_reg_id = models.CharField(max_length=255, blank=True, null=True)
	hos_dir_name = models.CharField(max_length=255, blank=True, null=True)
 	hos_reg_date = models.DateField(blank=True, null=True)
	ambulance_count = models.IntegerField(default=0)
  	hospital_mobile = models.CharField(max_length=25, blank=True, null=True)
	address = models.ForeignKey(Address, blank=True, null=True)

	def __unicode__(self):
		return "%s - %s - %s" %(self.user, self.hos_dir_name, self.ambulance_count)
