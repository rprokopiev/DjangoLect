from django.shortcuts import render
import logging
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User
from django.core.files.storage import FileSystemStorage


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # doing something
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})


# def many_fields_form(request):
#     if request.method == 'POST':
#         form = ManyFieldsForm(request.POST)
#         if form.is_valid():
#             # doing something
#     else:
#         form = ManyFieldsForm()

#     return render(request, 'myapp4/many_fields_form.html', {'form': form})


def many_fields_form(request):
    
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            pass
    else:
        form = ManyFieldsFormWidget()

    return render(request, 'myapp4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'User saved'
    else:
        form = UserForm()
        message = 'Заполни форму'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})
