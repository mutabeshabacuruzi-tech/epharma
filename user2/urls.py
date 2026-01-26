from django.urls import path
from .views import connection
# from . import views
urlpatterns = [
    path('login/', connection, name='login')
    path('logout/', deconnection, name='logout')

]