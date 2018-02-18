# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
	('male', 'Male'),
	('female', 'Female')
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
	severity = models.CharField(max_length=255, blank=True, null=True)

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
		return "%s - %s - %s" % (self.address1. self.city, self.country)


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
