from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Q, Count
from .forms import ReportForm, ContactForm

def is_valid_queryparam(param):
        return param != '' and param is not None

def home(request):
        qs = Report.objects.all().order_by('-publish_date')
        categories = Category.objects.all()
        subjects = Subject.objects.all()
        regions = Region.objects.all()
        schools = School.objects.all()
        title_contains_query = request.GET.get('title_contains')
        id_exact_query = request.GET.get('id_exact')
        title_or_author_query = request.GET.get('title_or_author')
        view_count_min = request.GET.get('view_count_min')
        view_count_max = request.GET.get('view_count_max')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')
        category = request.GET.get('category')
        subject = request.GET.get('subject')
        region = request.GET.get('region')
        school = request.GET.get('school')
        reviewed = request.GET.get('reviewed')
        not_reviewed = request.GET.get('notReviewed')


        if is_valid_queryparam(title_contains_query):
                qs = qs.filter(title__icontains=title_contains_query)

        elif is_valid_queryparam(id_exact_query):
                qs = qs.filter(id=id_exact_query)

        elif is_valid_queryparam(title_or_author_query):
                qs = qs.filter(Q(title__icontains=title_or_author_query)
                | Q(author__name__icontains=title_or_author_query)
                ).distinct()
        
        if is_valid_queryparam(view_count_min):
                qs = qs.filter(views__gte=view_count_min)

        if is_valid_queryparam(view_count_max):
                qs = qs.filter(views__lt=view_count_max)

        if is_valid_queryparam(date_min):
                qs = qs.filter(publish_date__gte=date_min)

        if is_valid_queryparam(date_max):
                qs = qs.filter(publish_date__lt=date_max)

        
        if is_valid_queryparam(category) and category != 'Choose...':
                qs = qs.filter(categories__name=category)

        if is_valid_queryparam(subject) and subject != 'Choose...':
                qs = qs.filter(subjects__name=subject)

        if is_valid_queryparam(region) and region != 'Choose...':
                qs = qs.filter(regions__name=region)

        if is_valid_queryparam(school) and school != 'Choose...':
                qs = qs.filter(schools__name=school)
                
        if reviewed == 'on':
                qs = qs.filter(reviewed=True)

        elif not_reviewed == 'on':
                qs = qs.filter(reviewed=False)
 
        #return qs

        context = {
                'queryset' : qs,
                'categories' : categories,
                'subjects' : subjects,
                'regions' : regions,
                'schools' : schools
        }
        return render(request, 'Report/home.html', context)

def CreateReport(request):
        if request.method == 'POST':
                form = ReportForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        return redirect('/')
        else:
                form = ReportForm()
                
        context = {
                'form': form
        }
        return render(request, 'Report/report_form.html', context)

def about(request):
        return render(request, 'Report/about.html')
        
def news(request):
        return render(request, 'Report/news.html')
        

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                form.save()
                pass  # does nothing, just trigger the validation
        messages.success(request, f'Thank you, we have received your message')
        return redirect('/about')
    else:
        form = ContactForm()
    return render(request, 'Report/contact_form.html', {'form': form})
