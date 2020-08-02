from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from login.views import LoginViewset
from dashboard.views import DashboardViewset
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'login', LoginViewset)
router.register(r'dashboard', DashboardViewset)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
