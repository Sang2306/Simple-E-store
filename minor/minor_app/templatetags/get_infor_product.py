from django.template import Library
from ..models import SubCategory, Category, Product_Order

register = Library()


@register.filter
def get_product_id(product):
    return product['product_id']


@register.filter
def get_product_name(product):
    return product['product_name']


@register.filter
def get_product_price(product):
    return product['price']


@register.filter
def get_product_category(product):
    category = ""
    try:
        category = Category.objects.get(pk=product['category_id'])
    except Exception:
        pass
    return category


@register.filter
def get_product_sub_category(product):
    subcate = ""
    try:
        subcate = SubCategory.objects.get(pk=product['category_id'])
    except Exception:
        pass
    return subcate


@register.filter
def get_quantity(product, order_id):
    quantity = 0
    try:
        product_id = product['product_id']
        quantity = Product_Order.objects.filter(order_id=order_id).get(product_id=product_id).quantity
    except Exception:
        pass
    return quantity


@register.filter
def get_product_discount(product):
    return product['discount']


@register.filter
def get_total_price(product, order_id):
    return (get_product_price(product) - (
                get_product_price(product) * (get_product_discount(product) / 100))) * get_quantity(product, order_id)
