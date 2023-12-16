class LoginPageView(LoginView):
    template_name = 'main/index_login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main_page')
    extra_context = {
        'title': 'Login'
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)


class RegisterPageView(CreateView):
    template_name = 'main/index_register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login_page')
    extra_context = {
        'title': 'Register',
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('main_page')
