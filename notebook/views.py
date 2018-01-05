from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponseRedirect, resolve_url

from notebook import models


def notes(request):

    qs = models.Note.objects.filter().order_by('-creation_date')

    context = {}

    if request.method == "GET":
        data = request.GET
        if 'search' in data:
            context['search'] = data['search']
            qs = qs.filter(content__icontains=data['search'])

    paginator = Paginator(qs, 10)

    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        qs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        qs = paginator.page(paginator.num_pages)

    context['notes'] = qs

    return render(request, 'notebook/notes.jade', context)


def create(request):

    data = request.POST

    if 'content' in data:
        models.Note.objects.create(content=data['content'])

    return HttpResponseRedirect(resolve_url('notes'))


def update(request):

    data = request.POST
    note_id = data['id']

    models.Note.objects.filter(id=note_id).update(
        content=data['content'])

    return HttpResponseRedirect("{}#note-{}".format(
        resolve_url('notes'), note_id))


def delete(request, note_id):

    models.Note.objects.filter(id=int(note_id)).delete()

    return HttpResponseRedirect(resolve_url('notes'))

def archive(request, note_id):

    models.Note.objects.filter(id=int(note_id)).update(archived=True)

    return HttpResponseRedirect(resolve_url('notes'))
