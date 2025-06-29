from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# We're using two generic views here: ListView and DetailView. Respectively,
# those two views abstract the concepts of "display a list of objects" and
# "display a detail page for a particular type of object."

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


###########################

# For learning, we first wrote the index, detail, and results views this way:

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

    # Note: There's also a get_list_or_404() function, which works just as
    # get_object_or_404() – except using filter() instead of get(). It raises
    # Http404 if the list is empty.

def results(request, question_id):
    # Version 1: very simple
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question })

def vote(request, question_id):
    # Version 1: very simple
    # return HttpResponse("You're voting on question %s." % question_id)

    # Version 2: handle the submitted form
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        # POST data. This prevents data from being posted twice if a user hits
        # the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
