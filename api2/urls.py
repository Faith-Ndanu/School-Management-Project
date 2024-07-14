from django.urls import path
from .views import ClassPeriodListView


urlpatterns=[
    path("classperiods/",ClassPeriodListViewListView.as_view(),name="classperiods_list_view")
]