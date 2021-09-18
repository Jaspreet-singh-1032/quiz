"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


# drf imports
from rest_framework_nested import routers

# custom dacorators
from app.dacorators import cache_page_for_guests

# users
from users.views import (
    LoginView,
    SignUpView
)

# app
from app.views import (
    ListQuizView,
    QuizPageView,
    ResultView,
    ResultPageView,
    DeleteQuizView
)

# api
from api.views import (
    QuizViewSet,
    QuestionViewSet,
)

router = routers.DefaultRouter()

router.register(r'quiz', QuizViewSet , basename='quiz')

quiz_router = routers.NestedSimpleRouter(router, r'quiz' ,lookup='quiz')
quiz_router.register(r'question', QuestionViewSet , basename='question')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('' , TemplateView.as_view(template_name='users/home.html')),

    # api's
    path('api/' , include(router.urls)),
    path('api/',include(quiz_router.urls)),

    # app
    path('app/quiz/' , ListQuizView.as_view() , name='quiz_list'),
    path('app/quiz/<str:pk>/' , (cache_page_for_guests(20))(QuizPageView.as_view()) , name='quiz_page'),
    path('app/quiz/<str:pk>/delete/' , DeleteQuizView.as_view() , name='quiz_delete'),
    path('app/quiz/<str:pk>/results/',ResultView.as_view() , name='quiz_results'), # for authenticated user to view all results
    path('app/quiz/result/<str:pk>/',ResultPageView.as_view() , name='result_page'), # for visitor who is attempting quiz

    # auth
    path('logout/', LogoutView.as_view() , name='logout'),
    path('login/' , LoginView.as_view() , name='login'),
    path('signup/' , SignUpView.as_view() , name='signup')
] 
