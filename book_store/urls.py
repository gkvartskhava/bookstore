
from django.contrib import admin
from django.urls import path,include
from store.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('api/login', CustomAuthToken.as_view()),

]
