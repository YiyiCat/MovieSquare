from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from models import *
from forms import *


# Create your views here.
def getMoviePoster(request):
    form = MoviePosterForm(request.GET)
    valid = form.is_valid()
    if valid:
        cd = form.cleaned_data
        contents = Post.objects.filter(movie__name__contains=cd["movie"], plate=cd["plate"]).order_by("-time")
    return render(request, "getMoviePoster.html", locals())


@login_required
def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
            form = PostForm()
    else:
        form = PostForm()
    return render(request, "newPost.html", locals())


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = "/getMoviePoster/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(RegisterView, self).form_valid(form)


class PostDetailView(DetailView):
    model = Post


def getReplies(request, post_id):
    contents = Reply.objects.filter(post_id=post_id).order_by("-time")
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
