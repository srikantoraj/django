from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ImgModel

# Create your views here.
def index(request):
    data = ImgModel.objects.all()
    context = {'items':data}
    return render(request,'Testimg/index.html',context)
# Create your views here.
def upload(request):
    if request.method == "POST":
        imageF = request.FILES['image']
        titleF = request.POST['title']
        allData = ImgModel(title = titleF, image=imageF)
        allData.save()
        return redirect('index')
    return render(request,'Testimg/upload.html')