from django.http import HttpResponse
from django.shortcuts import render
#from .models import Iphone

# Create your views here.


def index(request):
    #iphone = Iphone.objects.all()
    return render(request, 'general/index.html')
    #return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})




'''res = '<h1>список новостей</h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
    return HttpResponse(res)'''