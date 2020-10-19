from django.urls import path
from ayeApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax_call/', views.ajax_call, name='email_form_view')
 ]
