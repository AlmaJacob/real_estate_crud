from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import estateViewset,CartView, CartRemoveView,RegisterUserView,UserListView,LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'estatehub',estateViewset)
#path specified.
urlpatterns = [
    path('',include(router.urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/', CartRemoveView.as_view(), name='remove-from-cart'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user-list'),
]
