from django.shortcuts import render,redirect
from django.views import View
from .models import Books
from .forms import BookForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    
class Addbook(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'addbook.html', {'form': form})
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid:
            title=request.POST.get("title")
            author=request.POST.get("author")
            description=request.POST.get("description")
            status=request.POST.get("status")
            Books.objects.create(title=title,author=author,description=description,status=status)
            messages.success(request,"Book added successfully")
            return redirect('home_view')
        else:
            messages.MessageFailure(request,"invalid form")
            return redirect('add_view')
        

class Listbooks(View):
    def get(self, request,*args,**kwargs):
        book = Books.objects.all()
        return render(request, 'booklist.html',{'book':book})
    
class Deletebook(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        book = Books.objects.get(id=id)
        book.delete()
        return redirect('list_view')

class Editbook(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        form=BookForm(instance=book)
        return render(request, 'edit.html',{'form':form})
    def post(self, request, *args, **kwargs):
        title=request.POST.get("title")
        author=request.POST.get("author")
        description=request.POST.get("description")
        status=request.POST.get("status")
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        book.title=title
        book.author=author
        book.description=description
        book.status=status
        book.save()
        return redirect('list_view')
        

