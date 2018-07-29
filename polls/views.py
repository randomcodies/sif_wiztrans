from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

from .models import Choice, Question,authenticate

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.order_by('-pub_date')

class HomeView(generic.TemplateView):
    template_name = 'polls/home.html'


class Login(generic.TemplateView):
    template_name = 'polls/Login.html'

class Simple_Interface(generic.TemplateView):
    template_name = 'polls/Simple_Interface.html'
    # def get(self, request, **kwargs):
    #     return render(request, 'Simple_Interface.html', context=None)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # selected_choice = question.choice_set.get(pk=request.POST['q_answer'])
        selected_choice = request.POST.get("q_answer", 'This is a default value')
        q1 = Question.objects.get(pk=question_id)
        q1.choice_set.create(choice_text=selected_choice, votes=0)
        q1.save()
    # posted_question = question.question_text.get(question_text=request.POST['question'])
    except Exception as e:
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))

def submit(request):
    inp_value = request.POST.get("qtext", 'This is a default value')
    q1 = Question(question_text=inp_value, pub_date=timezone.now())
    q1.save()
    return HttpResponseRedirect(reverse('polls:results', args=(q1.id,)))

def userauthentication(request):
    #import pdb
    #pdb.set_trace()
    username = request.POST.get("uname")
    password = request.POST.get("psw")
    user = authenticate(username=username, password=password)
   # if user is not None:
       #if user.is_active:
           # login(request, user)
           # return redirect('music/index.html')
    return HttpResponseRedirect(reverse('polls:home'))