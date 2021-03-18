from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Category, Entry
from .forms import CategoryForm, EntryForm

# Create your views here.


def index(request):
    # Home page
    return render(request, 'xlogs/index.html')

@login_required 

def categories(request):
    #show all categories
    categories = Category.objects.filter(owner=request.user).order_by('date_added')
    context = {'categories':categories}
    return render(request,'xlogs/categories.html', context)

@login_required

def category(request, category_id):
    #Show a single category and all entries
    category = Category.objects.get(id=category_id)
    # Make sure the category belongs to current user
    if category.owner != request.user:
        raise Http404
    entries = category.entry_set.order_by('-date_added')
    context = {'category': category, 'entries': entries}
    return render(request, 'xlogs/category.html', context)


@login_required

def new_cat(request):
    if request.method != 'POST':
        #No data submitted; create blank form
        form = CategoryForm()
    else:
        #POST data submitted; process data
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return HttpResponseRedirect(reverse('xlogs:categories'))

    context = {'form':form}
    return render(request, 'xlogs/new_cat.html',context) 

@login_required

def new_entry(request, category_id):
    #Add a new entry for a particular category
    category = Category.objects.get(id=category_id)

    if request.method != 'POST':
        #No data submitted;create blank form
        form = EntryForm()
    else:
        #POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.category = category
            new_entry.save()
            return HttpResponseRedirect(reverse('xlogs:category', args=[category_id])) 

    context = {'category':category, 'form':form} 
    return render(request, 'xlogs/new_entry.html', context) 

@login_required

def edit_entry(request, entry_id):
    #Edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    category = entry.category
    if category.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request: pre fill form with current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('xlogs:category',args=[category.id]))

    context = {'entry':entry, 'category':category, 'form':form}
    return render(request,'xlogs/edit_entry.html', context)

