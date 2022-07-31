from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TeamMember

def list(request):
    team_members = TeamMember.objects.all().values()
    template = loader.get_template('list.html')
    context = {
        'team_members': team_members
    }
    return HttpResponse(template.render(context, request))

def add(request):
    roles = TeamMember.role.field.choices
    context = {
        'roles': roles
    }
    template = loader.get_template('add.html')
    return HttpResponse(template.render(context, request))

def add_save(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    role = request.POST['role']
    team_member = TeamMember(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, role=role)
    team_member.save()
    return HttpResponseRedirect(reverse('list'))

def edit(request, id):
    team_member = TeamMember.objects.get(id=id)
    roles = TeamMember.role.field.choices
    template = loader.get_template('edit.html')
    context = {
        'team_member': team_member,
        'roles': roles
    }
    return HttpResponse(template.render(context, request))

def edit_save(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    role = request.POST['role']
    team_member = TeamMember.objects.get(id=id)
    team_member.first_name = first_name
    team_member.last_name = last_name
    team_member.email = email
    team_member.phone_number = phone_number
    team_member.role = role
    team_member.save()
    return HttpResponseRedirect(reverse('list'))

def edit_delete(_, id):
    team_member = TeamMember.objects.get(id=id)
    team_member.delete()
    return HttpResponseRedirect(reverse('list'))
