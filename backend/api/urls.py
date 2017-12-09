from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateCustomerView, CustomerDetailsView

urlpatterns = {
    url(r'^customers/$', CreateCustomerView.as_view(), name="custCreate"),
    url(r'^customers/(?P<pk>[0-9]+)/$', CustomerDetailsView.as_view(), name="custDetails"),
}

urlpatterns = format_suffix_patterns(urlpatterns)