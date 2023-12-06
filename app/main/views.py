from django.shortcuts import render, redirect

from .forms import CinemaForm


def add_cinema(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
        else:
            print(form.errors)
    else:
        form = CinemaForm()

    return render(request, 'main/add_cinema.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')
