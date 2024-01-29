from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Query
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
