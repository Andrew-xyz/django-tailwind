from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page_one', views.page_one, name='page_one'),
    path('page_two', views.page_two, name='page_two'),
    path('page_three', views.page_three, name='page_three'),
]
