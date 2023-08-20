"""PID URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.contrib import admin
from PID_app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^$',Home_page),
    url(r'^Home_page', Home_page, name="Home_page"),
    url(r'^CheckLogin', CheckLogin, name="CheckLogin"),
    url(r'^Login_page',Login_page,name="Login_page"),
    url(r'^Reg_customer',Reg_customer,name="Reg_customer"),
    url(r'^Save_cutomer',Save_cutomer,name="Save_cutomer"),
    url(r'^Reg_Volunteer',Reg_Volunteer,name="Reg_Volunteer"),
    url(r'^Save_volunteer',Save_volunteer,name="Save_volunteer"),
    url(r'^About_page',About_page,name="About_page"),
    url(r'^Customer_home',Customer_home,name="Customer_home"),
    url(r'^Volunteer_home',Volunteer_home,name="Volunteer_home"),
    url(r'^Customer_add_request',Customer_add_request,name="Customer_add_request"),
    url(r'^Add_request_data',Add_request_data,name="Add_request_data"),
    url(r'^Customer_view_requests',Customer_view_requests,name="Customer_view_requests"),
    url(r'^Volunteer_view_request',Volunteer_view_request,name="Volunteer_view_request"),
    url(r'^Accept_wrequest',Accept_wrequest,name="Accept_wrequest"),
    url(r'^Volunterr_accepted_requests',Volunterr_accepted_requests,name="Volunterr_accepted_requests"),
    url(r'^Get_waste_loc',Get_waste_loc,name="Get_waste_loc"),
    url(r'^Volunterr_view_map',Volunterr_view_map,name="Volunterr_view_map"),
    url(r'^Save_waste_id',Save_waste_id,name="Save_waste_id"),
    url(r'^Volunterr_edit_waste',Volunterr_edit_waste,name="Volunterr_edit_waste"),
    url(r'^Update_status',Update_status,name="Update_status"),
    url(r'^Update_work',Update_work,name="Update_work"),
    url(r'^Volunteer_view_route',Volunteer_view_route,name="Volunteer_view_route"),
    url(r'^Volunteer_get_locations',Volunteer_get_locations,name="Volunteer_get_locations"),
    url(r'^Volunteer_list_user_page',Volunteer_list_user_page,name="Volunteer_list_user_page"),
    url(r'^Volunteer_chat_page',Volunteer_chat_page,name="Volunteer_chat_page"),
    url(r'^Customer_list_user_page',Customer_list_user_page,name="Customer_list_user_page"),
    url(r'^Customer_chat_page',Customer_chat_page,name="Customer_chat_page"),




    url(r'^Addchat',Addchat,name="Addchat"),
    url(r'^Save_user2_id',Save_user2_id,name="Save_user2_id"),
    url(r'^Getallchats',Getallchats,name="Getallchats"),






]
