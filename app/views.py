
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Note
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def Create_List(request):
    if request.method == 'POST':
        Note1= request.POST.get('List')
        Create_Data = Note.objects.create(Notes=Note1)
        return redirect('Show_data')
    
def Show_page(request):
    return render(request, 'app/show.html')
    
def Show_data(request): 
    Note_data = Note.objects.all()
    return render(request, 'app/show.html', {'Key': Note_data})

def Delete_Data(request,pk):
    Notes = Note.objects.get(id=pk)
    Notes.delete()
    return redirect('Show_data')

def update_page(request, pk):
    update = get_object_or_404(Note, pk=pk)
    return render(request, "app/edit.html", {"update": update})

def update_data(request, pk):
    update_data = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        update_data.Notes = request.POST.get("List")
        update_data.save()
    return redirect('Show_data')
    