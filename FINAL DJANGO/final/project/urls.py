from django.urls import path
from project import views
from django.conf.urls import url


urlpatterns = [
url(r'^$', views.IcList.as_view(), name='ic_list'),
url(r'^new$', views.IcCreate.as_view(), name='ic_new'),
url(r'^edit/(?P<pk>\d+)$', views.IcUpdate.as_view(), name='ic_edit'),
url(r'^delete/(?P<pk>\d+)$', views.IcDelete.as_view(), name='ic_delete'),
]