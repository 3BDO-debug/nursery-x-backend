# Generated by Django 3.2.7 on 2021-10-07 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0002_auto_20211008_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=350, verbose_name='Age')),
                ('hobbies', models.CharField(max_length=350, null=True, verbose_name='Hobbies')),
                ('health_status', models.TextField(verbose_name='Health status')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='kids_attahcments', verbose_name='Attachment')),
                ('parent_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.parent', verbose_name='Parent account')),
            ],
        ),
    ]
