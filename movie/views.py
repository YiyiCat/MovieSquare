# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from models import *
from forms import *


# Create your views here.

@login_required
def getMoviePoster(request, movie_name, page):
    if page is None:
        page = 1
    movie = Movie.objects.get(name=movie_name)
    plates = [(
        Post.objects.filter(movie__name__contains=movie_name).order_by("-time")[page - 1:page + 19], "plate_all",
        "全部")] + [
                 (Post.objects.filter(movie__name__contains=movie_name, plate=plate_id).order_by("-time")[
                  page - 1:page + 19], "plate_{}".format(plate_id),
                  plate_name)
                 for plate_id, plate_name in validPlates]
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.movie_id = movie_name
            post.poster = request.user
            post.save()
            form = PostForm()
    else:
        form = PostForm()
    return render(request, "getMoviePoster.html", locals())


def getMoviePosterAll(request, movie_name, page):
    Poster = Post.objects.filter(movie__name=movie_name).order_by("-time")[page - 1:page + 18]
    movie = Movie.objects.get(name=movie_name)
    return render(request, "getMoviePoster.html", locals())


@login_required
def newPost(request, movie_name):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.movie_id = movie_name
            post.poster = request.user
            post.save()
            form = PostForm()
    else:
        form = PostForm()
    return render(request, "newPost.html", locals())


# class RegisterView(FormView):
#     template_name = 'register.html'
#     form_class = UserCreationForm
#     success_url = reverse("login")
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.save()
#         return super(RegisterView, self).form_valid(form)


def registerView(request):
    if request.method == "POST":
        form1 = RegisterForm(request.POST)
        form2 = RegisterProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            profile = form2.save(commit=False)
            profile.auth_user = user
            profile.save()
            return redirect("login")
    else:
        form1 = RegisterForm()
        form2 = RegisterProfileForm()
    return render(request, "register.html", locals())


# class PostDetailView(DetailView):
#     model = Post


@login_required
def postDetailView(request, pk):
    post = Post.objects.get(id=pk)
    contents = Reply.objects.filter(post_id=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post_id = pk
            reply.save()
            form = ReplyForm()
    else:
        form = ReplyForm()
    return render(request, "movie/post_detail.html", locals())


def getReplies(request, post_id):
    post = Post.objects.get(id=post_id)
    contents = Reply.objects.filter(id=post_id).order_by("-time")[0, 19]
    return render(request, "getReplies.html", locals())


def getRepliesPage(request, post_id, page):
    post = Post.objects.get(id=post_id)
    contents = Reply.objects.filter(id=post_id).order_by("-time")[page - 1:page + 18]
    return render(request, "getReplies.html", locals())


@login_required
def newReply(request, post_id):
    if request.method == "POST":
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post_id = post_id
            reply.save()
            form = ReplyForm()
    else:
        form = ReplyForm()
    return render(request, "newReply.html", locals())


def index(request):
    return render(request, "index.html")
