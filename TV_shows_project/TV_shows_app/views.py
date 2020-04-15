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
            return redirect(f'/shows/{num1}')
    else:
        new_network = Network.objects.create(name=network)
        new_show = Show.objects.create(title=title, network=new_network, desc=desc, release_date=release_date)
        num1 = int(new_show.id)
        return redirect(f'/shows/{num1}')


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

def edit(request, num1):
    display_show2 = Show.objects.get(id=num1)
    context = {
        'display_show2': display_show2,
        'num1': num1,
    }
    return render(request, 'edit.html', context)

def update(request, num1):
    print('HELLO IS THIS WORKING')
    edit_show = Show.objects.get(id=num1)
    new_title = request.POST['title']
    new_desc = request.POST['desc']
    new_network = request.POST['network_name']
    new_release_date = request.POST['release_date']


    if new_title != edit_show.title:
        print(new_title)
        edit_show.title = new_title
        edit_show.save()
    if new_desc != edit_show.desc:
        print('first elif ')
        edit_show.desc = new_desc
        edit_show.save()
    if new_release_date != edit_show.release_date:
        edit_show.release_date = new_release_date
        edit_show.save()
    if new_network != 'foo':
        print('in elif')
        all_networks = Network.objects.all()
        for nets in all_networks:
            if new_network == nets.name:
                print(new_network)
                edit_show.network = nets
                edit_show.save()
    else:
        print('in else statement')
        edit_show.network = new_network
        edit_show.save()
            

    # all_networks = Network.objects.all()
    # for nets in all_networks:
    #     if new_network == nets.name:
    #         edit_show.network = nets
    #     else:
    #         edit_show.network = new_network
    #         edit_show.save()



    return redirect(f'/shows/{num1}')


def destroy(request, num1):
    delete_show = Show.objects.get(id=num1)
    delete_show.delete()
    return redirect('/shows')
