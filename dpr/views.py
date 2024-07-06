# views.py

from django.shortcuts import render,redirect
from django.utils import timezone
from .models import TimeAndDate
from .forms import TimeAndDateForm
import pytz

from django.shortcuts import render
import pytz
from .models import TimeAndDate

def timeanddate_list(request):
    time_and_date_items = TimeAndDate.objects.all()
    
    # Get user's preferred timezone from session, default to UTC if not set
    user_timezone = request.session.get('user_timezone', 'UTC')
    
    # Convert created_date and updated_date to user's local timezone
    for item in time_and_date_items:
        if item.created_date:
            item.created_date = item.created_date.astimezone(pytz.timezone(user_timezone))
        if item.updated_date:
            item.updated_date = item.updated_date.astimezone(pytz.timezone(user_timezone))
    
    context = {
        'time_and_date_items': time_and_date_items,
        'user_timezone': user_timezone,
    }
    
    return render(request, 'timeanddate_list.html', context)

# Example of setting user's timezone preference in a view
def set_user_timezone(request):
    if request.method == 'POST':
        user_timezone = request.POST.get('timezone')  # Assuming you have a form field named 'timezone'
        request.session['user_timezone'] = user_timezone
        return redirect('timeanddate_list')
    else:
        return render(request, 'set_timezone.html')  # Example template for setting timezone


def timeanddate_create(request):
    if request.method == 'POST':
        form = TimeAndDateForm(request.POST)
        if form.is_valid():
            time_and_date_item = form.save(commit=False)
            time_and_date_item.save()
            return redirect('timeanddate_list')
    else:
        form = TimeAndDateForm()
    return render(request, 'timeanddate_form.html', {'form': form, 'title': 'Create Time and Date'})

# Implement other views (edit, delete) as needed
