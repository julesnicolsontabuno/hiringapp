# Generated by Django 3.1.14 on 2022-10-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_team_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestteam',
            name='status',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
