from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post,Aboutus
from django.core.paginator import Paginator
from .forms import *


# posts = [
#         {'id':1,"title":'post 1', 'content': 'Content of Post 1'},
#         {'id':2,"title":'post 2', 'content': 'Content of Post 2'},
#         {'id':3,"title":'post 3', 'content': 'Content of Post 3'},
#         {'id':4,"title":'post 4', 'content': 'Content of Post 4'}
#     ]


def index(request):
    blog_title = "Recent Posts"
    #getting data from post model
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'blog_title':blog_title, 'page_obj':page_obj})

def detail(request, slug):

    #  static data
    # post = next((item for item in posts if item['id'] == post_id),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')

    try:
    #getting data from model by id
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
    return render(request, 'details.html',{'post':post, 'related_posts':related_posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
            success_message = 'Your Email has been sent'
            return render(request,'contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request, "contact.html", {"form":form, "name":name, "email":email, "message":message})
    return render(request, "contact.html")

def about_view(request):
    about_content = Aboutus.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default content goes here."  # Replace with your desired default string
    else:
        about_content = about_content.content

    return render(request, 'about.html',{'about_content':about_content})