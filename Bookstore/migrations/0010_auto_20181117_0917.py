# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0009_book_cover_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '\u5e10\u6237'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '\u4e66\u7c4d'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date'], 'verbose_name': '\u8ba2\u5355'},
        ),
        migrations.AlterModelOptions(
            name='orderbookrelation',
            options={'verbose_name': '\u8ba2\u5355&\u4e66\u7c4d\u5173\u7cfb'},
        ),
        migrations.AlterModelOptions(
            name='shopcart',
            options={'verbose_name': '\u8d2d\u7269\u8f66'},
        ),
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.TextField(verbose_name='\u5730\u5740'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='comments',
            field=models.ManyToManyField(related_name='comments_on_this_book', verbose_name='\u8bc4\u8bba', through='Bookstore.Comment', to='Bookstore.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='recommend_books',
            field=models.ManyToManyField(related_name='accounts_should_recommend_this_book', verbose_name='\u63a8\u8350\u4e66\u7c4d', to='Bookstore.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='shop_cart',
            field=models.ManyToManyField(to='Bookstore.Book', verbose_name='\u8d2d\u7269\u8f66', through='Bookstore.ShopCart'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.CharField(max_length=100, verbose_name='\u5c01\u9762\u56fe\u7247'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='\u7b80\u4ecb'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=200, verbose_name='\u8bed\u8a00'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=2000, verbose_name='\u4e66\u540d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='page_number',
            field=models.IntegerField(verbose_name='\u9875\u6570'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(verbose_name='\u4ef7\u683c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(verbose_name='\u51fa\u7248\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=1000, verbose_name='\u51fa\u7248\u5546'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='related_books',
            field=models.ManyToManyField(related_name='related_books_rel_+', null=True, verbose_name='\u76f8\u5173\u4e66\u7c4d', to='Bookstore.Book', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='aid',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='bid',
            field=models.ForeignKey(verbose_name='\u4e66\u7c4d', to='Bookstore.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=2000, verbose_name='\u8bc4\u8bba\u5185\u5bb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(verbose_name='\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='aid',
            field=models.ForeignKey(verbose_name='\u8ba2\u5355\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(to='Bookstore.Book', verbose_name='\u4e66\u7c4d', through='Bookstore.OrderBookRelation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='\u65e5\u671f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=20, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(b'u', '\u672a\u5b8c\u6210'), (b'p', '\u6b63\u5728\u8fdb\u884c'), (b'c', '\u5df2\u5b8c\u6210')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderbookrelation',
            name='bid',
            field=models.ForeignKey(verbose_name='\u4e66\u7c4d', to='Bookstore.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderbookrelation',
            name='number_of_book',
            field=models.IntegerField(verbose_name='\u6570\u91cf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderbookrelation',
            name='oid',
            field=models.ForeignKey(verbose_name='\u8ba2\u5355', to='Bookstore.Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='aid',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='bid',
            field=models.ForeignKey(verbose_name='\u4e66\u7c4d', to='Bookstore.Book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='number_of_book',
            field=models.IntegerField(verbose_name='\u6570\u91cf'),
            preserve_default=True,
        ),
    ]
