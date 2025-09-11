from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import PostForm, PostModelForm
from .models import Post, Author, Comment
from .tasks import send_notification_email



# # Create your views here.
# def home(request):
#     return render(request, 'blog_app/index.html')


class IndexTemplateView(TemplateView):
    """ Представление для отображения страницы 'Главная'. """
    template_name = 'blog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['description'] = 'Добро пожаловать на наш блог!'
        return context



# def about(request):
#     return render(request, 'blog_app/about.html')


class AboutTemplateView(TemplateView):
    """ Представление для отображения страницы 'О нас'. """
    template_name = 'blog_app/about.html'



# def post_list(request):
#     posts = Post.objects.all()
#     # posts = Post.objects.filter(id=10)
#
#     context = {
#         'title': 'Список постов',
#         'posts': posts
#     }
#     return render(request, 'blog_app/post_list.html', context=context)


class PostListView(ListView):
    """ Представление для отображения списка постов. """
    model = Post
    template_name = 'blog_app/post_list.html'
    context_object_name = 'posts'

#
# def post_detail(request, post_id):
#     # post = Post.objects.get(id=post_id)
#     post = get_object_or_404(Post, pk=post_id)
#     # comments = post.comments.all()
#     comments = Comment.objects.filter(post=post)
#     tags = post.tags.all()
#     context = {
#         # 'title': 'Список постов',
#         'post': post,
#         'comments': comments,
#         'tags': tags
#     }
#     return render(request, 'blog_app/post_detail.html', context=context)


class PostDetailView(DetailView):
    """ Представление для отображения деталей поста. """
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = 'Детальный пост!'
        return context

# def post_add(request):
#     """Представление для добавления нового поста через форму."""
#     if request.method == 'POST':
#         # form = PostForm(request.POST)
#         form = PostModelForm(request.POST)
#         if form.is_valid():
#             # Post.objects.create(
#             #     title=form.cleaned_data['title'],
#             #     content=form.cleaned_data['content'],
#             #     author=form.cleaned_data['author'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             form.save()
#             return redirect('post_list')
#     else:
#         # form = PostForm()
#         form = PostModelForm()
#
#     context = {
#         'form': form,
#         'title': 'Добавить пост',
#     }
#     return render(request, 'blog_app/post_add.html', context=context)


class PostCreateView(CreateView):
    """ Представление для создания поста. """
    model = Post
    template_name = 'blog_app/post_add.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_notification_email.delay(
            recipient_email='user@example.com',
            subject='Новый пост',
            message=f'Пост "{form.instance.title}" был успешно создан'
        )
        messages.success(self.request, 'Пост был успешно создан! Уведомление отправлено')
        return response



#
# def post_edit(request, post_id):
#     """Представление для редактировани поста через форму."""
#     post = get_object_or_404(Post, pk=post_id)
#
#     if request.method == 'POST':
#         form = PostModelForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostModelForm(instance=post)
#
#     context = {
#         'form': form,
#         'title': f'Редактировать пост {post.title}',
#     }
#     return render(request, 'blog_app/post_edit.html', context=context)


class PostUpdateView(UpdateView):
    """ Представление для редактирования поста. """
    model = Post
    template_name = 'blog_app/post_edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('post_list')


class PostDeleteView(DeleteView):
    """ Представление для удаления поста. """
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('post_list')


def author_list(request):
    authors = Author.objects.all()
    context = {
        'title': 'Список авторов',
        'authors': authors
    }
    return render(request, 'blog_app/author_list.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {
        # 'title': 'Список постов',
        'author': author,
        # 'posts': author.posts.all()
    }
    return render(request, 'blog_app/author_detail.html', context=context)
