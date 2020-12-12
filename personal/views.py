from django.shortcuts import render
from .models import Topic

# Create your views here.
def indexview(request):
	return render(request, "home.html")

def ngoview(request):
	topic = Topic.objects.all()

	context = {
		'topic' : topic,
	}
	return render(request, "search.html", context)

def aboutview(request):
	return render(request, "about.html")