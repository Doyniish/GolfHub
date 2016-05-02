# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainWebsite', '0002_remove_golfevent_group'),
        ('Users', '0004_auto_20160427_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackNine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole_scores', models.CharField(max_length=1000)),
                ('hole_putts', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='FrontNine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole_scores', models.CharField(max_length=1000)),
                ('hole_putts', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('back_nine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.BackNine')),
                ('front_nine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.FrontNine')),
            ],
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.ManyToManyField(to='Users.Round')),
            ],
        ),
        migrations.AddField(
            model_name='userdata',
            name='events',
            field=models.ManyToManyField(to='MainWebsite.GolfEvent'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='stats',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.UserStats'),
            preserve_default=False,
        ),
    ]