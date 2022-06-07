from unicodedata import name
from django.shortcuts import render, redirect
from matplotlib.pyplot import title  
from bookEntry.forms import bookForm  
from bookEntry.models import BookEntry  
# Create your views here.  
def index(request):  
    if request.method == "POST":  
        form = bookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/retrieve')  
            except:  
                pass  
    else:  
        form = bookForm()  
    return render(request,'enterbookDetails.html',{'form':form}) 

def retrieve(request):  
    books = BookEntry.objects.all()  
    return render(request,"retrieve.html",{'books':books})   

def edit(request,id):  
    editBook = BookEntry.objects.get(id=id)  
    return render(request,'edit.html', {'book':editBook})  

def update(request, id):  
    book = BookEntry.objects.get(id=id)  
    form = bookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/retrieve")  
    return render(request, 'edit.html', {'book': book})  

def destroy(request, id):  
    book = BookEntry.objects.get(id=id)  
    book.delete()  
    return redirect("/retrieve") 

def home(request):
    books = BookEntry.objects.all()  
    return render(request,"index.html",{'books':books})

def bbybookname(request):
    return render(request,"bbybookname.html")

def bbybarcode(request):
    return render(request,"bbybarcode.html")

def bbyauthor(request):
    return render(request,"bbyauthor.html")

def searchbyauthor(request):
    if request.method == "POST":
        author = request.POST.get('searchByAuthor') 
    booksByauthor = BookEntry.objects.all().filter(author=author)
    return render(request,"bbyauthor.html",{'books':booksByauthor})

def searchbybookname(request):
    if request.method == "POST":
        bookname = request.POST.get('searchByBookName')
    booksBytitle = BookEntry.objects.all().filter(title=bookname)
    return render(request,"bbyauthor.html",{'books':booksBytitle})

def searchbybarcode(request):
    if request.method == "POST":
        code = request.POST.get('searchByCode')
    booksBycode = BookEntry.objects.all().filter(code = code)
    return render(request,"bbyauthor.html",{'books':booksBycode})
