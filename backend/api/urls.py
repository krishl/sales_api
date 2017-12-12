from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCustomerView, CustomerDetailsView, CreateProductView, ProductDetailsView, CreateCartView, CartDetailsView, CustomerCartView

urlpatterns = {
    url(r'^customers/$', CreateCustomerView.as_view(), name="custCreate"),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetailsView.as_view(), name="custDetails"),
    url(r'^customers/(?P<pk>[0-9]+)/cart/$', CustomerCartView.as_view(), name="custCart"),
    url(r'^products/$', CreateProductView.as_view(), name="prodCreate"),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailsView.as_view(), name="prodDetails"),
    url(r'^carts/$', CreateCartView.as_view(), name="cartCreate"),
    url(r'^carts/(?P<pk>[0-9]+)/$', CartDetailsView.as_view(), name="cartDetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)