from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def submit_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('submit_message')
    else:
        form = MessageForm()

    return render(request, 'submit_message.html', {'form':form})

def get_message(request, recipient_name):
    messages = Message.objects.filter(recipient_name=recipient_name).order_by('-timestamp')[:20]
    return render(request, 'get_messages.html', {'messages': messages, 'recipient_name': recipient_name})