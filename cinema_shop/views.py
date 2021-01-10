from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User


from .forms import ProjectionForm, CardForm
from .models import Projection, Card

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    return render(request, "index.html", {})

# Craeting projection object in database
@login_required(login_url='login')
def projection_create_view(request):
    form = ProjectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectionForm()
    
    return render(request, "create_projection.html", {'form': form});

# Displaying List of Projection objects
@login_required(login_url='login')
def projection_list_view(request):
    movies = Projection.objects.all()
    context = {
        "movies": movies,
    }
    return render(request, "projection_list_view.html", context)
    

# Buying ticket for Movie
@login_required(login_url='login')
def create_ticket(request, movie_id):
    movie = Projection.objects.get(pk=movie_id)
    bought_cards = Card.objects.filter(movie = movie_id).values_list('seat_number', flat=True)
    context = {
        "movie": movie,
        "bought_cards": bought_cards
    }
    if request.method == 'POST':
        seat_number = request.POST['seat_number']
        Card.objects.create(movie=movie, user=request.user, seat_number=seat_number)
        return redirect('tickets')
    return render(request, "buy_ticket.html", context);
    

# Displaying List of Card objects
@login_required(login_url='login')
def card_list_view(request):
    queryset = Card.objects.filter(user__username = request.user).select_related('movie')
    context = {
        "tickets": queryset
    }
    return render(request, "card_list_view.html", context)

# Displaying Single Projection object
@login_required(login_url='login')
def projection_view(request, id):
    movie = get_object_or_404(Projection, id=id)
    allViewers = {}
    for card in movie.card_set.all():
        if card.user in allViewers:
            allViewers[card.user] += 1
        else:
            allViewers[card.user] = 1
    bought_cards = Card.objects.filter(movie = id).values_list('seat_number', flat=True)
    context = {
        "movie": movie,
        "allViewers": allViewers,
        "bought_cards": bought_cards
    }
    return render(request, 'projection_view.html', context)

# Register new user
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = UserCreationForm()
    return render(request, 'register.html', {"form": form})

# User Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

# User Logout
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')