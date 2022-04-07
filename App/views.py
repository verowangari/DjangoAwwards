from django.shortcuts import render,redirect
from django.template import loader
from django.http  import HttpResponse
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#................
# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def Signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			return redirect('welcome')
	else:
		form = SignupForm()
	
	context = {
		'form':form,
	}

	return render(request, 'signup.html', context)

# @login_required
def Search_users(request):
    template = loader.get_template('search_users.html')
    
    if request.method =='POST':
        searched=request.POST['searched']
       
        # searched=Post.objects.filter(user_id__icontains=searched)
        # searcheduser = Post.objects.filter(user__icontains=searched)
        
        context={
            'searched':searched,
            # 'searcheduser':searcheduser,
        }
        return HttpResponse(template.render(context,request))
        
    else:
        return HttpResponse(template.render())