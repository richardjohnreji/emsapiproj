from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

#create an instance of the DefaultRouter class
router = DefaultRouter() 

#registering the mapping for url and views
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path("Signup/",views.SignupAPIView.as_view(), name="user-signup"),
    path("Login/",views.LoginAPIView.as_view(), name="user-login"),
]

 

#create a urlpatterns list from the router urls
urlpatterns = urlpatterns + router.urls