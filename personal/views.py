from django.shortcuts import render
from .models import Topic

# Create your views here.
def indexview(request):
	topic = Topic.objects.all().order_by('-date')

	context = {
		'topic' : topic,
	}
	return render(request, "home.html", context)

def aboutview(request):
	return render(request, "about.html")