from django.db import models


class Segment(models.Model):
    """
        Create a segment table contain type of customer
    """
    segment_name = models.CharField(max_length=10, verbose_name='Tên phân khúc')

    class Meta:
        verbose_name = "Phân khúc"
        verbose_name_plural = "Phân khúc"

    def __str__(self):
        return self.segment_name


class Customer(models.Model):
    """
        Create a customer table in a database
    """
    customer_id = models.CharField(max_length=50, verbose_name='Mã khách hàng', default="EXAMPLE_ID", primary_key=True)
    city = models.ForeignKey('City', verbose_name='Thành phố (Quận)', null=True, on_delete=models.CASCADE)
    state = models.ForeignKey('State', verbose_name='Tiểu bang(Thành phố)', null=True, on_delete=models.CASCADE)
    country = models.ForeignKey('Country', verbose_name='Quốc gia', null=True, on_delete=models.CASCADE)
    segment = models.ForeignKey(Segment, verbose_name='Tên phân khúc', on_delete=models.CASCADE)
    customer_name = models.CharField(verbose_name='Tên khách hàng', max_length=50)
    number_phone = models.CharField(verbose_name='Số điện thoại', max_length=15, default='0')

    class Meta:
        verbose_name = "Khách hàng"
        verbose_name_plural = "Khách hàng"

    def __str__(self):
        return self.customer_name


class City(models.Model):
    """
        Create a city table
    """
    state = models.ForeignKey('State', null=True, verbose_name='Tiểu bang(Thành phố )', on_delete=models.CASCADE)
    city_code = models.BigIntegerField(null=False, verbose_name='Mã thành phố (Quận)', )
    city_name = models.CharField(max_length=100, null=False, verbose_name='Tên thành phố (Quận)', )

    region_list = [
        ('W', 'WEST'),
        ('E', 'EAST'),
        ('S', 'SOUTH'),
        ('N', 'NORTH'),
        ('CE', 'CENTRAL')
    ]

    region = models.CharField(
        max_length=2,
        choices=region_list,
        default='CE',
        verbose_name='Vùng'
    )

    class Meta:
        verbose_name = "Thành phố (Quận)"
        verbose_name_plural = "Thành phố (Quận)"

    def __str__(self):
        return self.city_name


class State(models.Model):
    """
        Create a state table
    """
    country = models.ForeignKey('Country', verbose_name='Quốc gia', null=True, on_delete=models.CASCADE)
    state_code = models.BigIntegerField(verbose_name='Mã tiểu bang(Thành phố)', null=False, default=00000)
    state_name = models.CharField(verbose_name='Tên tiểu bang(Thành phố)', max_length=100, null=False,
                                  default="state name")

    class Meta:
        verbose_name = "Tiểu bang(Thành phố )"
        verbose_name_plural = "Tiểu bang(Thành phố )"

    def __str__(self):
        return self.state_name


class Country(models.Model):
    """
        Create a table which contain all country name
    """
    country_code = models.CharField(max_length=10, verbose_name='Mã quốc gia', primary_key=True)
    country_name = models.CharField(max_length=75, verbose_name='Tên quốc gia')

    class Meta:
        verbose_name = "Quốc gia"
        verbose_name_plural = 'Quốc gia'
        ordering = ['country_name']

    def __str__(self):
        return self.country_name


class Ship(models.Model):
    """
        Create ship table
    """
    ship_date = models.DateField(verbose_name='Ngày vận chuyển')

    mode = (
        ('Second class', 'Second class'),
        ('Standard class', 'Standard class'),
        ('First Class', 'First Class'),
        ('Same day', 'Same day'),
    )

    ship_mode = models.CharField(max_length=20, verbose_name='Phương thức vận chuyển', choices=mode)

    class Meta:
        verbose_name = 'Vận chuyển'
        verbose_name_plural = 'Vận chuyển'

    def __str__(self):
        return str(self.ship_date)


class Order(models.Model):
    """
        Create a order table
    """
    product = models.ManyToManyField('Product', verbose_name='Sản phẩm', related_name='orders')
    customer = models.ForeignKey(Customer, verbose_name='Khách hàng', null=True, on_delete=models.CASCADE)
    ship = models.OneToOneField(Ship, verbose_name='Vận chuyển', on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True, verbose_name='Ngày đặt hàng')

    class Meta:
        verbose_name = 'Đơn hàng'
        verbose_name_plural = 'Đơn hàng'

    def __str__(self):
        return str(self.order_date)


class Product(models.Model):
    """
        Create a product table
    """
    product_id = models.CharField(max_length=20, primary_key=True, verbose_name='ID Sản phẩm')
    product_name = models.CharField(max_length=250, verbose_name='Tên sản phẩm')
    price = models.FloatField(verbose_name='Giá')
    discount = models.FloatField(default=0, verbose_name="Giảm giá(%)")
    category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, verbose_name='Loại sản phẩm')

    class Meta:
        verbose_name = 'Sản phẩm'
        verbose_name_plural = 'Sản phẩm'
        ordering = ["product_id"]

    def __str__(self):
        return self.product_name


class Product_Order(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='Số lượng', default=0)

    def __str__(self):
        return self.product.product_name
        return self.product.product_name


class Category(models.Model):
    """
        Create a category table
    """
    category_name = models.CharField(max_length=50, verbose_name='Tên danh mục')

    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    """
        Create a category table
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Danh mục')
    subcategory_name = models.CharField(max_length=50, verbose_name='Loại sản phẩm')

    class Meta:
        verbose_name = 'Loại sản phẩm'
        verbose_name_plural = 'Loại sản phẩm'

    def __str__(self):
        return self.subcategory_name
