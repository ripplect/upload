# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUserOpinions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('opinionOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempUserQueries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('queryOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tempuseropinions',
            name='questionOfOpinion',
            field=models.ForeignKey(to='data.TempUserQueries'),
        ),
    ]
