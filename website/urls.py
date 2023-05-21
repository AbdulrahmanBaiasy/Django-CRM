
from django.urls import path
from . import views 

urlpatterns = [
    path ('',views.home, name  ='home'),
    path ('register/',views.register_user, name  ='register'),
    path ('logout/',views.logout_user,name='logout'),
    path ('record/<int:pk>',views.customer_record,name='record'),
    path ('record/delete/<int:pk>',views.customer_delete_record,name='delete_record'),
    path ('record/add_record/',views.add_record,name='add_record'),
    path ('record/update/<int:pk>',views.customer_update_record,name='update_record'),


]
