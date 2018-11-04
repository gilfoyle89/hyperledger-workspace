from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_banker:
            return redirect('bankers:quiz_change_list')
        else:
            return redirect('customers:quiz_list')
    return render(request, 'bank/home.html')
