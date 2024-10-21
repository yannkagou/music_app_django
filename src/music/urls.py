from django.urls import path

from . import views

urlpatterns = [
    path('subscribers/', views.SubscriberAdd.as_view()),
    path('subscribers/<int:pk>/', views.SubscriberDetails.as_view()),
    path('subscribers/me/', views.CurrentSubscriber.as_view()),
]