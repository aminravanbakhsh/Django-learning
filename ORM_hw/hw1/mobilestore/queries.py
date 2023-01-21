from .models import Brand, Mobile


def list_all_brands():
    query = Brand.objects.all()
    return query


def list_all_mobiles():
    query = Mobile.objects.all()
    return query


def price_of_mobile_with_model(model_name):
    query = Mobile.objects.get(model=model_name).price
    return query


def most_expensive_mobile():
    query = Mobile.objects.order_by('-price')[0]
    return query


def all_mobiles_with_brand_of(brand_name):
    query = Mobile.objects.filter(brand__name=brand_name)
    return query


def all_available_mobiles_with_price_in_range(min_price, max_price):
    query = Mobile.objects.filter(price__gte=min_price).filter(price__lte=max_price).count()
    return query


"""
from mobilestore.queries import *
from mobilestore.models import *
53060000
60000000
600000000
600000000
83123431, 53060000
all_available_mobiles_with_price_in_range(53060000, 83123431)
Mobile.objects.filter(price__lte=max_price).filter(price__gte=min_price).count()
"""

