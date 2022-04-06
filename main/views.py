from django.shortcuts import render
from django.contrib.auth.models import User

from .models import articles

def home(request):
    queryset = articles.objects.all()
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def Sign(request):
    return render(request,'sign.html')

def write(request):
    current = request.user.id
    if current == None:
     print(current)
     mess = 'You are not loged in'
     return render(request,'home.html',{'mess':mess})
    else:
        return render(request,'write.html')

def logpage(request):
    return render(request,'log.html')

def homes(request):
    queryset = articles.objects.all()
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            message = 'username taken'
            return render(request,'sign.html',{'mess':message})
        elif pass1 != pass2:
            message = 'password one is not equal to password two'
            return render(request,'sign.html',{'mess':message})
        else:
            user = User.objects.create_user(email=email,username=username,password=pass2)
            user.save()
            mess='Account created'
            return render(request,'home.html',{'mess':mess})

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

from .models import comment

def comments(request,article):
     comments.article = article
     query1 = articles.objects.get(id=article)
     query = comment.objects.filter(post=article)
     return render(request,'mypost.html',{'comments':query ,'post':query1})

def post_comment(request):
    if request.method == 'POST':
        comment1 = request.POST['content']
        user = request.user.username
        save = comment(content=comment1,post=comments.article,write=user)
        save.save()
        query1 = articles.objects.get(id=comments.article)
        query = comment.objects.filter(post=comments.article)
        return render(request,'mypost.html',{'comments':query ,'post':query1})

def log(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        mess = 'You are now loged in'
        return render(request,'home.html',{'mess':mess})
    else:
        mess = 'Your log in details are invalid'
        return render(request,'home.html',{'mess':mess})
def article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        current_user = request.user.id
        current_user1 = request.user.username
        current = request.user.email
        print(current)
        article = articles(title=title,content=content,author=current_user,write=current_user1,email=current)
        article.save()
        mess = 'Article created'
        return render(request,'home.html',{'mess':mess})

from django.contrib.postgres.search import SearchVector, SearchQuery

def search(request):
    if request.method == 'POST':
        tk = request.POST['ccc']        
        queryset = articles.objects.annotate(search=SearchVector("title","content")).filter(search=SearchQuery(tk)) 
        return render(request,'home.html',{'articles':queryset})

def logout(request):
    django_logout(request)
    queryset = articles.objects.all()
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def my_post(request):
    current = request.user.id
    queryset = articles.objects.filter(author=current)
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

# Preventing link errors from happening------------------------------------------------------------------------------------------

def prevent_home_error(request):
    queryset = articles.objects.all()
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def prevent_mypost_error(request):
    current = request.user.id
    queryset = articles.objects.filter(author=current)
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def prevent_write_error(request):
    current = request.user.id
    if current == None:
     print(current)
     mess = 'You are not loged in'
     return render(request,'home.html',{'mess':mess})
    else:
        return render(request,'write.html')

def prevent_logpage_error(request):
    return render(request,'log.html')

def prevent_sign_error(request):
    return render(request,'sign.html')

def prevent_logout_error(request):
    django_logout(request)
    queryset = articles.objects.all()
    print(queryset)
    return render(request,'home.html',{'articles':queryset})

def prevent_article_error(request):
     if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        current_user = request.user.id
        current_user1 = request.user.username
        article = articles(title=title,content=content,author=current_user,write=current_user1)
        article.save()
        mess = 'Article created'
        return render(request,'home.html',{'mess':mess})

def prevent_sign_error(request):
     return render(request,'sign.html')

def prevent_log_error(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['pass']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        mess = 'You are now loged in'
        return render(request,'home.html',{'mess':mess})
    else:
        mess = 'Your log in details are invalid'
        return render(request,'home.html',{'mess':mess})

def prevent_save_error(request):
     if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            message = 'username taken'
            return render(request,'sign.html',{'mess':message})
        elif pass1 != pass2:
            message = 'password one is not equal to password two'
            return render(request,'sign.html',{'mess':message})
        else:
            user = User.objects.create_user(email=email,username=username,password=pass2)
            user.save()
            mess='Account created'
            return render(request,'home.html',{'mess':mess})