from django.shortcuts import render

# Create your views here.
# dps/views.py

from django.shortcuts import render, redirect
from .dps import Data
from .forms import DataForm


# dpr/views.py

def home(request):
    data = Data.objects.all()
    return render(request, 'home.html', {'data': data})

def create_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after saving
    else:
        form = DataForm()
    return render(request, 'create.html', {'form': form})
# dpr/views.py
# dpr/views.py

def update_data(request, id):
    data = Data.objects.get(id=id)
    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after updating
    else:
        form = DataForm(instance=data)
    return render(request, 'update_data.html', {'form': form})


def delete_data(request, id):
    data = Data.objects.get(id=id)
    data.delete()
    return redirect('home')

