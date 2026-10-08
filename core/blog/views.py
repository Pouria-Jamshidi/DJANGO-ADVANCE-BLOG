from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView_cbv(TemplateView):
    """
    class based view for index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context["posts"] = Post.objects.all()
        return context

class PostListView(LoginRequiredMixin, ListView):
    """
    Class based view for posts
    """
    # model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-publish_date')
        return posts

class PostDetailView(LoginRequiredMixin, DetailView):
    """
    Class based view for post detail
    """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Class based view for creating a post
    """
    model = Post
    template_name = "blog/create_post.html"
    fields = ['title', 'content', 'status', 'category', 'publish_date']
    success_url = reverse_lazy('blog:post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class based view for updating a post
    """
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs = {'pk':self.object.id})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class based view for deleting a post
    """
    model = Post
    success_url = reverse_lazy('blog:post-list')