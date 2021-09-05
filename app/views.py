# django imports
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# models imports
from .models import (
    Quiz
)

class ListQuizView(LoginRequiredMixin,generic.ListView):
    template_name = 'app/list_quiz.html'
    def get_queryset(self):
        return Quiz.objects.filter(user = self.request.user).order_by('-created')
    context_object_name = 'quiz_list'

class QuizPageView(generic.DetailView):
    template_name = 'app/quiz_page.html'
    context_object_name = 'quiz'

    def get_object(self ):
        quiz = get_object_or_404(Quiz.objects.select_related('user'), pk=self.kwargs.get('pk'))
        return quiz
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = context['quiz'].questions.all()
        return context
    
    