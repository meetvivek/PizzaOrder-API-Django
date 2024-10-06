from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='orders_detail'),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_orders_status'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:user_id>/orders/<int:order_id>', views.UserOrdersDetail.as_view(), name='user_orders_detail'),
    
]

