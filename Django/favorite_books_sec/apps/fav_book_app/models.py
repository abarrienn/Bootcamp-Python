from __future__ import unicode_literals
from django.db import models
import re  
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
NAME_REGEX = re.compile(r'^[a-zA-Z]')
import bcrypt


class userManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2 or not postData['fname'].isalpha():
            errors['fname'] = "Name must be at least 2 characters."
        if len(postData['lname']) < 2 or not postData['lname'].isalpha():
            errors['lname'] = "Name must be at least 2 characters."
        if EMAIL_REGEX.match(postData['email']) == None:
            errors['email'] = "Invalid email format."
        if User.objects.filter(email = postData['email']):#this checks to see if email is unique
        	errors['email'] = "Email is already taken. Please login or provide another email address."
        if len(postData['password']) < 8:
            errors['password'] = "Text length must be more than 10 characters."
        if postData['password'] != postData['confirm_password']:
        	errors['password'] = "Password and Confirm password do not match." 
        return errors
    def login_validate(self, postData):
    	user = User.objects.filter(email = postData['email'])
    	errors = {}
    	if not user:
    		errors['email'] = "Please enter a valid email address."
    	if user and not bcrypt.checkpw(postData['password'].encode('utf8'), user[0].password.encode('utf8')):
    		errors['password'] = "Invalid password."
    	return errors

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = userManager()

class bookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters."
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least 5 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name= "books")
    users_who_liked = models.ManyToManyField(User, related_name="favd_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = bookManager()
