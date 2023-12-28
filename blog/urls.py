from django.urls import path
from .views import *


urlpatterns =[
    path("",HomePageView.as_view(), name="home" ),
    path('post/<int:pk>', DetailPageView.as_view(), name="blog_details" ),
    path('post/edit/<int:pk>', UpdatePostView.as_view(),name="update_post"),
    path('post/del/<int:pk>', DeletPostView.as_view(), name='delete_post'),
    path('newpost', PostNewView.as_view(), name="post_new")
]