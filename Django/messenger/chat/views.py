from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from chat import models
from django.shortcuts import redirect
from django.db import connection
import datetime
from django.http import JsonResponse
from django.core.serializers import serialize

# Create your views here.


def check_loggin_decorator(func):    
    def wraper(request, **kwargs):
        if 'logged' not in request.session:
            return redirect("login_view")
        if func.__name__ == 'chat_view': 
            return func(request,kwargs['group_id']) 
        if func.__name__ == 'get_group_id_by_friend_id': 
            return func(request,kwargs['friend_id']) 

        return func(request)
    return wraper

def login_view(request):
    if 'logged' not in request.session:
        return render(request,"users/login.html")
    else:
        return redirect("chat_view",group_id = 0)

def sign_out(request):
    user = models.users.objects.get(pk=request.session['logged']['id'])      
    user.status = 0
    user.save()
    del request.session['logged']
    return redirect("login_view")

def login(request):
    user = models.users.objects.filter(name=request.POST["name"],pwd= request.POST["pwd"])

    if not user.count():
        context = {'message':"Invalid information"}
        return render(request,"users/login.html",context)
    else:
        context = {'message':f"Hello, {request.POST['name']}"}
        user= user.first() 
        user.status = 1
        user.save()
        request.session['logged'] = {'id':user.id,'name':user.name}



        # return render(request,"mess/index.html",context)
        return redirect("login_view")
    
def gen_context_for_chat(request,group_id):
    ss = request.session['logged']
    mems = models.members.objects.filter(id_user = ss['id'] ).values('id_group')
    groups = []
    ids_of_groups = list(i['id_group'] for i in  list(mems)  ) 
    groups = models.group.objects.filter(pk__in=ids_of_groups).order_by("-updated")
    messengers = []            
    messengers = models.messengers.objects.filter(id_group = group_id).order_by("date")
    current_id = 0
    try:
        group = models.group.objects.get(pk = group_id)
        mem = models.members.objects.filter(id_group =group_id , id_user = ss['id'])
        if not mem.count():
            messengers = []
        else:
            current_id = mem.first().id
    except:
        group = {}
    context = {'name':ss['name'],"current_id":current_id,"groups":groups,"messengers":messengers ,'group':group}
    return context
@check_loggin_decorator
def chat_view(request,group_id):
    # ss = request.session['logged']
    # mems = models.members.objects.filter(id_user = ss['id'] ).values('id_group')
    # groups = []
    # ids_of_groups = list(i['id_group'] for i in  list(mems)  ) 
    # groups = models.group.objects.filter(pk__in=ids_of_groups).order_by("-updated")
    # messengers = []            
    # messengers = models.messengers.objects.filter(id_group = group_id).order_by("-date")
    # current_id = 0
    # try:
    #     group = models.group.objects.get(pk = group_id)
    #     mem = models.members.objects.filter(id_group =group_id , id_user = ss['id'])
    #     if not mem.count():
    #         messengers = []
    #     else:
    #         current_id = mem.first().id
    # except:
    #     group = {}
    # context = {'name':ss['name'],"current_id":current_id,"groups":groups,"messengers":messengers,'group':group}
    context = gen_context_for_chat(request,group_id)
    return render(request,"mess/index.html",context)    

def refresh_data(request , group_id):
    # data = {'content': 'This is the updated content!'}  # Example data
    context = gen_context_for_chat(request,group_id)
    lst = []
    for row in context['messengers']:
        lst.append({'content':row.content,'date':row.date , 'sender': row.sender_id.id_user.name,'id_sender': row.sender_id.id })        
    # data = ["Item 1 (updated)", "Item 2 (updated)", "Item 3 (updated)"]  # Example data
    return JsonResponse({'mess':lst})
    # return JsonResponse(context)

def send_mess(request,group_id):
    ss = request.session['logged']
    group = models.group.objects.get(pk=group_id )
    mem = models.members.objects.filter(id_group = group_id, id_user = ss['id']).first()
    if mem.DoesNotExist():
        m = models.messengers(content = request.POST['message'],sender_id =mem, date =datetime.datetime.now(), id_group =  group )
        m.save()
        group.updated = datetime.datetime.now()
        group.save()


        return redirect("chat_view",group_id =group_id )
    else:
        return HttpResponse("no found")

  

# @check_loggin_decorator
# def get_group_id_by_friend_id(request,friend_id):
#     ss = request.session['logged']
#     with connection.cursor() as cursor:
#         query = f'''
#             select t1.id_group_id 
#             from ( select * from chat_members WHERE id_user_id = {friend_id}) t1 
#             inner join
#             ( select * from chat_members WHERE id_user_id = {ss['id']}) t2
#             on t1.id_group_id = t2.id_group_id
#         '''
#         print(query)
#         cursor.execute(query)  # Escape user input with f-string
#         results = cursor.fetchall()
#         next_group_id = results[0][0] if  results else 0 
#         return redirect("chat_view",group_id = next_group_id ) 


        # print(results[0][0])
    # return render(request,"users/add.html")    