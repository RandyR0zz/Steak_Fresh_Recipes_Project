from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Author
from .forms import AddPost


def show_homepage(request):
    
    '''
    Function for rendering homepage. 
    '''
    
    return render(request, 'home.html')


def show_history_page(request):
    
    '''
    Function for rendering history_page.
    ''' 
    
    return render(request, 
                  'about_us.html')


def show_note(request, note=''):
    
    '''
    Function for rendering notice page in case of some mistakes or system warnings. 
    '''
    
    return render(request, 'note.html', 
                  {'note': note})


def show_all_posts(request):
    
    '''
    Function for rendering list of all moderated posts.
    Posts are order by issued.
    Including paginator for show number of pages 
    '''
    
    posts = Post.objects.filter(moderation=True).order_by('-issued')
    
    if posts.count() == 0:
        note = 'There is no any added recipes yet! Add your personal recipe first!'
        return show_note(request, note)

    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    
    try:
        all_posts = paginator.page(page_num)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    return render(request, 'posts.html', 
                      {'posts': all_posts})


def show_post(request, id):
    
    '''
    Function for rendering post ordered by id. 
    '''
    
    try:
        post = Post.objects.get(id=id)
        return render(request, 'post.html', {'post': post})
    except:
        note = 'Oh, sorry! We can`t find this post!'
        return show_note(request, note)


def initialize():
    
    '''Adding user if there are no users at all'''
    
    if Author.objects.all().count() == 0:
        Author.objects.create(username = 'User', mail = 'test@gmail.com')


def add_post(request):
    
    '''
    Function for adding posts to the data base by the POST method.
    Validates data. 
    Redirecting to the note page if not validated 
    '''
    
    initialize()
    
    if request.method == 'POST':
        new_form = AddPost(request.POST, request.FILES)

        if new_form.is_valid():
            post = Post()
            post.author = Author.objects.all()[0]
            post.title = new_form.cleaned_data["title"]
            post.content = new_form.cleaned_data["content"]
            post.recipe = new_form.cleaned_data["recipe"]
            post.save()
            note = 'Thank you! Your post has been sent on moderation. Please wait a while for our team to check it out with our moderators!'
            return show_note(request, note)
        else:
            note = 'Oh! Sorry! Something went wrong! You shouldn`t enter special symbols! Try again please!'
            return show_note(request, note)
        
    else:
        new_form = AddPost()
    return render(request, 
                  'add_post.html', {'new_form': new_form})