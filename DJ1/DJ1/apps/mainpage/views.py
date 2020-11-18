from django.shortcuts import render
from django.apps import apps
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
Subject = apps.get_model('subjects', 'Subject')
Task = apps.get_model('subjects', 'Task')
import datetime
def index(request):
    subjects = Subject.objects.all()
    tasks = Task.objects.all()
    return render(request, 'main/mainpage.html', {'subjects' : subjects, 'tasks' : tasks})

def leave_task(request):
    subject = request.POST['subject']
    text = request.POST['text']
    if subject == 'Economics':
        task = Economics(task_text = text)
        task.save()
    elif subject == "IT":
        task = IT(task_text = text)
        task.save()
    return HttpResponseRedirect(reverse('mainpage:index'))
    # a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    # return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))

@csrf_exempt
def leave_task_ajax(request):
    if request.is_ajax():
        subject = request.POST['subject']
        text = request.POST['text']
        date = request.POST['date']
        s = Subject.objects.get(subject_name = subject)
        s.task_set.create(task_text = text, expire = date)
    else:
        message = "Bad request!"
    data_to_response = {
        'task_text' : text,
        'subject' : subject,
        's' : s
    }
    return HttpResponse(data_to_response)
def educators(request):
    return render(request, 'main/educators.html')