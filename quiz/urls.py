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
from rest_framework_nested import routers


# app
from users.views import (
    LoginView,
    SignUpView
)

# api
from api.views import (
    QuizViewSet,
    QuestionViewSet
)

router = routers.DefaultRouter()

router.register(r'quiz', QuizViewSet , basename='quiz')

quiz_router = routers.NestedSimpleRouter(router, r'quiz' ,lookup='quiz')
quiz_router.register(r'question', QuestionViewSet , basename='question')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('' , TemplateView.as_view(template_name='users/home.html')),

    # api's
    path('api/' , include(router.urls)),
    path('api/',include(quiz_router.urls)),

    # auth
    path('logout/', LogoutView.as_view() , name='logout'),
    path('login/' , LoginView.as_view() , name='login'),
    path('signup/' , SignUpView.as_view() , name='signup')
]
