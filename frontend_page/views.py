from django.shortcuts import render, redirect
from . import admin
from django.core.files.storage import FileSystemStorage
from .models import Imageblog, Category
from .forms import BlogForm, UpdateForm, CategoryForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 

# Create your views here.
def homepage(request):

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(homepage, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

    return render(request, 'home.html')



def photos(request):
    images = Imageblog.objects.all()
    context = {
        'images':images
    }
    return render(request, 'photo.html', context)

class BlogView(ListView):
    model = Imageblog
    template_name = 'blog.html'
    ordering = ['-post_date']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    
class BlogDetailView(DetailView):
    model = Imageblog
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class AddPostView(CreateView):
    model = Imageblog
    form_class = BlogForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'
    # fieds = '__all__'

def CategoryView(request, cats):
    category_post = Imageblog.objects.filter(category=cats)
    context ={
        'cats':cats,
        'category_post':category_post
    }
    return render(request, 'categories.html', context)

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    context ={
        'cat_menu_list':cat_menu_list
    }
    
    return render(request, 'cat_menu_list.html', context)


class UpdatePostView(UpdateView):
    model = Imageblog
    form_class = UpdateForm
    template_name = 'update.html'

class DeletePostView(DeleteView):
    model = Imageblog
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')
