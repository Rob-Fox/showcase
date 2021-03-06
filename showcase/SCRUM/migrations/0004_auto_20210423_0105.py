# Generated by Django 3.2 on 2021-04-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('SCRUM', '0003_auto_20210421_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leading', to='login_reg.user')),
                ('members', models.ManyToManyField(related_name='projects', to='login_reg.User')),
            ],
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.AlterField(
            model_name='task',
            name='assignedTo',
            field=models.ManyToManyField(related_name='assigned', to='login_reg.User'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SCRUM.project'),
        ),
    ]
