from django.shortcuts import render
from  django.http import  HttpResponse
# Create your views here.
# def homepage(request):
#     return render(request, 'homepage.html')
# def about(request):
#     return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
# def products(request):
#     return render(request, 'products.html')
# def search(request):
#     return render(request, 'search.html')
def homepage_view(args, kwargs):
    return HttpResponse ("<h1>Hello World!</h1>")