# resumeeApp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from .models import Resume
import json

def home(request):
    return render(request, 'home.html')

def templates(request):
    return render(request, 'templates.html')

def builder(request):
    selected_template = request.session.get('selected_template', '1')
    selected_color = request.session.get('selected_color', 'black')

    if request.method == 'POST':
        # Extract data from POST request
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        skills_json = request.POST.get('skills')  # JSON string
        work_experiences_json = request.POST.get('work_experiences')  # JSON string
        educations_json = request.POST.get('educations')  # JSON string

        # Save to database
        resume = Resume.objects.create(
            name=name,
            address=address,
            phone=phone,
            email=email,
            skills=skills_json,
            work_experiences=work_experiences_json,
            educations=educations_json,
            selected_template=selected_template,
            selected_color=selected_color,
        )

        # Redirect to resume detail page
        return redirect('resume_detail', resume_id=resume.id)
    else:
        context = {
            'selected_template': selected_template,
            'selected_color': selected_color,
        }
        return render(request, 'builder.html', context)

@csrf_exempt
def set_template_color(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_template = data.get('selected_template')
        selected_color = data.get('selected_color')

        request.session['selected_template'] = selected_template
        request.session['selected_color'] = selected_color

        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def render_resume_preview(request):
    if request.method == 'POST':
        selected_template = request.session.get('selected_template', '1')
        selected_color = request.session.get('selected_color', 'black')

        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        skills_json = request.POST.get('skills', '')
        work_experiences_json = request.POST.get('work_experiences', '')
        educations_json = request.POST.get('educations', '')

        # Convert JSON strings back to Python objects
        skills = json.loads(skills_json) if skills_json else []
        work_experiences = json.loads(work_experiences_json) if work_experiences_json else []
        educations = json.loads(educations_json) if educations_json else []

        context = {
            'name': name,
            'address': address,
            'phone': phone,
            'email': email,
            'skills': skills,
            'work_experiences': work_experiences,
            'educations': educations,
            'selected_color': selected_color,
        }

        html = render_to_string(
            f'templates/template_{selected_template}.html', context
        )
        return HttpResponse(html)
    return HttpResponse(status=400)

def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)

    # Parse JSON fields back into Python objects
    skills = json.loads(resume.skills) if resume.skills else []
    work_experiences = json.loads(resume.work_experiences) if resume.work_experiences else []
    educations = json.loads(resume.educations) if resume.educations else []

    context = {
        'name': resume.name,
        'address': resume.address,
        'phone': resume.phone,
        'email': resume.email,
        'skills': skills,
        'work_experiences': work_experiences,
        'educations': educations,
        'selected_color': resume.selected_color,
        'selected_template': resume.selected_template,
    }
    return render(
        request,
        f'templates/template_{resume.selected_template}.html',
        context
    )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')
