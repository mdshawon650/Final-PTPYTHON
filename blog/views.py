from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailsView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})
