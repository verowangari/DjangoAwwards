from django.shortcuts import render,redirect
from django.template import loader
from django.http  import HttpResponse
from .forms import SignupForm,UserUpdateForm, ProfileUpdateForm,NewPostForm,RateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer,ProfileSerializer
from rest_framework import status
#................
# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request,id):
    user=request.user
    # posts=Post.objects.filter(user=user)
    posts = Post.objects.filter(user=id)
    
    # group_ids=[]
    
    for posts in posts:
        # group_ids.append(post.post_profile)

        post_items = Post.objects.all()
    template=loader.get_template('index.html')

    context={
    'post_items':post_items,
}

    return HttpResponse(template.render(context,request))



# def index(request):
#     post_items = Post.objects.all()
#     return render(request, 'index.html', {"post_items": post_items})



class PostList(APIView):
    def get(self,request,format = None):
        all_posts = Post.objects.all()
        serializerdata = PostSerializer(all_posts,many = True)
        return Response(serializerdata.data)
    
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



def posts(request, id):
    postie = Post.objects.get(id=id)
    return render(request, 'readmore.html', {"postie": postie})

def profile(request,id):
    prof = Profile.objects.get(user = id)
    return render(request,'profile.html',{"profile":prof})

class ProfileList(APIView):
    def get(self,request,format = None):
        all_profile = Profile.objects.all()
        serializerdata = ProfileSerializer(all_profile,many = True)
        return Response(serializerdata.data)
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


   

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
			return redirect('index')
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
    
# @login_required
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

# @login_required
@login_required(login_url='login')      
def NewPost(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.profile=current_user
            new_post.save()
            print('post saved')
            return redirect(index)
    else:
        form = NewPostForm()
    return render(request, 'newpost.html',{'form':form})

@login_required(login_url='login')   
def rate(request,id):
    # reviews = Revieww.objects.get(projects_id = id).all()
    # print
    post = Post.objects.get(id = id)
    # post = Post.objects.get(post = post)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.profile = user
            rate.post = post
            # rate.save()
            return redirect('index')
    else:
        form = RateForm()
    return render(request,"rate.html",{"form":form,"post":post})