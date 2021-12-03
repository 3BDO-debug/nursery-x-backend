# Generated by Django 3.2.7 on 2021-10-07 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=350, verbose_name='Role')),
                ('cv', models.FileField(upload_to='staff_CVs', verbose_name='CV')),
                ('staff_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Staff account')),
            ],
            options={
                'verbose_name': 'Staff member',
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
