# Generated by Django 3.2.5 on 2021-11-15 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_body', models.TextField(blank=True, null=True, verbose_name='Post body')),
                ('post_attachment', models.FileField(blank=True, null=True, upload_to='class_posts_attachments', verbose_name='Post attachment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('activity_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_classes.activityclass', verbose_name='Activity class')),
            ],
            options={
                'verbose_name': 'Class post',
                'verbose_name_plural': 'Class posts',
            },
        ),
    ]
