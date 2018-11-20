# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0010_auto_20181117_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_storage',
            field=models.IntegerField(default=123321, verbose_name='\u5e93\u5b58'),
            preserve_default=False,
        ),
    ]
