from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.contrib import messages
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if form.errors.get('phone_no', None):
            if 'exists' in str(form.errors['phone_no']):
                messages.error(self.request, 'این شماره قبلا ثبت شده')
            else:
                messages.error(self.request, 'فرمت شماره صحیح نمی باشد')

        if form.errors.get('password2', None):
            if 'match' in str(form.errors['password2']):
                messages.error(self.request, 'رمزها یکسان نمی باشند')

            else:
                messages.error(self.request, 'این رمز ساده است')

        return response
