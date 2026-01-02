from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from inventory.models import Radiator


@login_required
def dashboard(request):
    """Dashboard view with quick stats and recent jobs"""
    total_jobs = Job.objects.count()
    pending_jobs = Job.objects.filter(status='Pending').count()
    in_progress_jobs = Job.objects.filter(status='In Progress').count()
    completed_jobs = Job.objects.filter(status='Completed').count()
    recent_jobs = Job.objects.all()[:5]
    low_stock_radiators = [r for r in Radiator.objects.all() if r.is_low_stock()]
    
    context = {
        'total_jobs': total_jobs,
        'pending_jobs': pending_jobs,
        'in_progress_jobs': in_progress_jobs,
        'completed_jobs': completed_jobs,
        'recent_jobs': recent_jobs,
        'low_stock_radiators': low_stock_radiators,
    }
    return render(request, 'dashboard.html', context)

