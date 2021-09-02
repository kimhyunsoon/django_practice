from accountapp.forms import AccountUpdateForm
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, UpdateView

from accountapp.models import HelloWorld

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from django.views.generic import CreateView


# Create your views here.
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        # 입력받은 정보 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save();

        print(new_hello_world.text)
        # 입력받은 정보 불러옴
        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


class AccountDeleteView(DeleteView):
    model =User
    success_url= reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
