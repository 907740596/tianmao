# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-17 14:54
from __future__ import unicode_literals

import apps.home.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(storage=apps.home.models.ImageStorage(), upload_to='banner/%Y%m%d', verbose_name='轮播图')),
                ('detail_url', models.URLField(verbose_name='访问地址')),
                ('order', models.IntegerField(default=1, verbose_name='顺序')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False, verbose_name='分类ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '分类菜单',
                'verbose_name_plural': '菜单管理',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('nav_id', models.AutoField(primary_key=True, serialize=False)),
                ('nav_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'navigation',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('order_code', models.CharField(max_length=255, verbose_name='订单号')),
                ('address', models.CharField(max_length=255, verbose_name='配送地址')),
                ('post', models.CharField(max_length=255, verbose_name='邮编')),
                ('receiver', models.CharField(max_length=255, verbose_name='收货人')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('user_message', models.CharField(max_length=255, verbose_name='附加信息')),
                ('create_date', models.DateTimeField(max_length=0, verbose_name='创建日期')),
                ('pay_date', models.DateTimeField(blank=True, max_length=0, null=True, verbose_name='支付时间')),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='交易日期')),
                ('confirm_date', models.DateTimeField(blank=True, null=True, verbose_name='确认日期')),
                ('status', models.IntegerField(choices=[(1, '正常'), (0, '异常'), (-1, '删除')], default=1, verbose_name='订单状态')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单管理',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商品属性')),
                ('name', models.CharField(max_length=64, verbose_name='属性名称')),
                ('cate', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '商品属性',
                'verbose_name_plural': '商品属性',
                'db_table': 'property',
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('pro_value_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='属性值')),
                ('property', models.ForeignKey(db_column='property_id', on_delete=django.db.models.deletion.CASCADE, to='home.Property', verbose_name='属性ID')),
            ],
            options={
                'verbose_name': '商品属性值',
                'verbose_name_plural': '商品属性值',
                'db_table': 'property_value',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=4000, verbose_name='内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='商品ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('sub_title', models.CharField(max_length=255, verbose_name='商品标题')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='原价')),
                ('promote_price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='折扣价')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('cate', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category', verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品管理',
                'db_table': 'shop',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='商品数量')),
                ('status', models.IntegerField(default=1)),
                ('order', models.ForeignKey(db_column='oid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Order', verbose_name='商品ID')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Shop', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shop_car',
            },
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('shop_img_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=32, null=True, verbose_name='图片类型')),
                ('shop', models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Shop', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片管理',
                'db_table': 'shop_image',
            },
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('sub_menu_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='名称')),
                ('cate', models.ForeignKey(db_column='cate_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '一级菜单',
                'verbose_name_plural': '一级菜单管理',
                'db_table': 'sub_menu',
            },
        ),
        migrations.CreateModel(
            name='SubMenu2',
            fields=[
                ('sub_menu2_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('sub_menu', models.ForeignKey(db_column='sub_menu_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.SubMenu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '二级菜单',
                'verbose_name_plural': '二级菜单管理',
                'db_table': 'sub_menu2',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('phone', models.CharField(default='110', max_length=11)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('icon', models.ImageField(default='apps/static/img/default.png', upload_to='upload/img/%Y%m%d', verbose_name='头像')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='shopcar',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Shop', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='propertyvalue',
            name='shop',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='home.Shop', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.UserProfile', verbose_name='用户ID'),
        ),
    ]
