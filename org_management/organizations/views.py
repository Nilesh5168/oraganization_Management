from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Organization, Role
from .forms import OrganizationForm, UserForm, RoleForm


def user_management(request):
    # Your logic here
    return render(request, 'user_management.html')  # or whatever template you want to render

def home(request):
    return render(request, 'home.html')

User  = get_user_model()

@login_required
def create_organization(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = OrganizationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('organizations:organization_list')
        else:
            form = OrganizationForm()
        return render(request, 'organizations/organization_form.html', {'form': form})
    return redirect('home')

@login_required
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations/organization_list.html', {'organizations': organizations})

@login_required
def manage_users(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    if request.user.organization == organization:
        users = User.objects.filter(organization=organization)
        return render(request, 'organizations/user_management.html', {'users': users, 'organization': organization})
    return redirect('home')

@login_required
def assign_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.organization == user.organization:
        if request.method == 'POST':
            form = RoleForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('organizations:manage_users', org_id=user.organization.id)
        else:
            form = RoleForm(instance=user)
        return render(request, 'organizations/assign_role.html', {'form': form})
    return redirect('home')