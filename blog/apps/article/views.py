from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

from .models import Article, Comment

def post_list(request):
	latest_article_list = Article.objects.order_by('-pub_date')
	paginator = Paginator(latest_article_list, 10)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator,page(paginator.num_pages)
	return render(request, 'article/list.html', {'page': page, 'posts': posts})

def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Статья не найдена!")

	latest_comment_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'article/detail.html', {'article':a, 'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('article:detail', args = (a.id, )) )


