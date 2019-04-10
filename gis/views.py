from django.shortcuts import render,redirect
from gis.models import Marker
from django.http import JsonResponse
# Create your views here.

def index(request):
    #return render(request,'gis/indexbaiduapi.html')
    return render(request,'gis/map.html',{'enableGetPoint':0})

def add_marker1(request):
    return render(request,'gis/form_basic.html')

def add_marker2(request):
    return render(request,'gis/right.html',{'enableGetPoint':1})
    
def add_matker_ajax(request):
    result = {'status':"True",'message':''}
    if request.method == 'POST':
        marker = {
            'title': request.POST.get('title'),
            'lng':request.POST.get('lng'),
            'lat':request.POST.get('lat'),
            'content':request.POST.get('content')
        }
        Marker.objects.create(**marker)
        result['message'] = 'add success'    
    else :
        result['status'] = "False"
        result['message'] = 'only method post'
        
    return JsonResponse(result,safe=False)    

def ajax_get_marker_list(request):
    markers = Marker.objects.all()#取出所有的marker
    marker = []
    for _ in markers:
        dict_of_marker = {}
        dict_of_marker['title'] = _.title
        dict_of_marker['lng'] = _.lng
        dict_of_marker['lat'] = _.lat
        dict_of_marker['content'] = _.content
        marker.append(dict_of_marker)
    return JsonResponse(marker,safe=False)

def search(request):
    return render(request,'gis/search.html')

def ajax_search(request):
    title = request.POST.get('title')
    result = {'status':"False",}
    try:
        result_set = Marker.objects.get(title=title)
    except Exception:
        result_set = None
        print('查找失败')
    if result_set is not None:
        result["status"] = "True"
        result["title"] = result_set.title
        result["lng"] = result_set.lng
        result['lat'] = result_set.lat
        result["content"] = result_set.content        
    return JsonResponse(result,safe=False)
def route_plan(request):
    return render(request,'gis/route_plan.html')
def data_admin(request):
    markers = Marker.objects.all()
    counts = len(markers)
    content = {"markers":markers,'counts':counts}
    return render(request,'gis/admin.html',content)
    
def edit(request):
    result = {"status":"False","message":''}
    if request.method == 'POST':
        title = request.POST.get("title")
        lng = request.POST.get("lng")
        lat = request.POST.get("lat")
        content = request.POST.get("content")
        m_id = request.POST.get("id")
        try:
            marker = Marker.objects.get(id=m_id)
            marker.title = title
            marker.lng = lng
            marker.lat = lat
            marker.content = content
            marker.save()
        except Exception:
            result["message"] = "更新数据库失败"
        result["status"] = "True"
        
    else:
        result["message"] = "only POST"
        
    return JsonResponse(result,safe=False)

def edit_page(request,id):
    marker = Marker.objects.get(id=id)
    content = {"marker":marker}
    return render(request,'gis/edit.html',content)
    
def delete(request,id):
    try:
        Marker.objects.get(id=id).delete()
    except Exception :
        #result['msg'] = "删除失败"
        print("删除失败")    
    return redirect("gis:data_admin")
    
def admin_search(request):
    title = request.GET.get('search')
    try :
        marker = Marker.objects.get(title=title)
    except Exception:
        markers = None
        counts = 0
    markers=[]
    markers.append(marker)
    counts = 1
    content = {'markers':markers,"counts":counts}
    return render(request,'gis/admin.html',content)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
