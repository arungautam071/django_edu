from django.shortcuts import render
from django.urls import  reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def home(request):
    return render(request, 'main_section/index.html')



from django.views.generic import CreateView
from .models import Contact

class ContactView(SuccessMessageMixin,CreateView):
    model = Contact
    template_name = 'main_section/index.html'
    success_url = reverse_lazy("main-home")
    success_message = '"Your message has been successfully sent !!!!'
    fields = ('name', 'email', 'phone_number', 'Subject','message')    
     # this method will enable your message to display
    # you can also use it to overwrite form data.
    # def form_valid(form):
    #     messages.success(f'Account created successfully')
    #     return super().form_valid(form)