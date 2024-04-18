from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlatformForm, RecordTypeForm, RecordForm, AccountForm, PostForm
from .models import Platform, RecordType, Account, Record

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os, base64


def index(request):
    return HttpResponse("Hello, world. I am your asset manager!")

def add_platform(request):
    if request.method == "POST":
        form = PlatformForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_platform.html', {})
    else:
        return render(request, 'add_platform.html', {})


def add_record_type(request):
    if request.method == "POST":
        form = RecordTypeForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_record_type.html', {})
    else:
        return render(request, 'add_record_type.html', {})




def add_record(request):
    platforms = Platform.objects.all()
    types = RecordType.objects.all()
    if request.method == "POST":
        # Get the thumbnail data from the request.POST dictionary
        thumbnail_data = request.POST.get('thumbnail')
        # Convert Base64 data to binary image data
        thumbnail_binary_data = base64.b64decode(thumbnail_data.split(",")[1])

        # Create a file path for the thumbnail image
        thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'thumbnails', 'thumbnail.jpg')
        
        # Save the binary image data to a file
        with open(thumbnail_path, 'wb') as f:
            f.write(thumbnail_binary_data)

        # Get other form data
        form = RecordForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form data, including the path to the thumbnail image
            model_instance = form.save(commit=False)
            model_instance.thumbnail = os.path.relpath(thumbnail_path, settings.MEDIA_ROOT)
            model_instance.save()
#            return redirect('success_url')  # Redirect to a success page
    else:
        form = RecordForm()
    return render(request, 'add_record.html', {'form': form, 'platforms': platforms, 'types': types})



'''

def add_record(request):
    platforms = Platform.objects.all()
    types = RecordType.objects.all()
    if request.method == "POST":
        #Get the file_name from the hidden field in html and store it in the model
#        file_name = request.POST.get('hiddenName')
        
        # Get the file object from the request
        file = request.POST.get('thumbnail')
        
        print(file)
        
        # Get the file name from the request.POST dictionary
        file_name = request.POST.get('fileName')

        # Save the uploaded file to the media storage
        file_path = default_storage.save(f'{settings.MEDIA_ROOT}/{file_name}', ContentFile(file.read()))
        
        # Construct the URL of the saved image
        thumbnail_url = default_storage.url(file_path)
 
         # Get the thumbnail image URL from the request.POST dictionary
 #       thumbnail_url = request.POST.get('thumbnail')

#        print(file)
        print(file_name)
        print(thumbnail_url)
       
        form = RecordForm(request.POST, request.FILES)
        model_instance = form.save(commit=False)
        model_instance.file_name = file_name
        model_instance.thumbnail.url = thumbnail_url

        if form.is_valid():
            model_instance.save()

        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})
    else:
        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})

'''




def add_account(request):
    platforms = Platform.objects.all()
    if request.method == "POST":
        form = AccountForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_account.html', {'platforms':platforms})
    else:
        return render(request, 'add_account.html', {'platforms':platforms})


def add_post(request):
    accounts = Account.objects.all()
    records = Record.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'add_post.html', {'accounts': accounts, 'records': records})
    else:
        return render(request, 'add_post.html', {'accounts': accounts, 'records': records})


