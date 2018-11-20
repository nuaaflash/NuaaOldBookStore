# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0011_book_book_storage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_storage',
        ),
    ]
