from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.utils import timezone
from .models import Customer, Category, Country, Product, Segment, State, Order, Ship, Product_Order
from .forms import ShipForm
# site-packages load
import logging

logging.basicConfig(level=logging.DEBUG)


def index(request):
    """
        Show all information
    """
    orders = Order.objects.all()

    context = {
        'orders': orders,
    }

    return render(request, 'minor_app/index.html', context=context)


def product(request):
    add_product_success = False
    message = ""
    if request.method == 'POST':
        try:
            id = request.POST['id']
            name = request.POST['name']
            discount = request.POST['discount']
            price = request.POST['price']
            category = request.POST['sub_cate']
            Product.objects.create(
                product_id=id,
                product_name=name,
                price=price,
                discount=discount,
                category_id=category,
            )
            add_product_success = True
        except IntegrityError:
            message = "Mã sản phẩm đã có trong cơ sở dữ liệu"
        except Exception as error:
            logging.debug("{error}".format(error=error))

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'add_product_success': add_product_success,
        'message': message,
    }
    return render(request, 'minor_app/product.html', context=context)


def load_sub_categories(request):
    cate_id = request.POST['category_id']
    sub_categories = Category.objects.get(pk=cate_id).subcategory_set.all()
    context = {
        'sub_categories': sub_categories,
    }
    return render(request, 'minor_app/load-sub-categories.html', context=context)


def order(request):
    """
        user id duoc tinh khi client gui request bang ajax VN-thoigianhientaicuahethong

    """

    products = Product.objects.all()

    segments = Segment.objects.all()

    context = {
        'products': products,
        'segments': segments,
    }
    return render(request, 'minor_app/order.html', context=context)


def ordered(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        number_phone = request.POST['number_phone']
        country_pk = request.POST['country_pk']
        state_id = request.POST['state_id']
        city_id = request.POST['city_id']
        segment_id = request.POST['segment_id']

        customer_id = country_pk + str(int(timezone.now().timestamp() * 1000000))
        Customer.objects.create(
            customer_id=customer_id,
            customer_name=customer_name,
            city_id=city_id,
            state_id=state_id,
            country=Country.objects.get(pk=country_pk),
            segment_id=segment_id,
            number_phone=number_phone,
        )

        ship_mode = request.POST['ship_mode']
        ship_date = request.POST['ship_date']
        year = int(ship_date.split('/')[2])
        month = int(ship_date.split('/')[1])
        day = int(ship_date.split('/')[0])
        ship_date = timezone.datetime(year, month, day)
        ship = Ship.objects.create(
            ship_date=ship_date,
            ship_mode=ship_mode
        )

        order = Order.objects.create(
            customer=Customer.objects.get(pk=customer_id),
            ship=ship,
        )

        product_id = request.POST['product_id']

        order.product.set(Product.objects.filter(pk=product_id))

        quantity = request.POST['quantity']

        Product_Order.objects.create(
            order=order,
            product_id=product_id,
            quantity=quantity
        )

    return HttpResponseRedirect(reverse_lazy('minor_app:order'))


def cart(request):
    ship_form = ShipForm()
    countries = Country.objects.all()
    context = {
        'countries': countries,
        'ship_form': ship_form,
    }
    return render(request, 'minor_app/cart.html', context=context)


def load_states(request):
    country_pk = request.GET['country_pk']
    states = State.objects.filter(country_id=country_pk)
    data = {
        'length': len(states),
        'result': (
            list(states.values('id', 'state_name'))
        )
    }
    return JsonResponse(data=data)


def load_cities(request):
    state_id = request.GET['state_id']
    cities = get_object_or_404(State, pk=state_id).city_set.all()
    data = {
        'cities': (
            list(cities.values('id', 'city_name'))
        )
    }
    return JsonResponse(data=data)


def load_delivery_date(request):
    ship_mode = request.GET['ship_mode']
    today = timezone.now().date()
    # mac dinh same day
    timedelta = timezone.timedelta(0)
    if ship_mode == 'Second class':
        timedelta = timezone.timedelta(4)
    elif ship_mode == 'Standard class':
        timedelta = timezone.timedelta(5)
    elif ship_mode == 'First Class':
        timedelta = timezone.timedelta(3)

    ship_date = today + timedelta
    delivery_date = str(ship_date.day) + '/' + str(ship_date.month) + '/' + str(ship_date.year)

    data = {
        'delivery_date': delivery_date
    }

    return JsonResponse(data=data)
