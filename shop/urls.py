from django.conf.urls import url
from . import views
from .views import ItemListView, DeleteItem, ItemUpdateView, LoginView, NoticeView

app_name = "shop"
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^services$', views.services, name = "services"),
    url(r'^demand$', views.demand_view, name = "demand"),
    url(r'^search', views.search, name = "search"),
    url(r'^about$', views.about, name = "about"),
    url(r'^enquiry$', views.enquiry, name = "enquiry"),
    url(r'^contact$', views.contact, name = "contact"),
    url(r'^download_demand$', views.demand_download_view, name = "demand_download"),
    url(r'^thank_you', views.thank_you, name = "thank_you"),
    url(r'^accounts/logout', views.logout_view, name = "logout"),
    url(r'^inventory_management', views.inventory_management, name = "inventory_management"),
    url(r'^notice', NoticeView.as_view(), name = "notice"),
    url(r'^inventory_detail', ItemListView.as_view(), name = "item_list"),
    url(r'^accounts/login', LoginView.as_view(), name = "login"),
    url(r'^delete/(?P<pk>.*)', DeleteItem.as_view(), name = "delete"),
    url(r'^update/(?P<pk>.*)', ItemUpdateView.as_view(), name = "update"),
]