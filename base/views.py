from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreatePost, CommentForm
from .filters import PostFilter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
	posts = Post.objects.filter(active = True, featured = True)[0:3]
	tags = Tag.objects.all()[0:5]
	context = {'posts' : posts, 'tags':tags}	
	print(tags)
	return render(request, 'base/index.html', context)

def posts(request):
	posts = Post.objects.filter(active = True)
	myFilter = PostFilter(request.GET, queryset = posts)
	posts = myFilter.qs

	page = request.GET.get('page')
	paginator = Paginator(posts, 3)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	print(posts.number)
	context = {'posts' : posts, 'myFilter' : myFilter}
	return render(request, 'base/posts.html', context)

def post(request, slug):
	post = Post.objects.get(slug = slug)
	c_form = CommentForm()
	if request.method == "POST":
		c_form = CommentForm(request.POST)
		if c_form.is_valid():
			instance = c_form.save(commit = False)
			instance.post = Post.objects.get(id = request.POST.get('post-id'))
			instance.user = request.POST.get('user')
			instance.save()
			c_form = CommentForm()
	context = {'posts' : post, 'c_form': c_form}
	return render(request, 'base/post.html', context)

def profile(request):
	return render(request, 'base/profile.html')

def tagPosts(request, name):
	posts = Post.objects.filter(tags__name = name)
	print(posts)
	myFilter = PostFilter(request.GET, queryset = posts)
	posts = myFilter.qs
	context = {'posts': posts, 'name':name}
	return render(request, 'base/posts.html', context)

@login_required(login_url = 'home')
def createPost(request):
	form = CreatePost()
	if request.method == "POST":
		form = CreatePost(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')
	context = {'form' : form}
	return render(request, 'base/post_form.html', context)

@login_required(login_url = 'home')
def updatePost(request, slug):
	post = Post.objects.get(slug = slug)
	form = CreatePost(instance = post)
	if request.method == "POST":
		form = CreatePost(request.POST, request.FILES, instance = post)
		if form.is_valid():
			form.save()
		return redirect('posts')
	context = {'form' : form}
	return render(request, 'base/post_form.html', context)


@login_required(login_url = 'home')
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method == 'POST':
		post.delete()
		return redirect('posts')
	context = {'item' : post}
	return render(request, 'base/delete_confirm.html', context)


def send_email(request):
	if request.method == 'POST':
		template = render_to_string('base/email_template.html', {
			'name': request.POST['name'],
			'email': request.POST['email'],
			'message': request.POST['message'],
			})

		print(template)

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['tushar24081@gmail.com']
			)
		email.fail_silently = False
		email.send()

	return render(request, 'base/email_sent.html')