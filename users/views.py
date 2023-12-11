from django.views.generic import TemplateView


class CustomUserRegistration(TemplateView):
    template_name = "account/signup.html"
