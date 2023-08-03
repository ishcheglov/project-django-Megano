from orders.views import Orders, OrderDetail, PaymentView
from django.urls import path

urlpatterns = [
    path("api/orders/", Orders.as_view(), name='orders'),
    path("api/orders/<int:pk>/", OrderDetail.as_view(), name='order_detail'),
    path("api/payment/<int:pk>/", PaymentView.as_view(), name='payment'),
]
