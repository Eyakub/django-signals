from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished, request_started
from django.dispatch import receiver, Signal
from .models import Post
# Create your views here.


#custom signals
request_counter_signal = Signal(providing_args=['timestamp'])

def home(request):
    # calling the custom signals and sending arguments
    request_counter_signal.send(sender=Post,timestamp='2019-01-10')
    return HttpResponse('Here is the response')

# request started signal
@receiver(request_started)
def print_started(sender, **kwargs):
    print('request started...')

# after finishing the httpresponse it counted as finished
@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print('request finished...!')


# custom receiver signals
@receiver(request_counter_signal)
def post_counter_signal_receiver(sender, **kwargs):
    print(kwargs)


    # def ready(self):
    #     request_started.connect(self.print_started)
    #     request_started.connect(self.print_finished)

    # def print_started(self, sender, **kwargs):
    #     print('got request')
    
    # def print_finished(self, sender, **kwargs):
    #     print('finished request')