# Generated by Django 3.2.5 on 2021-11-18 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_classes', '0004_classpostcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityclass',
            old_name='class_member',
            new_name='class_members',
        ),
    ]