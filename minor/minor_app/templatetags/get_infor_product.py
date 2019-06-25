from django.template import Library
from ..models import SubCategory, Category, Product_Order, Product

register = Library()


@register.filter
def get_product_id(product):
    return product['product_id']


@register.filter
def get_product_name(product):
    name = Product.objects.get(pk=get_product_id(product)).product_name
    return name


@register.filter
def get_product_price(product):
    product = Product.objects.get(pk=get_product_id(product))
    return product.price


@register.filter
def get_product_category(product):
    category = ""
    try:
        category_id = Product.objects.get(pk=get_product_id(product)).category_id
        category = Category.objects.get(p=category_id).category_name
    except Exception:
        pass
    return category


@register.filter
def get_product_sub_category(product):
    subcate = ""
    try:
        product = Product.objects.get(pk=get_product_id(product))
        subcate = product.category.subcategory_name
    except Exception:
        pass
    return subcate


@register.filter
def get_quantity(product):
    quantity = 0
    try:
        quantity = product['quantity']
    except Exception:
        pass
    return quantity


@register.filter
def get_product_discount(product):
    product = Product.objects.get(pk=get_product_id(product))
    return product.discount


@register.filter
def get_total_price(product):
    return (get_product_price(product) - (
                int(get_product_price(product)) * (get_product_discount(product) / 100))) * get_quantity(product)
