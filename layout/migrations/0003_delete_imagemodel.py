# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0002_auto_20151109_1947'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]