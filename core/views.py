from django.shortcuts import render, redirect
from .forms import RatingForm
from .models import Rating
from .filters import RatingFilter

def home(request):
    if request.method == "POST":
      form = RatingForm(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return redirect('search')
    else:
      form = RatingForm()
    return render(request, 'home.html', {"form" : form})

def search(request):
    template = 'search.html'
    rating = Rating.objects.all()
    rating_filter = RatingFilter(request.GET, queryset=rating)
    context = {"rating": rating_filter}
    return render(request,template, context)