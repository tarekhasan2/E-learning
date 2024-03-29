# Generated by Django 2.1.7 on 2019-05-03 13:52

import courses.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=courses.models.uploded_location)),
                ('publish', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=courses.models.uploded_location)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
