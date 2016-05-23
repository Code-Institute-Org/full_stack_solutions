from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
	"""
	Create a view that will return a
	list of Posts that were published prior to'now'
	and render them to the 'blogposts.html' template
	"""
	posts = Post.objects.filter(published_date__lte=timezone.now()
		).order_by('-published_date')
	return render(request, "blogposts.html", {'posts': posts})


def post_details(request, id):
	"""
	Create a view that return a single
	Post object based on the post ID and
	and render it to the 'postdetail.html'
	template. Or return a 404 error if the 
	post is not found
	"""
	post = get_object_or_404(Post, pk=id)
	return render(request, "postdetail.html", {'post': post})
