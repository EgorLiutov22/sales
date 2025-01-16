from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render, redirect
from django.contrib import messages

from .form import CustomerForm
from .models import Customer


def index(request):
    template = loader.get_template("sales/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = Customer()
            customer.name = form.fields['name']
            customer.lastname = form.fields['lastname']
            customer.phone = form.fields['phone']
            customer.email = form.fields['email']
            customer.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('blog-home')
    else:
        form = CustomerForm()
    return render(request, 'users/register.html',
                  get_context({'form': form}))


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context