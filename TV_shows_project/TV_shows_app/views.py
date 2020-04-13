from django.shortcuts import render, redirect
from TV_shows_app.models import Network, Show

# Create your views here.

def index(request):
    pass

def new(request):
    return render(request, 'new.html')

def create(request):
    # print(request.POST)
    # print(request.POST['title'])
    # print(request.POST['network'])
    # print(request.POST['desc'])
    # print(request.POST['release_date'])

    network = request.POST['network_name']
    all_networks = Network.objects.all()
    
    for net in all_networks:
        if network == net.name:
            new_network = Network.objects.get(name=network)
            new_show = Show.objects.create(title=request.POST['title'], network=new_network, desc=request.POST['desc'], release_date=request.POST['release_date'])
            num1 = int(new_show.id)
            print(num1)
            return redirect(f'/{num1}')
        else:
            new_network = Network.objects.create(name=request.POST['network_name'])
            new_show = Show.objects.create(title=request.POST['title'], network=new_network, desc=request.POST['desc'], release_date=request.POST['release_date'])
            num1 = int(new_show.id)
            print(num1)
            return redirect(f'{num1}')


def display(request, num1):
    context = {
        'number': num1,
    }
    
    return render(request, 'display_shows.html', context)