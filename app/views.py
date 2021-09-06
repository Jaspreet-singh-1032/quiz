# django imports
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import HttpResponse

# models imports
from .models import (
    Quiz
)

# forms import
from .forms import (
    AnswerForm
)

class ListQuizView(LoginRequiredMixin,generic.ListView):
    template_name = 'app/list_quiz.html'
    context_object_name = 'quiz_list'
    
    def get_queryset(self):
        return Quiz.objects.values('id','name').filter(user = self.request.user).order_by('-created')

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
    
class ResultView(View):

    def post(self , request , pk):
        selected_options = []
        i = 1
        while True:
            option = request.POST.get(f'option{i}')
            if option:
                i += 1
                selected_options.append(option) 
            else:
                break
        data = {
            "name":request.POST.get('name'),
            "quiz":pk,
            "options":selected_options
        }
        form = AnswerForm(data=data)
        print(form.is_valid())
        if not form.is_valid():
            '''
            return result page  
            '''
            print(form.errors)

        return HttpResponse('done')