from django.urls import path
from . import views
from .views import BlogView,BlogDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('photos/', views.photos, name='photos'),
    path('blog/', BlogView.as_view(), name='blog' ),
    path('article-details/<int:pk>/', BlogDetailView.as_view(), name='article-details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('updatepost/<int:pk>', UpdatePostView.as_view(), name='update_post' ),
    path('deletepost/<int:pk>', DeletePostView.as_view(), name='delete_post' ),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='categories_list')
    
]