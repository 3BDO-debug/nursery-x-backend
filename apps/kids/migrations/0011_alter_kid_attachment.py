# Generated by Django 3.2.5 on 2021-12-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0010_alter_kid_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='kids_attahcments', verbose_name='Attachment'),
        ),
    ]