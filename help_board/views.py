from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Query, Answer
from .forms import AnswerForm

# Create your views here.


class QueryList(generic.ListView):
    queryset = Query.objects.all().order_by("created_on")
    template_name = "qna_board/index.html"
    paginate_by = 2


def query_detail(request, slug):
    """
    Display an individual :model:`help_board.Query`.

    **Context**

    ``Query``
        An instance of :model:`help_board.Query`.

    **Template:**

    :template:`qna_board/query_detail.html`
    """

    queryset = Query.objects.filter(status=1)
    query = get_object_or_404(queryset, slug=slug)
    answers = query.query_asked.all().order_by("-created_on")
    answer_count = query.query_asked.filter(approved=True).count()

    if request.method == "POST":
        answer_form = AnswerForm(data=request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.author = request.user
            answer.query = query
            answer.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Answer submitted and awaiting approval'
            )

    answer_form = AnswerForm()

    return render(
        request,
        "qna_board/query_detail.html",
        {
            "query": query,
            "answers": answers,
            "answer_count": answer_count,
            "answer_form": answer_form
        },

    )


def answer_edit(request, slug, answer_id):
    """
    view to edit Answers
    """
    if request.method == "POST":

        queryset = Query.objects.filter(status=1)
        query = get_object_or_404(queryset, slug=slug)
        answer = get_object_or_404(Answer, pk=answer_id)
        answer_form = AnswerForm(data=request.POST, instance=answer)

        if answer_form.is_valid() and answer.author == request.user:
            answer = answer_form.save(commit=False)
            answer.query = query
            answer.approved = False
            answer.save()
            messages.add_message(request, messages.SUCCESS, 'Answer Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating Answer!')

    return HttpResponseRedirect(reverse('query_detail', args=[slug]))


def answer_delete(request, slug, answer_id):
    """
    view to delete answer
    """
    queryset = Query.objects.filter(status=1)
    query = get_object_or_404(queryset, slug=slug)
    answer = get_object_or_404(Answer, pk=answer_id)

    if answer.author == request.user:
        answer.delete()
        messages.add_message(request, messages.SUCCESS, 'Answer deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own answers!')

    return HttpResponseRedirect(reverse('query_detail', args=[slug]))
