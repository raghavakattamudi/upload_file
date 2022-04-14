from django.shortcuts import render
from .forms import GeeksForm

def handle_uploaded_file(f):
	with open('uploadfile/upload/'+f.name, 'wb') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
   
   
# Create your views here.
def home_view(request):
	context = {}
	if request.POST:
		form = GeeksForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES["geeks_field"])
	else:
		form = GeeksForm()
	context['form'] = form
	return render(request, "uploadfile\home.html", context)
