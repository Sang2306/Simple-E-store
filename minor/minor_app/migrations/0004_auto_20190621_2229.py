# Generated by Django 2.2.2 on 2019-06-21 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minor_app', '0003_auto_20190620_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Danh mục', 'verbose_name_plural': 'Danh mục'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Thành phố (Quận)', 'verbose_name_plural': 'Thành phố (Quận)'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['country_name'], 'verbose_name': 'Quốc gia', 'verbose_name_plural': 'Quốc gia'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Khách hàng', 'verbose_name_plural': 'Khách hàng'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Đơn hàng', 'verbose_name_plural': 'Đơn hàng'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_id'], 'verbose_name': 'Sản phẩm', 'verbose_name_plural': 'Sản phẩm'},
        ),
        migrations.AlterModelOptions(
            name='segment',
            options={'verbose_name': 'Phân khúc', 'verbose_name_plural': 'Phân khúc'},
        ),
        migrations.AlterModelOptions(
            name='ship',
            options={'verbose_name': 'Vận chuyển', 'verbose_name_plural': 'Vận chuyển'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'Tiểu bang(Thành phố )', 'verbose_name_plural': 'Tiểu bang(Thành phố )'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Loại sản phẩm', 'verbose_name_plural': 'Loại sản phẩm'},
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.SmallIntegerField(default=0, verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='Tên danh mục'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_code',
            field=models.BigIntegerField(verbose_name='Mã thành phố (Quận)'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=100, verbose_name='Tên thành phố (Quận)'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.CharField(choices=[('W', 'WEST'), ('E', 'EAST'), ('S', 'SOUTH'), ('N', 'NORTH'), ('CE', 'CENTRAL')], default='CE', max_length=2, verbose_name='Vùng'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.State', verbose_name='Tiểu bang(Thành phố )'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Mã quốc gia'),
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=75, verbose_name='Tên quốc gia'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.City', verbose_name='Thành phố (Quận)'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.Country', verbose_name='Quốc gia'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='EXAMPLE_ID', max_length=50, primary_key=True, serialize=False, verbose_name='Mã khách hàng'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(max_length=50, verbose_name='Tên khách hàng'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minor_app.Segment', verbose_name='Tên phân khúc'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.State', verbose_name='Tiểu bang(Thành phố)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.Customer', verbose_name='Khách hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now=True, verbose_name='Ngày đặt hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='minor_app.Product', verbose_name='Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ship',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='minor_app.Ship', verbose_name='Vận chuyển'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minor_app.SubCategory', verbose_name='Loại sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Giảm giá(%)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Giá'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=250, verbose_name='Tên sản phẩm'),
        ),
        migrations.AlterField(
            model_name='segment',
            name='segment_name',
            field=models.CharField(max_length=10, verbose_name='Tên phân khúc'),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_date',
            field=models.DateField(verbose_name='Ngày vận chuyển'),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_mode',
            field=models.CharField(choices=[('SeC', 'Second class'), ('StdC', 'Standard class'), ('FC', 'First Class'), ('Same', 'Same day')], max_length=8, verbose_name='Ohương thức vận chuyển'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='minor_app.Country', verbose_name='Quốc gia'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_code',
            field=models.BigIntegerField(default=0, verbose_name='Mã tiểu bang(Thành phố)'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_name',
            field=models.CharField(default='state name', max_length=100, verbose_name='Tên tiểu bang(Thành phố)'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minor_app.Category', verbose_name='Danh mục'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_name',
            field=models.CharField(max_length=50, verbose_name='Loại sản phẩm'),
        ),
    ]
