from django.urls import path
from .views import article_list, article_detail,locality_list,locality_detail

urlpatterns = [

    path('article/', article_list),
    path('detail/<int:pk>', article_detail),
    path('locality/', locality_list),
    path('locality/<int:pk>', locality_detail),


]