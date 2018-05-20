from django.urls import path
from stocksapp import views

urlpatterns = [

    path('',views.first,name='first'),
    path('f/', views.home, name='home'),
    path('intradaydata/',views.get_intra_day_data, name='getintradaylivedata'),
    path('livedata/',views.get_data, name='getlivedata'),
    path('adjlivedata/',views.get_adj_data, name='getadjlivedata'),
    path('gethistdata/',views.get_data, name='gethistdata'),
    path('getsmadata/',views.get_sma, name='getsmadata'),
    path('getemadata/',views.get_ema, name='getemadata'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    #path('simfin/', views.post_list, name='post_list'),

]
