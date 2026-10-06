from django.urls import path
from . import views

# urlpatterns = [

#     path(
#         '',
#         views.home,
#         name='home'
#     ),

#     path(
#         'register/',
#         views.register,
#         name='register'
#     ),

#     path(
#         'login/',
#         views.login_user,
#         name='login'
#     ),

#     path(
#         'logout/',
#         views.logout_user,
#         name='logout'
#     ),

#     path(
#         'add-food/',
#         views.add_food,
#         name='add_food'
#     ),

#     path(
#         'edit-food/<int:id>/',
#         views.edit_food,
#         name='edit_food'
#     ),

#     path(
#         'delete-food/<int:id>/',
#         views.delete_food,
#         name='delete_food'
#     ),

#     path(
#     'order/<int:id>/',
#     views.order_food,
#     name='order_food'
# ),

# path(
#     'my-orders/',
#     views.my_orders,
#     name='my_orders'
# ),

# path('api/foods/', views.food_api, name='food_api'),


# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('add-food/', views.add_food, name='add_food'),
    path('edit-food/<int:id>/', views.edit_food, name='edit_food'),
    path('delete-food/<int:id>/', views.delete_food, name='delete_food'),

    path('order/<int:id>/', views.order_food, name='order_food'),
    path('my-orders/', views.my_orders, name='my_orders'),

    path('api/foods/', views.food_api, name='food_api'),
    path('api/foods/<int:id>/', views.food_detail_api, name='food_detail_api'),
]