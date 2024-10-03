from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET:
            search = self.request.GET.get('search')
            posts = Post.objects.filter(title__icontains=search)
            context['posts'] = posts

        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created')[:4]
        return context


class SingleBlogView(DetailView):
    model = Post
    template_name = 'single-blog.html'
    context_object_name = 'post'

    def post(self, request, pk):
        p = Post.objects.get(id=pk)
        p.likes += 1
        p.save()
        return redirect('single-blog', pk=p.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        index = list(posts).index(self.object)
        context['posts'] = posts

        try:
            context['previous'] = posts[index - 1]
        except:
            context['previous'] = posts[index]
        try:
            context['next'] = posts[index + 1]
        except:
            context['next'] = posts[index]

        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created')[:4]
        try:
            context['best'] = Comments.objects.filter(Q(post=self.object) & Q(best_comment=True))[0]
        except:
            context['best'] = None
        context['comments'] = Comments.objects.filter(post=self.object)

        return context
