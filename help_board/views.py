# Importing libraries required to build views

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Query, Answer, Category
from .forms import QueryForm, AnswerForm


# Created CategoryList generic view that renders all info of category model
class CategoryList(generic.ListView):
    queryset = Category.objects.all().order_by("title")
    template_name = "qna_board/index.html"


# Created queries view that renders all info from category and query model
def queries(request, slug):
    """
    Display an individual :model:`help_board.Query`.

    **Context**

    ``Query``
        An instance of :model:`help_board.Query`.

    **Template:**

    :template:`qna_board/queries.html`
    """

    queryset = Category.objects.all()
    categories = queryset.values(
        "title", "slug", "fontawesome_icon"
    ).order_by("title")
    category = get_object_or_404(queryset, slug=slug)
    queries = category.query_category.all().order_by("-created_on")
    queries_count = category.query_category.filter(status=1).count()

    return render(
        request,
        "qna_board/queries.html",
        {
            "categories": categories,
            "category": category,
            "queries": queries,
            "queries_count": queries_count
        },
    )


# Created ask_query view that renders all info of query model
def ask_query(request):
    """
    Input info to model:`help_board.Query`.

    **Context**

    ``Query``
        An instance of :model:`help_board.Query`.

    **Template:**

    :template:`qna_board/ask_query.html`
    """

    if request.method == "POST":
        query_form = QueryForm(data=request.POST)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.author = request.user
            query.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Query submitted and awaiting approval'
            )

    query_form = QueryForm()

    return render(
        request,
        "qna_board/ask_query.html",
        {
            "query_form": query_form
        },
    )


# Created query_detail view that renders all info from query and answer model
def query_detail(request, slug):
    """
    Display's multiple models:`help_board.Query` & `help_board.Answer`.

    **Context**

    ``Query``
        An instance of models:`help_board.Query` & `help_board.Answer`.

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


# Created answer_edit view that renders info of
# answer model and helps edit the existing answer
def answer_edit(request, slug, answer_id):
    """
    View to edit records of a model.

    **Context**

    ``Query``
        An instance of models: `help_board.Answer`.
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


# Created answer_delete view that renders info of
# answer model and helps delete the existing answer
def answer_delete(request, slug, answer_id):
    """
    View to delete records in a model.

    **Context**

    ``Query``
        An instance of models: `help_board.Answer`.
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


# Created query_delete view that renders info of
# query model and helps delete the existing query
def query_delete(request, slug, query_id):
    """
    View to delete records in a model.

    **Context**

    ``Query``
        An instance of models: `help_board.Query`.
    """
    queryset = Category.objects.all()
    category = get_object_or_404(queryset, slug=slug)
    query = get_object_or_404(Query, pk=query_id)

    if query.author == request.user:
        query.delete()
        messages.add_message(request, messages.SUCCESS, 'Query deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own queries!')

    return HttpResponseRedirect(reverse('queries', args=[slug]))
