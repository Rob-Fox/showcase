from __future__ import unicode_literals
from django.db import models
from login_reg.models import User as User


# class TeamMember(models.Model):
#     name = models.CharField(max_length=255)
#     username = models.CharField(max_length=25)

#     def __repr__(self):
#         return 'name: {}, username: {}'.format(self.name, self.username)

class Project(models.Model):
    creationDate = models.DateTimeField(auto_created=True, auto_now_add=True)
    name = models.CharField(max_length=255)
    head = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leading")
    members = models.ManyToManyField(User, related_name="projects")
    status = models.BooleanField(default=False)

    def __repr__(self):
        return 'name: {}, status: {}, head: {}, members: {}, creationDate: {}'.format(self.name, self.status, self.head, self.members, self.creationDate)

class Task(models.Model):
    status = models.CharField(max_length=12)
    creationDate = models.DateTimeField(auto_created=True, auto_now_add=True)
    editDate = models.DateTimeField(auto_created=True, auto_now=True)
    name = models.CharField(max_length=69)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    assignedTo = models.ManyToManyField(User, related_name='assigned')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return 'name: {}, status: {}, creator: {}, assignedTo: {}, creationDate: {}, editDate: {}'.format(self.name, self.status, self.creator, self.assignedTo, self.creationDate, self.editDate)
