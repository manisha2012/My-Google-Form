# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import Form, Question, Option
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/GoogleForm/login")
            #return render_to_response('registration/login.html', RequestContext(request, {}))
            #return render(RequestContext(request), 'registration/login.html')
            #return render(request, 'registration/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def index(request):
    #if request.user.is_authenticated():
    form_list = Form.objects.all()
    #user = User.objects.get(pk=request.user)
    #form_list = user.Form_set.all()
    context = {'form_list': form_list, 'user': request.user}
    return render(request, 'GoogleForm/index.html', context)


@login_required
def formDetail(request, form_id):
    form = Form.objects.get(pk=form_id)
    ques_list = form.question_set.all().order_by('created_at')
    single_options_ques = []
    multiple_options_ques = []
    for ques in ques_list:
        quesObj = Question.objects.get(pk=ques.id)
        if ques.ques_type == 'SC':
            single_options = []
            single_options.append(ques.id)
            single_options.append(quesObj.option_set.all())
            single_options_ques.append(single_options)
        if ques.ques_type == 'MC':
            multiple_options = []
            multiple_options.append(ques.id)
            multiple_options.append(quesObj.option_set.all())
            multiple_options_ques.append(multiple_options)
    options = {'single_options': single_options_ques, 'multiple_options': multiple_options_ques}
    context = {'form': form, 'ques_list': ques_list, 'options': options}
    return render(request, 'GoogleForm/createForm.html', context)

@login_required
def createForm(request):
    return render(request, 'GoogleForm/createForm.html')

def saveForm(request):
    if request.method == 'POST':
        form_title = request.POST.get('form_title', '')
        form_desc = request.POST.get('form_description', '')
        ques_count = request.POST.get('ques_count', '')
        formObj = Form(form_title=form_title, form_description=form_desc, user=request.user, total_ques=ques_count)
        formObj.save()
        ques_count_int = int(ques_count)
        for count in range(1, ques_count_int+1):
            count_str = str(count)
            ques_title = request.POST.get('ques_title'+count_str, '')
            ques_type = request.POST.get('ques_type'+count_str, '')
            ques_obj = Question(ques_title=ques_title, ques_type=ques_type, form=formObj)
            ques_obj.save()
            if ques_type == 'SC':
                for opt_c in range(1,3):
                    opt_count = str(opt_c)
                    option_name = request.POST.get('option_single_'+count_str+'_'+opt_count, '')
                    option_obj = Option(ques=ques_obj, name=option_name)
                    option_obj.save()
            if ques_type == 'MC':
                for opt_c in range(1,5):
                    opt_count = str(opt_c)
                    option_name = request.POST.get('option_mul_'+count_str+'_' + opt_count, '')
                    option_obj = Option(ques=ques_obj, name=option_name)
                    option_obj.save()
        #option_name = request.POST.get('name', '')
        form_list = Form.objects.all()
        context = {'form_list': form_list}
        return render(request, 'GoogleForm/index.html', context)

def updateForm(request, form_id):
    form = Form.objects.get(pk=form_id)
    total_ques_earlier = int(form.total_ques)
    if request.method == 'POST':
        form_title = request.POST.get('form_title', '')
        form_desc = request.POST.get('form_description', '')
        ques_count = request.POST.get('ques_count', '')
        ques_count_int = int(ques_count)
        Form.objects.filter(id=form_id).update(form_title=form_title, form_description=form_desc, total_ques=ques_count)
        for count in range(1, total_ques_earlier+1):
            count_str = str(count)
            ques_id = request.POST.get('ques'+count_str, '')
            ques_id_int = int(ques_id)
            ques_title = request.POST.get('ques_title' + count_str, '')
            ques_type = request.POST.get('ques_type' + count_str, '')
            Question.objects.filter(id=ques_id_int).update(ques_title=ques_title)
            if ques_type == 'SC':
                for opt_c in range(1, 3):
                    opt_count = str(opt_c)
                    option_id = request.POST.get('optionSC'+count_str+ opt_count, '')
                    option_id_int = int(option_id)
                    option_name = request.POST.get('option_single_'+count_str+'_'+ opt_count, '')
                    Option.objects.filter(id=option_id_int).update(name=option_name)
            if ques_type == 'MC':
                for opt_c in range(1, 5):
                    opt_count = str(opt_c)
                    option_id = request.POST.get('optionMC'+count_str+opt_count, '')
                    option_id_int = int(option_id)
                    option_name = request.POST.get('option_mul_'+count_str+'_' + opt_count, '')
                    Option.objects.filter(id=option_id_int).update(name=option_name)
        for count in range(total_ques_earlier+1, ques_count_int+1):
            count_str = str(count)
            ques_title = request.POST.get('ques_title' + count_str, '')
            ques_type = request.POST.get('ques_type' + count_str, '')
            ques_obj = Question(ques_title=ques_title, ques_type=ques_type, form=form)
            ques_obj.save()
            if ques_type == 'SC':
                for opt_c in range(1, 3):
                    opt_count = str(opt_c)
                    option_name = request.POST.get('option_single_'+count_str+'_' + opt_count, '')
                    option_obj = Option(ques=ques_obj, name=option_name)
                    option_obj.save()
            if ques_type == 'MC':
                for opt_c in range(1, 5):
                    opt_count = str(opt_c)
                    option_name = request.POST.get('option_mul_'+count_str+'_' + opt_count, '')
                    option_obj = Option(ques=ques_obj, name=option_name)
                    option_obj.save()
        form_list = Form.objects.all()
        context = {'form_list': form_list}
        return render(request, 'GoogleForm/index.html', context)
    # Create your views here.
