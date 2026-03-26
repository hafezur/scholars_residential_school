from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('custom_admin/', views.custom_admin,name="admin_panel"),
    path('login/', views.user_login,name="get_login"),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('logout/', views.logout_view,name="logout"),
    path('user_dashboard/', views.userDashboard,name="userDashboard"),
    path('updateProfile/', views.profile_update, name='updateProfile'),
]
