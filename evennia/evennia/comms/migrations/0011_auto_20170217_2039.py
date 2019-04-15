# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-17 20:39


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0007_auto_20150403_2339'),
        ('comms', '0010_auto_20161206_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='db_receivers_scripts',
            field=models.ManyToManyField(blank=True, help_text='script_receivers', null=True, related_name='receiver_script_set', to='scripts.ScriptDB'),
        ),
        migrations.AddField(
            model_name='msg',
            name='db_sender_scripts',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, related_name='sender_script_set', to='scripts.ScriptDB', verbose_name='sender(script)'),
        ),
    ]