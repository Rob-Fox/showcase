from __future__ import unicode_literals
from django.db import models
from login_reg.models import User as User


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=25)

    def __repr__(self):
        return 'name: {}, username: {}'.format(self.name, self.username)

class Task(models.Model):
    status = models.CharField(max_length=12)
    creationDate = models.DateTimeField(auto_created=True, auto_now_add=True)
    editDate = models.DateTimeField(auto_created=True, auto_now=True)
    name = models.CharField(max_length=69)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    assignedTo = models.ManyToManyField(TeamMember, related_name='assigned')

    def __repr__(self):
        return 'name: {}, status: {}, creator: {}, assignedTo: {}, creationDate: {}, editDate: {}'.format(self.name, self.status, self.creator, self.assignedTo, self.creationDate, self.editDate)
