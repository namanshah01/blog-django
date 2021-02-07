from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'Blog - About Page'})

# dummy_data = [
# 	{
# 		'title': 'Coffee Jelly',
# 		'author': 'Kusuo Saiki',
# 		'content': 'Some content for the first blog. Yare yare',
# 		'time': 'Dec 2020',
# 	},
# 	{
# 		'title': 'Dark Reunion',
# 		'author': 'Shun Kaido',
# 		'content': 'I sense a dark energy is coming for us',
# 		'time': 'Jan 2021',
# 	},
# 	{
# 		'title': 'Ramen',
# 		'author': 'Riki Nendo',
# 		'content': 'Oh aibo, ramen ikoze?',
# 		'time': 'Nov 2020',
# 	}
# ]
