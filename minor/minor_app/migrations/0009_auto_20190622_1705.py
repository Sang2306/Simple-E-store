# Generated by Django 2.2.2 on 2019-06-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor_app', '0008_auto_20190622_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='orders', to='minor_app.Product', verbose_name='Sản phẩm'),
        ),
    ]
