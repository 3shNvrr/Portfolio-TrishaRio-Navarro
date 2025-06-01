from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    return render(request, 'main/skills.html')

def hobbies(request):
    return render(request, 'main/hobbies.html')

def favorites(request):
    folder = request.GET.get('folder')
    context = {'folder': folder}

    if folder == 'anime':
        context['items'] = range(1, 31)
    elif folder == 'manhwa':
        context['items'] = range(1, 21)
    elif folder == 'movies':
        context['items'] = range(1, 31)

    return render(request, 'main/favorites.html', context)



def contact(request):
    return render(request, 'main/contact.html')

def secret(request):
    return render(request, 'main/secret.html')
