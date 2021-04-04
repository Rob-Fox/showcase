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
        if users.objects.filter(username = postData['username']):
            errors['username'] = "You have already registered or that Username is already taken."
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a password that is 8 characters or longer."
        if postData['password'] != postData['confirmPassword']:
            errors['password'] = "Entered passwords do not match. Please enter the same password in both fields."
        return errors

    def login_validator(self, postData):
        errors = {}
        if not User.objects.filter(username=postData["loginUsername"]):
            errors["loginUsername"] = "Sorry. That Username does not exist. Perhaps try creating an account?"
        if len(postData["loginPassword"]) < 8:
            errors["loginPassword"] = "Please enter a valid password."
        if not User.objects.filter(username=postData['loginUsername']):
            if not bcrypt.checkpw(postData['loginPassword'].encode(), User.objects.get(username=postData["loginUsername"]).password.encode()):
                errors['loginPassword'] = "That Username and password combo is incorrect. Please try again."
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=255)

    objects = UserManager()

    # When asked for a representation of itself what is returned
    def __repr__(self):
        return 'name: {}, username {}, password {}'.format(self.name, self.username, self.password)

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=25)

class Task(models.Model):
    status = models.CharField(max_length=12)
    creationDate = models.DateTimeField(auto_created=True, auto_now_add=True)
    editDate = models.DateTimeField(auto_created=True, auto_now=True)
    name = models.CharField(max_length=69)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    assignedTo = models.ManyToManyField(TeamMember, related_name='assigned')

    def __repr__(self):
        return 'name: {}, status: {}, creator: {}, assignedTo: {}, creationDate: {}, editDate: {}'.format(self.name, self.status, self.creator, self.assignedTo, self.creationDate, self.editDate)

