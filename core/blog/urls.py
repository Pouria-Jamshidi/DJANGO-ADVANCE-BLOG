from django.urls import path
from blog.views import IndexView_cbv, PostListView, PostDetailView\
    , PostCreateView, PostUpdateView, PostDeleteView
from django.views.generic import RedirectView

app_name = 'blog'

urlpatterns = [
    path('cbv-index/', IndexView_cbv.as_view(), name='cbv-index'),
    path('redirect/', RedirectView.as_view(pattern_name='blog:cbv-index'), name='redirect-to-index'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name= 'post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name= 'post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name= 'post-delete'),
]