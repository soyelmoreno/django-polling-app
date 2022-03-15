from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
# from django.template import loader

from .models import Question

# Each view is responsible for doing one of two things: returning an
# HttpResponse object containing the content for the requested page, or raising
# an exception such as Http404. The rest is up to you.

# Your view can read records from a database, or not. It can use a template
# system such as Django's – or a third-party Python template system – or not. It
# can generate a PDF file, output XML, create a ZIP file on the fly, anything
# you want, using whatever Python libraries you want. All Django wants is that
# HttpResponse. Or an exception.

def index(request):
    # Version 1: very simple
    # return HttpResponse("Hello, world. You're at the polls index.")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    # Version 2:
    # Could join into a comma-separated array and just return that:
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # Version 3:
    # Load a template file, call its render() method with the context
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # Version 4:
    # Use the `render` shortcut (now we don't need `loader` or `HttpResponse`)
    return render(request, 'polls/index.html', context)


def wow(request):
    return HttpResponse("Wow, it works. You're at the polls Wow page.")

def detail(request, question_id):
    # Version 1: very simple
    # return HttpResponse("You're looking at question %s." % question_id)

    # Version 2:
    # Use the `render` shortcut to render the template with the context
    # And raise an exception if that question id doesn't exist.
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # Version 3:
    # Use the `get_object_or_404` shortcut to do all of that, then render.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
