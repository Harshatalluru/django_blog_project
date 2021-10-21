    
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import post,contactus
from .forms import blogform
from translate import Translator

# Create your views here.


def homepage(request):
    posts = post.objects.all()
    return render(request,'index.html',{'posts':posts})

def blogpost(request, pk):
    posts = post.objects.get(title=pk)
    return render(request,'blog-post.html',{'posts':posts})

def about(request):
    return render(request,'about.html')


#def Login(request):
    context ={}
    context["form"] = form
    return render(request,'login.html',context)
    '''if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return redirect('validcheck/') 

    else:

        prirnt('error')  '''        

#def signup(request):
    #return render(request,'signup.html')
    '''  if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       
        if User.objects.filter(username=username).exists():
            flash = 'username already used'
            return render(request,'logandreg.html',{'flash':flash})
        elif User.objects.filter(email=email).exists():
            flash = 'email already used'
            return render(request,'logandreg.html',{'flash':flash})
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            return render(request,'logandreg.html')

    else:
        return render(request,'logandreg.html')

    return render(request,'logandreg.html')'''

     
                   




def contact(request):
    if request.method== 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        country=request.POST['country']
        message = request.POST['message']
        contact=contactus.objects.create(first_name=first_name,last_name=last_name,country=country,message=message)
        flash = 'submitted successfully'
        return render(request,'contact.html',{'flash':flash})
    else:
        flash = 'error detected'
        return render(request,'contact.html',{'flash':flash})

    
    
    return render(request,'contact.html')


   
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = blogform(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['post']= form
    return render(request, "add_post.html", context)



def list_view(request):
    return render(request,'blog-list.html')


# update view for details
def update_post(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(post, title = pk)
 
    # pass the object as instance in form
    form = blogform(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
       
        return render(request,"blog-post.html")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context) 

def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(post, title = pk)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return render(request,'blog-list.html')
 
    return render(request, "delete_view.html", context)    


def translator(request):
    if request.method == 'POST':
        text = request.POST['translator']
        language = request.POST['language']
        translator=Translator(to_lang=language)
        translation=translator.translate(text)
        return HttpResponse(translation)
    return render(request,"translator.html")    
