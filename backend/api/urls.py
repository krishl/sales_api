from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCustomerView, CustomerDetailsView, CreateProductView, ProductDetailsView

urlpatterns = {
    url(r'^customers/$', CreateCustomerView.as_view(), name="custCreate"),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetailsView.as_view(), name="custDetails"),
    url(r'^products/$', CreateProductView.as_view(), name="prodCreate"),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailsView.as_view(), name="prodDetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)