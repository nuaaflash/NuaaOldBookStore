# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0012_remove_book_book_storage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_storage',
            field=models.IntegerField(default=212, verbose_name='\u5e93\u5b58'),
            preserve_default=False,
        ),
    ]
