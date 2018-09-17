from __future__ import unicode_literals

from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'

class Banner(models.Model):
    banner_id = models.AutoField('页头ID',primary_key=True)
    title = models.CharField('标题',max_length=100)
    image = models.CharField('图片路径',max_length=100)
    detail_url = models.CharField('图片地址',max_length=200)
    order = models.IntegerField('排序')
    create_time = models.DateTimeField('创建时间',blank=True, null=True)

    class Meta:
        db_table = 'banner'
        verbose_name = '页头'
        verbose_name_plural = verbose_name


class Category(models.Model):
    cate_id = models.AutoField('类别',primary_key=True)
    name = models.CharField('类别名称',max_length=255)

    class Meta:
        db_table = 'category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class Navigation(models.Model):
    nav_id = models.AutoField('导航栏ID',primary_key=True)
    nav_name = models.CharField('导航栏名称',max_length=64)

    class Meta:
        db_table = 'navigation'
        verbose_name = '导航栏'
        verbose_name_plural = verbose_name


class Order(models.Model):
    oid = models.AutoField('订单ID',primary_key=True)
    order_code = models.CharField('订单码',max_length=255)
    address = models.CharField('收货地址',max_length=255)
    post = models.CharField('邮编',max_length=255)
    receiver = models.CharField('收货人',max_length=255)
    mobile = models.CharField('电话',max_length=11)
    user_message = models.CharField('用户备注',max_length=255)
    create_date = models.DateTimeField('创建时间',blank=True, null=True)
    pay_date = models.DateTimeField('支付时间',blank=True, null=True)
    delivery_date = models.DateTimeField('派送时间',blank=True, null=True)
    confirm_date = models.DateTimeField('确认收货时间',blank=True, null=True)
    status = models.IntegerField('订单状态')
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        db_table = 'order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class Property(models.Model):
    property_id = models.AutoField('属性ID',primary_key=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    name = models.CharField('属性名',max_length=64)

    class Meta:
        db_table = 'property'
        verbose_name = '属性'
        verbose_name_plural = verbose_name

class PropertyValue(models.Model):
    pro_value_id = models.AutoField('属性值ID',primary_key=True)
    property_id = models.IntegerField('属性ID')
    shop_id = models.IntegerField('商品ID')
    value = models.CharField('属性值',max_length=255)

    class Meta:
        db_table = 'property_value'
        verbose_name = '属性值'
        verbose_name_plural = verbose_name




class Review(models.Model):
    review_id = models.AutoField('评价ID',primary_key=True)
    content = models.CharField('评价内容',max_length=4000)
    create_date = models.DateTimeField('创建时间',blank=True, null=True)
    shop = models.ForeignKey('Shop', models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')

    class Meta:
        db_table = 'review'
        verbose_name = '评价'
        verbose_name_plural = verbose_name


class Shop(models.Model):
    shop_id = models.IntegerField('商品ID',primary_key=True)
    name = models.CharField('商品名称',max_length=100)
    sub_title = models.CharField('sub标题',max_length=255)
    original_price = models.DecimalField('原价',max_digits=7, decimal_places=2)
    promote_price = models.DecimalField('折扣价',max_digits=7, decimal_places=2)
    stock = models.IntegerField('库存')
    cate = models.ForeignKey(Category, models.DO_NOTHING)
    create_date = models.DateTimeField('创建时间',blank=True, null=True)

    class Meta:
        db_table = 'shop'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class ShopCar(models.Model):
    car_id = models.AutoField('购物车ID',primary_key=True)
    number = models.IntegerField('数量')
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid')
    oid = models.IntegerField('订单ID',blank=True, null=True)
    status = models.IntegerField('购物车状态')

    class Meta:
        db_table = 'shop_car'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


class ShopImage(models.Model):
    shop_img_id = models.AutoField('商品图片ID',primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    type = models.CharField('类型',max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'shop_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class SubMenu(models.Model):
    sub_menu_id = models.AutoField('sub菜单',primary_key=True)
    name = models.CharField('sub菜单名称',max_length=255, blank=True, null=True)
    cate = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        db_table = 'sub_menu'
        verbose_name = 'sub菜单'
        verbose_name_plural = verbose_name


class SubMenu2(models.Model):
    sub_menu2_id = models.AutoField('sub菜单2ID',primary_key=True)
    name = models.CharField('sub菜单2名称',max_length=255)
    sub_menu = models.ForeignKey(SubMenu, models.DO_NOTHING)

    class Meta:
        db_table = 'sub_menu2'
        verbose_name = 'sub菜单2'
        verbose_name_plural = verbose_name


class UserProfile(models.Model):
    uid = models.AutoField('用户ID',primary_key=True)
    icon = models.CharField('图标',max_length=100)
    phone = models.CharField('电话',max_length=11)
    desc = models.CharField('简介',max_length=255, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户配置'
        verbose_name_plural = verbose_name



