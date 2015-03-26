# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ThisGame', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='period',
            old_name='classes',
            new_name='claz',
        ),
    ]
