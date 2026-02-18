from django.shortcuts import render
from .models import Quote
import random

def home(request):
    quotes = Quote.objects.all()
    # Pick a random one, or show a default if the DB is empty
    random_quote = random.choice(quotes) if quotes.exists() else "Keep coding!"
    return render(request, 'index.html', {'quote': random_quote})