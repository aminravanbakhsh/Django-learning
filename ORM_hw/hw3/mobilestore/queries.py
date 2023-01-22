from .models import Brand, Mobile
from django.db.models import F, Q

def all_brands_not_in_korea_china():
    query = Brand.objects.filter(~Q(nationality="China") & ~Q(nationality="Korea"))
    return query

def some_brand_mobiles(*brand_names):
    query = []
    if len(brand_names) == 0:
        query = Mobile.objects.all()
    else:
        query = Mobile.objects.filter(brand__name__in=brand_names)
    return query

def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality__exact=F('made_in'))
    return query