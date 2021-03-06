# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-30 20:56
from __future__ import unicode_literals

from copy import deepcopy
from base64 import b64encode, b64decode
from django.db import migrations
from pickle import dumps, loads
from evennia.utils.utils import to_bytes


def forwards(apps, schema_editor):
    Attribute = apps.get_model('typeclasses', 'Attribute')
    for attr in Attribute.objects.all():
        # we need to re-assign the Attribute it's own value to make sure pickle switches from v2 to v4,
        # otherwise we will not be able to search db by-value.
        attr.db_value = attr.db_value
        attr.save(update_fields=["db_value"])


class Migration(migrations.Migration):

    dependencies = [
        ('typeclasses', '0011_auto_20190128_1820'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
