# Generated by Django 3.2.5 on 2021-11-18 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0005_kid_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kid',
            options={'verbose_name': 'Kid', 'verbose_name_plural': 'Kids'},
        ),
        migrations.AddField(
            model_name='kid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 18, 7, 41, 38, 953974, tzinfo=utc), verbose_name='Created at'),
            preserve_default=False,
        ),
    ]
