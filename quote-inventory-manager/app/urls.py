from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    # re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # # The home page
    # path('', views.index, name='index'),

    path('', views.index, name='index'),
    path('customers/', views.customers, name="customers"),
    path('add_customer/', views.add_customer, name="add_customer"),
    path('edit_customer/<str:cust_id>', views.edit_customer, name="edit_customer"),
    path('delete_customer/<str:cust_id>', views.delete_customer, name="delete_customer"),

    path('providers/', views.providers, name="providers"),
    path('add_provider/', views.add_provider, name="add_provider"),
    path('edit_provider/<str:prov_id>', views.edit_provider, name="edit_provider"),
    path('delete_provider/<str:prov_id>', views.delete_provider, name="delete_provider"),

    path('makers/', views.makers, name="makers"),
    path('add_maker/', views.add_maker , name="add_maker"),
    path('edit_maker/<str:mk_id>', views.edit_maker, name="edit_maker"),
    path('delete_maker/<str:mk_id>', views.delete_maker, name="delete_maker"),


    path('hdd_capacities/', views.hdd_capacities, name="hdd_capacities"),
    path('add_hdd_capacity/', views.add_hdd_capacity , name="add_hdd_capacity"),
    path('edit_hdd_capacity/<str:hdd_cap_id>', views.edit_hdd_capacity, name="edit_hdd_capacity"),
    path('delete_hdd_capacity/<str:hdd_cap_id>', views.delete_hdd_capacity, name="delete_hdd_capacity"),

    path('nas_accessory_categories/', views.nas_accessory_categories, name="nas_accessory_categories"),
    path('add_nas_accessory_category/', views.add_nas_accessory_category, name="add_nas_accessory_category"),
    path('edit_nas_accessory_category/<str:nas_acc_cat_id>', views.edit_nas_accessory_category, name="edit_nas_accessory_category"),
    path('delete_nas_accessory_category/<str:nas_acc_cat_id>', views.delete_nas_accessory_category, name="delete_nas_accessory_category"),

    path('nas_models/', views.nas_models, name="nas_models"),
    path('add_nas_model', views.add_nas_model, name="add_nas_model"),
    path('edit_nas_model/<str:nas_model_id>', views.edit_nas_model, name="edit_nas_model"),
    path('delete_nas_model/<str:nas_model_id>', views.delete_nas_model, name="delete_nas_model" ),

    path('nas_accessories/', views.nas_accessories, name="nas_accessories"),
    path('add_nas_accessory', views.add_nas_accessory, name="add_nas_accessory"),
    path('edit_nas_accessory/<str:nas_acc_id>', views.edit_nas_accessory, name="edit_nas_accessory"),
    path('delete_nas_accessory/<str:nas_acc_id>', views.delete_nas_accessory, name="delete_nas_accessory"),
]
