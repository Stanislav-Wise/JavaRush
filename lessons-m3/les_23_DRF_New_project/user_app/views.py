from django.urls import reverse_lazy
from django.views.generic import  FormView, RedirectView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomAuthenticationForm, CustomUserCreationForm


class RegisterView(FormView):
    template_name = 'user_app/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Если наша форма валидна, то мы создаем и сразу логиним пользователя."""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'user_app/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    template_name = 'user_app/logout.html'
    next_page = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


