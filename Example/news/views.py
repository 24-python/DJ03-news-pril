from django.shortcuts import render, redirect
from .models import News_post, Full_post
from .forms import Full_postForm

def home(request):
	news = Full_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

def create_news(request):
	error = ""
	if request.method == 'POST':
		form = Full_postForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Данные введены некорректно'

	form = Full_postForm()
	return render(request, 'news/add_new_post.html', {'form': form, 'errors': error})




