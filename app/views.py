# django imports
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import HttpResponse , redirect , render
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages

# models imports
from .models import (
    Quiz,
    Answer
)

# forms import
from .forms import (
    AnswerForm
)

class ListQuizView(LoginRequiredMixin,generic.ListView ):
    '''
    rerturn list of quiz created by user
    '''
    template_name = 'app/quiz_list.html'
    context_object_name = 'quiz_list'
    
    def get_queryset(self):
        queryset = Quiz.objects.values('id','name','uuid').filter(user = self.request.user).order_by('-created')
        if queryset.count() == 0:
            messages.info(self.request, 'You have not created any quiz yet !')
        return queryset

class QuizPageView(generic.DetailView):
    '''
    return quiz page to attempt the quiz
    '''
    template_name = 'app/quiz_page.html'
    context_object_name = 'quiz'
    queryset = Quiz.objects.all()
    slug_field = 'uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = context['quiz'].questions.all()
        return context
    
class ResultView(View):

    def get_queryset(self):
        self.quiz = get_object_or_404(Quiz.objects.prefetch_related('questions'), pk=self.kwargs.get('pk') , user=self.request.user)        
        return Answer.objects.prefetch_related('options').filter(quiz=self.quiz).order_by('-created')
    
    def get_context_data(self):
        context = {}
        context['answers_list'] = self.get_queryset()
        context['quiz_name'] = self.quiz.name
        context['max_score'] = self.quiz.questions.count()
        return context
    
    def get(self , request , pk):
        '''
        return list of results for a quiz
        '''
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        context = self.get_context_data()
        
        return render(request, 'app/results_list.html' , context)

    def post(self , request , pk):
        '''
        save the result of a quiz
        '''
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
        if form.is_valid():
            obj = form.save()
            return redirect(reverse_lazy('result_page',kwargs={'pk':obj.pk}))
        messages.warning(request, 'Please try later')
        return redirect('/')


class ResultPageView(generic.DetailView):
    '''
    show result page
    '''
    template_name = 'app/result.html'
    context_object_name = 'answer'

    def get_object(self ):
        answer = get_object_or_404(Answer.objects.prefetch_related('options'), pk=self.kwargs.get('pk'))
        return answer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['answer'].quiz.user)
        context["total_answers"] = context['answer'].options.all().count()
        context["correct_answers"] = context['answer'].options.filter(is_correct=True).count()
        return context

class DeleteQuizView(LoginRequiredMixin,generic.DeleteView):
    """ delete quiz """
    success_url = reverse_lazy('quiz_list')

    def get_queryset(self):
        return Quiz.objects.filter(user = self.request.user)
    