from django.urls import path
from . import views

urlpatterns = [

    path('create', views.create, name='create'),    #this are Html that will be displayed for users to see and have access to...
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]
