from django.conf.urls import url
from . import views
from .views import ItemListView, DeleteItem, ItemUpdateView, LoginView, NoticeView, DemandView

app_name = "shop"
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^services$', views.services, name = "services"),
    url(r'^Demand$', views.DemandView, name = "demand"),
    url(r'^search', views.search, name = "search"),
    url(r'^about$', views.about, name = "about"),
    url(r'^enquiry$', views.enquiry, name = "enquiry"),
    url(r'^contact$', views.contact, name = "contact"),
    url(r'^download-demand$', views.DemandDownloadView, name = "demand_download"),
    url(r'^Thank-You', views.ThankYou, name = "thank_you"),
    url(r'^inventorymanagement', views.inventorymanagement, name = "inventorymanagement"),
    url(r'^Notice', NoticeView.as_view(), name = "notice"),
    url(r'^InventoryDetail', ItemListView.as_view(), name = "ItemList"),
    url(r'^accounts/login', LoginView.as_view(), name = "login"),
    url(r'^accounts/logout', views.Logoutview, name = "logout"),
    url(r'^Delete/(?P<pk>.*)', DeleteItem.as_view(), name = "delete"),
    url(r'^Update/(?P<pk>.*)', ItemUpdateView.as_view(), name = "update"),
]