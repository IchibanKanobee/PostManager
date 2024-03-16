from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlatformForm, RecordTypeForm, RecordForm, AccountForm, PostForm
from .models import Platform, RecordType, Account, Record


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
        #Get the file_name from the hidden field in html and store it in the model
        file_name = request.POST.get('hiddenName')
        form = RecordForm(request.POST, request.FILES)
        model_instance = form.save(commit=False)
        model_instance.file_name = file_name

        if form.is_valid():
            model_instance.save()

        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})
    else:
        return render(request, 'add_record.html', {'platforms':platforms, 'types':types})


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


