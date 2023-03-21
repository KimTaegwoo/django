from django.shortcuts   import render, get_object_or_404, redirect
from django.utils       import timezone

# Create your views here.


# from django.http import HttpResponse
from .models            import Question, Answer

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question} 

    return render(request, 'pybo/question_detail.html', context)



def answer_create(request, question_id):
    # pybo 답변 등록

    q = get_object_or_404(Question, pk=question_id)
    print('answer_create: ',q)
    print('request: ',request)
    print('question_id: ',question_id)
    print('--- request.POST.get(content): ', request.POST.get('content'))
    answer = Answer(question = q, 
                    content = request.POST.get('content'),
                    create_date = timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=q.id)


