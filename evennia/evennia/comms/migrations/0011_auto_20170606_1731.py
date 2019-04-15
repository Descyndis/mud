# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 17:31


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comms', '0010_auto_20161206_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channeldb',
            name='db_attributes',
            field=models.ManyToManyField(help_text='attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).', to='typeclasses.Attribute'),
        ),
        migrations.AlterField(
            model_name='channeldb',
            name='db_object_subscriptions',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='object_subscription_set', to='objects.ObjectDB', verbose_name='subscriptions'),
        ),
        migrations.AlterField(
            model_name='channeldb',
            name='db_subscriptions',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='subscription_set', to=settings.AUTH_USER_MODEL, verbose_name='subscriptions'),
        ),
        migrations.AlterField(
            model_name='channeldb',
            name='db_tags',
            field=models.ManyToManyField(help_text='tags on this object. Tags are simple string markers to identify, group and alias objects.', to='typeclasses.Tag'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_hide_from_channels',
            field=models.ManyToManyField(blank=True, related_name='hide_from_channels_set', to='comms.ChannelDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_hide_from_objects',
            field=models.ManyToManyField(blank=True, related_name='hide_from_objects_set', to='objects.ObjectDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_hide_from_accounts',
            field=models.ManyToManyField(blank=True, related_name='hide_from_accounts_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_receivers_channels',
            field=models.ManyToManyField(blank=True, help_text='channel recievers', related_name='channel_set', to='comms.ChannelDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_receivers_objects',
            field=models.ManyToManyField(blank=True, help_text='object receivers', related_name='receiver_object_set', to='objects.ObjectDB'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_receivers_accounts',
            field=models.ManyToManyField(blank=True, help_text='account receivers', related_name='receiver_account_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_sender_objects',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='sender_object_set', to='objects.ObjectDB', verbose_name='sender(object)'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_sender_accounts',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='sender_account_set', to=settings.AUTH_USER_MODEL, verbose_name='sender(account)'),
        ),
        migrations.AlterField(
            model_name='msg',
            name='db_tags',
            field=models.ManyToManyField(blank=True, help_text='tags on this message. Tags are simple string markers to identify, group and alias messages.', to='typeclasses.Tag'),
        ),
    ]