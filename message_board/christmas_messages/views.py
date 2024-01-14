from django.shortcuts import render, redirect
from .models import ChristmasMessage


def submit_message(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        last_name = request.POST.get('last_name')  # Ajout de last_name
        city = request.POST.get('city')  # Ajout de city
        gift_list = request.POST.get('gift_list')
        kindness_level = request.POST.get('kindness_level')
        age = request.POST.get('age')
        
        # Ajoutez ces lignes pour gérer correctement le champ has_cavities
        has_cavities = request.POST.get('has_cavities', False)
        has_cavities = True if has_cavities == 'on' else False

        ChristmasMessage.objects.create(
            sender_name=sender_name,
            last_name=last_name,  # Ajout de last_name
            city=city,  # Ajout de city
            gift_list=gift_list,
            kindness_level=kindness_level,
            age=age,
            has_cavities=has_cavities
        )
        # Redirige l'utilisateur vers la page de départ après avoir soumis le message.
        return redirect('submit_message')

    return render(request, 'submit_message.html')

def get_messages(request):
    messages = ChristmasMessage.objects.order_by('-timestamp')
    return render(request, 'get_messages.html', {'messages': messages})

def delete_message(request, message_id):
    message = ChristmasMessage.objects.get(pk=message_id)
    message.delete()
    return redirect('get_messages')