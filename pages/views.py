from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    """
    Home page view
    """
    context = {
        'page_title': 'CognitronixTechnology - AI Training Platform',
        'meta_description': 'Join CognitronixTechnology in shaping the future of AI. Flexible remote work, competitive pay, and hands-on AI training experience.',
    }
    return render(request, 'pages/home.html', context)


def about(request):
    """
    About page view
    """
    context = {
        'page_title': 'About Us - CognitronixTechnology',
        'meta_description': 'Learn about CognitronixTechnology\'s mission to drive innovation through human-AI collaboration.',
    }
    return render(request, 'pages/about.html', context)


def faq(request):
    """
    FAQ page view
    """
    # You can add dynamic FAQ data here if needed
    faq_data = [
        {
            'question': 'What is AI training?',
            'answer': 'AI training involves providing labeled data and feedback to machine learning models so they can learn patterns and make accurate predictions.',
            'category': 'getting-started'
        },
        {
            'question': 'Do I need technical experience?',
            'answer': 'No technical experience is required! We provide comprehensive training for all tasks.',
            'category': 'getting-started'
        },
        {
            'question': 'How much can I earn?',
            'answer': 'Most trainers earn between $15-$30 per hour based on task complexity.',
            'category': 'earnings'
        },
        {
            'question': 'What are the requirements?',
            'answer': 'You need a reliable internet connection, a computer or smartphone, and proficiency in English.',
            'category': 'getting-started'
        },
        {
            'question': 'How flexible is the schedule?',
            'answer': 'Completely flexible! You can work whenever you want, from anywhere.',
            'category': 'tasks'
        },
        {
            'question': 'What support do you provide?',
            'answer': 'We provide 24/7 support, detailed training materials, community forums, and video tutorials.',
            'category': 'support'
        },
    ]

    context = {
        'page_title': 'FAQ - CognitronixTechnology',
        'meta_description': 'Frequently asked questions about becoming an AI trainer with CognitronixTechnology.',
        'faqs': faq_data,
    }
    return render(request, 'pages/faq.html', context)


def register(request):
    """
    Registration page view (frontend-only form)
    """
    context = {
        'page_title': 'Register - CognitronixTechnology',
        'meta_description': 'Create your account to start your journey as an AI trainer.',
    }

    if request.method == 'POST':
        # Frontend-only form handling (no actual user creation)
        email = request.POST.get('email', '')
        if email:
            messages.success(request, 'Registration successful! Please check your email.')
            return redirect('home')

    return render(request, 'pages/register.html', context)


def login(request):
    """
    Login page view (frontend-only, no actual authentication needed)
    """
    context = {
        'page_title': 'Login - CognitronixTechnology',
        'meta_description': 'Login to your CognitronixTechnology account.',
    }

    if request.method == 'POST':
        # Frontend-only login simulation
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Simple validation (for demo purposes only)
        if email and password:
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Please enter both email and password.')

    return render(request, 'pages/login.html', context)


def logout(request):
    """
    Logout view (frontend-only)
    """
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def how_it_works(request):
    """
    How It Works page view
    """
    context = {
        'page_title': 'How It Works - CognitronixTechnology',
        'meta_description': 'Learn how to become an AI trainer with CognitronixTechnology in three simple steps.',
    }
    return render(request, 'pages/how_it_works.html', context)


def join(request):
    """
    Join Our Team page view
    """
    context = {
        'page_title': 'Join Our Team - CognitronixTechnology',
        'meta_description': 'Apply to become an AI trainer with CognitronixTechnology.',
    }

    if request.method == 'POST':
        # Handle the application form submission (frontend-only)
        # In a real app, you'd save this to a database
        first_name = request.POST.get('firstName', '')
        email = request.POST.get('email', '')

        if first_name and email:
            messages.success(request, f'Thank you {first_name}! Your application has been submitted.')
            return redirect('home')

    return render(request, 'pages/join.html', context)