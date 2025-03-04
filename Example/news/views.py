from django.shortcuts import render
from .models import News_post, Full_post

def home(request):
	news = Full_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

def create_news(request):
	return render(request, 'news/add_new_post.html')



