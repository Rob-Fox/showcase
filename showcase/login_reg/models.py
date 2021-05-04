from __future__ import unicode_literals
from django.db import models
import re, bcrypt


# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "Name must be at least 3 characters long."
        if not NAME_REGEX.match(postData['name']):
            errors['name'] = 'Name must be comprised of letters only.'
        if len(postData['username']) < 3:
            errors['username'] = "Username must be at least 3 characters long."
        if not NAME_REGEX.match(postData['username']):
            errors['username'] = 'Username must be comprised of letters only.'
        if User.objects.filter(username = postData['username']):
            errors['username'] = "You have already registered or that Username is already taken."
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a password that is 8 characters or longer."
        if postData['password'] != postData['c_password']:
            errors['password'] = "Entered passwords do not match. Please enter the same password in both fields."
        return errors

    def login_validator(self, postData):
        errors = {}
        if not User.objects.filter(username=postData["l_username"]):
            errors["l_username"] = "Sorry. That Username does not exist. Perhaps try creating an account?"
        if len(postData["l_password"]) < 8:
            errors["l_password"] = "Please enter a valid password."
        if not User.objects.filter(username=postData['l_username']):
            if not bcrypt.checkpw(postData['l_password'].encode(), User.objects.get(username=postData["l_username"]).password.encode()):
                errors['l_password'] = "That Username and password combo is incorrect. Please try again."
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)

    objects = UserManager()

    def name_array(self):
        return self.name.split(' ')

    # When asked for a representation of itself what is returned
    def __repr__(self):
        return 'name: {}, username {}, password {}'.format(self.name, self.username, self.password)
