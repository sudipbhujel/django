from django.shortcuts import render

from .models import Courses

def index(request):
	if request.method == 'POST':
		Course1 = request.POST.get('Course')
		Subject1 = request.POST.get('Subject')
		Rating1 = request.POST.get('Rating')
		var_Course = Courses(Course = Course1 ,Subject = Subject1,Rating = Rating1)
		var_Course.save()
		return render(request,'blog/home.html')
	else:
		return render(request, 'blog/home.html')