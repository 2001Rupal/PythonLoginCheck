from django.urls import path
from .views import LoginView, ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('protected/', ProtectedView.as_view(), name='protected'),  
]


