from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Query

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

    return render(
        request,
        "qna_board/query_detail.html",
        {
            "query": query,
            "answers": answers,
            "answer_count": answer_count,
        },
        
    )
