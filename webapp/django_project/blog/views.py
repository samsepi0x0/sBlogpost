from django.shortcuts import render

# dummpy data for the webapp

posts = [
    {
        'author' : 'samsepi0x0',
        'title' : 'First Blog post',
        'content' : 'content for the first blog post.',
        'date' : 'June 25th'
    }, 
    {
        'author' : 'John Doe',
        'title' : 'Second Blog post',
        'content' : 'content for the second blog post.',
        'date' : 'June 20th' # ideally a datetime object.
    }
]


def home(request):
    context = {
        'posts' : posts 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'}) 
