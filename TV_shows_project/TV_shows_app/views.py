from django.shortcuts import render, redirect
from TV_shows_app.models import Network, Show

# Create your views here.

def index(request):
    pass

def new(request):
    return render(request, 'new.html')

def create(request):

    network = request.POST['network_name']
    title = request.POST['title']
    desc = request.POST['desc']
    release_date = request.POST['release_date']
    all_networks = Network.objects.all()
    
    for net in all_networks:
        if network == net.name:
            current_network = Network.objects.get(name=network)
            new_show = Show.objects.create(title=title, network=current_network, desc=desc, release_date=release_date)
            num1 = int(new_show.id)
            print(num1)
            return redirect(f'/{num1}')
        else:
            new_network = Network.objects.create(name=network)
            new_show = Show.objects.create(title=title, network=new_network, desc=desc, release_date=release_date)
            num1 = int(new_show.id)
            print(num1)
            return redirect(f'/{num1}')


def display(request, num1):
    display_show = Show.objects.get(id=num1)

    context = {
        'number': num1,
        'display_show': display_show,
    }
    
    return render(request, 'display_shows.html', context)

def shows(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows,
    }
    return render(request, 'shows.html', context)


def edit(request):
    pass