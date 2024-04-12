from django.urls import path
from .views import *

urlpatterns = [
    path('post/', ProductView.as_view()),
    path('edit/<int:id>/', ProductEditView.as_view()),
    path('get/', GetallView.as_view()),
]