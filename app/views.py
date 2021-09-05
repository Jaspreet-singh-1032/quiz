# django imports
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# models imports
from .models import (
    Quiz
)

class ListQuizView(LoginRequiredMixin,generic.ListView):
    template_name = 'app/list_quiz.html'
    def get_queryset(self):
        return Quiz.objects.filter(user = self.request.user).order_by('-created')
    context_object_name = 'quiz_list'