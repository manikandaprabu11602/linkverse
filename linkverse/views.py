from django.shortcuts import render
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import LinkCategory, Link
from .forms import LinkCategoryForm, LinkForm
from django.contrib.auth.decorators import login_required

def guest_home(request):
    return render(request, 'linkverse/guest_home.html')

def creator_dashboard(request):
    # Get the total number of links and categories for the logged-in user
    total_links = Link.objects.filter(user=request.user).count()
    total_categories = LinkCategory.objects.filter(user=request.user).count()
    
    # Get the most recent 10 links for the logged-in user
    recent_links = Link.objects.filter(user=request.user).order_by('-created_at')[:10]

    context = {
        'total_links': total_links,
        'total_categories': total_categories,
        'recent_links': recent_links
    }

    return render(request, 'linkverse/creator_dashboard.html', context)

def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('creator_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'linkverse/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('guest_home') 

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            creator_group = Group.objects.get(name='creator')
            user.groups.add(creator_group)
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'linkverse/signup.html', {'form': form})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = LinkCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user  # Set created_by to the logged-in user
            category.user = request.user       # Set user to the logged-in user as well
            category.save()
            return redirect('category_list')  # Redirect to the category list page
    else:
        form = LinkCategoryForm()
    return render(request, 'linkverse/category/create_category.html', {'form': form})

@login_required
def category_list(request):
    categories = LinkCategory.objects.all()
    return render(request, 'linkverse/category/category_list.html', {'categories': categories})

@login_required
def update_category(request, pk):
    category = get_object_or_404(LinkCategory, pk=pk)
    if request.method == 'POST':
        form = LinkCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            # Ensure the created_by and user fields stay as the original values
            category.created_by = category.created_by  # Keep the original created_by value
            category.user = category.user  # Keep the original user value
            category.save()
            return redirect('category_list')
    else:
        form = LinkCategoryForm(instance=category)

    return render(request, 'linkverse/category/update_category.html', {'form': form})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(LinkCategory, pk=pk)
    category.delete()
    return redirect('category_list')

@login_required
def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES)
        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.user = request.user
            link.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'linkverse/links/create_link.html', {'form': form})


@login_required
def link_list(request):
    links = Link.objects.all()
    return render(request, 'linkverse/links/link_list.html', {'links': links})

@login_required
def update_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, request.FILES, instance=link)
        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = link.created_by
            link.user = link.user
            link.save()
            return redirect('link_list')
    else:
        form = LinkForm(instance=link)
    return render(request, 'linkverse/links/update_link.html', {'form': form})


@login_required
def delete_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    link.delete()
    return redirect('link_list')
