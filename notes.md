## Notes for python and projects

Virtual Env: seperate environments for separate projects.

source ./name/bin/activate


create apps within application.
create view file in apps
create urls.py

Request -> django urls.py -> blogs.url.py -> views.py -> things render.

python3 manage.py runserver

Templates: to render html without code repetition.

By default, django looks for templates subdirectory in each application.
Once blog-template is ready, add it to list of installed apps so django knows where to look for templates. Recommended place: apps.py -> setting.py module.

Go to django-project -> add class name  settings.py in INSTALLED apps names.

the way rendering happens is render(request, '<name of subdirectory inside the templates folder>/file.html', <parameter in the form of dictionary only>).

For jinja templates, {%%} -. code block for the posts, endif, endfor required for each end of block, and to access element use {{ post.title }} format to access element values.

Block is a section in base template that child sections can overwrite. {% block <name> %}{% endblock %}
extending done using: {% extends "<dir>/base.html" %}


To load static files, they must be placed in static/<appname>/<something.css/js> folder and base template must use the command {% load static %}. In the link rel stylesheet code, href = {% static 'blog/main.css' %} which generates a permalink for the path.

instead of hardcoding the href urls to point to specific pages in the website, use the syntax {% url '<route name>' %} where route name is defined in the urls.py file.



