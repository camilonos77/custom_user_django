# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustom',
            name='fecha_creacion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
