from django.shortcuts import render
from library_app.forms import AuthorForm, BookForm
from datetime import date

from django.contrib.auth.decorators import login_required

# Create your views here.
my_dict = {"insert_content":"Hello I'm from First App", "my_date":date.today()}

@login_required
def NewAuthor(request):
    form = AuthorForm()

    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,"first_app/index.html",my_dict)
        else:
            print("Error from Author Form")

    return render(request, "library_app/author.html", {"form":form})

@login_required
def NewBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,"first_app/index.html",my_dict)
        else:
            print("Error from Book Form")

    return render(request, "library_app/book.html", {"form":form})
