from django.urls import path
from .views import MaseratiList, MaseratiDetail

urlpatterns = [
    path('', MaseratiList.as_view(), name='vehicle_list'),
    path('<int:pk>', MaseratiDetail.as_view(), name='vehicle_list'),
]