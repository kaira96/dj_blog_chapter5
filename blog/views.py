from django.views.generic import (
							ListView, 
							DetailView, 
							CreateView, 
							UpdateView, 
							DeleteView
						)
from .models import Post
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy


class BlogListView(ListView):
	model = Post
	template_name = 'post_list.html'
	context_object_name = 'posts'

class BlogDetailView(DetailView): # new
	model = Post
	template_name = 'post_detail.html'

class PostCreateView(CreateView): # new
	model = Post
	template_name = 'post_new.html'
	form_class = PostForm

class PostUpdateView(UpdateView): # new
	model = Post
	template_name = 'post_edit.html'
	form_class = PostEditForm

class PostDeleteView(DeleteView): # new
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')