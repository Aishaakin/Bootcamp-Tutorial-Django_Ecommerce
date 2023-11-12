from django.urls import path
from .views import *
app_name = 'blog'
urlpatterns = [
path("home",BlogHome,name = "bloghome"),
path("shop",ShopHome,name = "shophome"),
path("12345",BlogMain,name = "blogmain"),
path("viewdata",ViewData,name = "viewdata")

]