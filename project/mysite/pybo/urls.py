# 여기 폴더의 url을 처리한다.

from django.urls import path

from . import views

app_name = 'pybo'  # 파일에 네임스페이스를 의미하는 app_name 변수를 지정

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

