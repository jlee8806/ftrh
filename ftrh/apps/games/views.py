from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import PostGame
from .models import game

def create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostGame(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Ya did good son")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, 'games/postform.html', context)

def detail(request, id):
	instance = get_object_or_404(game, id=id)
	context = {
	"title": instance.title,
	"instance" : instance
	}
	return render(request, 'games/detail.html', context)

def list(request):
	# if request.user.is_authenticated():
	queryset_list = game.objects.all().order_by("title")
	paginator = Paginator(queryset_list,12)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
	"object_list" : queryset,
	"title": "List"
	}
	return render(request, 'games/list.html', context)

def update(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(game, id=id)
	form = PostGame(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Ya did good son")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"title": instance.title,
	"instance" : instance,
	"form":form
	}
	return render(request, 'games/postform.html', context)

def delete(request, id=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(game, id=id)
	instance.delete()
	messages.success(request, "Burn dat shit")
	return redirect("games:list")
