# -*-coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentsForm
from comments.models import Comments
from .models import Article, Category
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
import json
# Create your views here.


def index(request, num=0):
    num = int(num)
    page = {'previous': num-1, 'next': num+1}
    latest_article_list = Article.objects.filter(is_active=True).order_by('-pub_date')[num*8:num*8+8]
    next_page = Article.objects.filter(is_active=True).order_by('-pub_date')[num*8+8:num*8+16]
    for article in latest_article_list:
        article.count_comments = Comments.objects.filter(enable=True, article=article.id).count()
    if latest_article_list:
        context = {'latest_article_list': latest_article_list, 'next_page': next_page, 'page': page}
        return render(request, 'article/index.html', context)
    else:
        return render(request, 'article/404.html')


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id, is_active=True)
    comments = Comments.objects.filter(article=article_id, enable=True).order_by('-pub_date')
    count_comments = comments.count()
    form = CommentsForm()
    recommend = Article.objects.filter(is_active=True).order_by('-pub_date')[0:4]
    context = {'article': article, 'comments': comments,
    'count_comments': count_comments,
    'form': form,
    'recommend': recommend
    }
    return render(request, 'article/article.html', context)


def category(request, category_id, num=0):
    num = int(num)
    page = {'previous': num-1, 'next': num+1}
    latest_article_list = Article.objects.filter(is_active=True, category=category_id).order_by('-pub_date')[num*8:num*8+8]
    next_page = Article.objects.filter(is_active=True, category=category_id).order_by('-pub_date')[num*8+8:num*8+16]
    for article in latest_article_list:
        article.count_comments = Comments.objects.filter(enable=True, article=article.id).count()
    if latest_article_list:
        context = {'latest_article_list': latest_article_list, 'next_page': next_page, 'page': page, 'category_id': category_id}
        return render(request, 'article/index.html', context)
    else:
        return render(request, 'article/404.html')


def create_comments(request, article_id):
    article = Article.objects.get(pk=article_id)
    form = CommentsForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article = article
        obj.author = request.user
        obj.save()
        return redirect('/article/%s#comments' % article.id)
    return redirect('/')


def del_comments(request, comment_id):
    comment = Comments.objects.get(pk=comment_id)
    article = comment.article
    if request.user == comment.author:
        comment.delete()
        return redirect('/article/%s#comments' % article.id)
    return redirect('/')


def update_comment(request, comment_id):
    comment = Comments.objects.get(pk=comment_id)
    article = comment.article.id
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment.body = request.POST['body']
        comment.save()
        return redirect('/article/%s#comments' % article)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


class RegistrationForm(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'article/reg.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationForm, self).form_valid(form)


class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = 'article/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginForm, self).form_valid(form)
