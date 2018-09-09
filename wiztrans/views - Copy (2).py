from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from googletrans import Translator



from .models import Choice, Question,authenticate,Category,Document
from .forms import DocumentForm

# Create your views here.


# #class IndexView(generic.ListView):
# #    template_name = 'wiztrans/index.html'
#     context_object_name = 'latest_question_list'
#
# #    def get_queryset(self):
#         """Return the last five published questions."""
#         #return Question.objects.order_by('-pub_date')[:5]
#         return Question.objects.order_by('-pub_date')



class IndexView(generic.ListView):
    template_name = 'wiztrans/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #fs=FileSystemStorage()
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



class HomeView(generic.TemplateView):
    template_name = 'wiztrans/home.html'


class Login(generic.TemplateView):
    template_name = 'wiztrans/Login.html'

class Simple_Interface(generic.ListView):
    context_object_name = 'home_list'
    template_name = 'wiztrans/Simple_Interface.html'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Simple_Interface, self).get_context_data(**kwargs)
        context['lang_list'] = Category.objects.filter(question_category2='Language')
        context['type_list'] = Category.objects.filter(question_category2='Type')
        # And so on for more models
        return context

class DetailView(generic.DetailView):
    #import pdb
    #pdb.set_trace()
    model = Question
    #qid = request.GET.get("pk")
    #translator = Translator()
    template_name = 'wiztrans/detail.html'
    #context_object_name = 'translated_question_list'
    #latest_question_list= translator.translate(Question.question_text, dest='ms')




class ResultsView(generic.DetailView):
    model = Question
    translator = Translator()
    template_name = 'wiztrans/results.html'


def vote(request, question_id):
    #import pdb
    question = get_object_or_404(Question, pk=question_id)
    try:
        #pdb.set_trace()
        #translator = Translator()
        #quest_translated= translator.translate(question.question_text, dest='ms')
        # selected_choice = question.choice_set.get(pk=request.POST['q_answer'])
        selected_choice = request.POST.get("q_answer", '')
        #if selected_choice != '':
        q1 = Question.objects.get(pk=question_id)
        uploaded_file_url=''
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        q1.choice_set.create(choice_text=selected_choice, votes=0,answer_link=uploaded_file_url)
        q1.save()
       # else:
            #return HttpResponseRedirect(reverse('wiztrans:detailtrans', args=(question.id,quest_translated,))
    # posted_question = question.question_text.get(question_text=request.POST['question'])
    except Exception as e:
        q1.choice_set.create(choice_text=selected_choice, votes=0,answer_link=uploaded_file_url)
        q1.save()
        # Redisplay the question voting form.
        return HttpResponseRedirect(reverse('wiztrans:detail', args=(question.id,)))
    else:
        return HttpResponseRedirect(reverse('wiztrans:detail', args=(question.id,)))

def submit(request):
    #import pdb
    try:
        inp_value = request.POST.get("qtext", 'This is a default value')
        inp_cat1 = request.POST.get("cat1", 'English')
        inp_cat2 = request.POST.get("cat2", 'Rhymes')
        translator = Translator()
        q_trans_ms= translator.translate(inp_value, dest='ms').text
        q_trans_md= translator.translate(inp_value, dest='zh-CN').text
        q_trans_ta= translator.translate(inp_value, dest='ta').text
        uploaded_file_url=''
        #pdb.set_trace()
        #test_file= request.POST.get('myfile')
        #Yes=request.POST.get("Yes", 'off')
        #if Yes == 'on':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        q1 = Question(question_text=inp_value,question_category1=inp_cat1,question_category2=inp_cat2, pub_date=timezone.now(),question_link=uploaded_file_url,question_text_my=q_trans_ms,question_text_md=q_trans_md,question_text_ta=q_trans_ta)
        q1.save()
        #pdb.set_trace()
        #if request.method == 'POST' and request.FILES['myfile']:
    except Exception as e:
        q1 = Question(question_text=inp_value,question_category1=inp_cat1,question_category2=inp_cat2, pub_date=timezone.now(),question_link=uploaded_file_url,question_text_my=q_trans_ms,question_text_md=q_trans_md,question_text_ta=q_trans_ta)
        q1.save()
        # Redisplay the question voting form.
        return HttpResponseRedirect(reverse('wiztrans:results', args=(q1.id,)))

    return HttpResponseRedirect(reverse('wiztrans:results', args=(q1.id,)))

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
    return HttpResponseRedirect(reverse('wiztrans:home'))
