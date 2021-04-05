# Generated by Django 3.1.7 on 2021-04-04 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editDate', models.DateTimeField(auto_created=True, auto_now=True)),
                ('creationDate', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('status', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=69)),
                ('assignedTo', models.ManyToManyField(related_name='assigned', to='SCRUM.TeamMember')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to='SCRUM.user')),
            ],
        ),
    ]