from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from products import models
# from django.template import loader
logged  = True
def check_loggin_decorator(func):
    def wrapper(request):
        if not logged:
            return HttpResponse("not logged in")
        return func(request)

    return wrapper
@check_loggin_decorator
def index(request):
    products = models.products.objects.all()
    context = {"products":products}

    #render(request, template_name-> name of html file NOT PATH, context-> data needs to be passed as a dictionary   ) 
    return render(request,"index.html",context)
    # return HttpResponse(products)
    # return HttpResponse("Hello, world. You're at the  index.")

def add_view(request):
    return render(request,"add.html")
    # return HttpResponse([1,2,3])
def submit_add(request):
    rsl = request.POST["param"]    
    return HttpResponse(rsl)


def detail(request, id):
    try:
        product = models.products.objects.get(pk=id)
    except models.products.DoesNotExist:
        return   HttpResponse("not found")
    # product = get_object_or_404(models.products,pk=id)
    context = {'product':product}
    return render(request,"detail.html",context)
    # return HttpResponse(product.name)
