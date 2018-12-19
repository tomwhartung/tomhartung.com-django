""" views.py for our content app

Purpose: define the views for this app
Author: Tom W. Hartung
Date: Summer, 2018.
Copyright: (c) 2018 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:
  (none)
"""

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import View


def home(request):

    """ Load and render the Home page template """

    title = "Tom's Non-Corn-Pone Opinions";
    template = 'content/home.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def about(request):

    """ Load and render the about template """

    title = 'Non-Corn-Pone Opinions';

    template = loader.get_template('content/about.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def index(request):

    """ Load and render the index template """

    title = 'index';

    template = loader.get_template('content/index.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def list_of_opinions(request):

    """ Load and render the list_of_opinions template """

    title = 'List of Non-Corn-Pone Opinions';

    template = loader.get_template('content/list_of_opinions.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def opinion(request, opinion_file_no_ext='opinion_outline'):

    """ Load and render the specified opinion template """

    if opinion_file_no_ext == 'book-alexander_hamilton':
        title = 'Alexander Hamilton'
    elif opinion_file_no_ext == 'book-four_hour_work_week':
        title = 'Four Hour Work Week'
    elif opinion_file_no_ext == 'opinion_outline':
        title = 'Opinion Outline'
    else:
        title = '** TITLE NOT SET ***'

    template_file = 'content/opinions/' + opinion_file_no_ext + '.html'
    template = loader.get_template(template_file)
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))


def versions(request):

    """ Load and render the versions template """

    import platform
    python_version = platform.python_version()
    import django
    django_version_1 = django.VERSION
    django_version_2 = django.get_version()

    from .models import DJANGO_DEBUG
    from .models import RUNNING_LOCALLY

    template = loader.get_template('content/versions.html')
    context = {
        'django_version_1': django_version_1,
        'django_version_2': django_version_2,
        'python_version': python_version,
        'DJANGO_DEBUG': DJANGO_DEBUG,
        'RUNNING_LOCALLY': RUNNING_LOCALLY,
    }
    return HttpResponse(template.render(context, request))


def not_found(request, unknown_page='default_unknown_page'):

    """ Load and render the 404 not found template """

    template = loader.get_template('content/404.html')
    context = {
        'unknown_page': unknown_page,
    }
    return HttpResponse(template.render(context, request))


##
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##   Views for Legal Pages
## -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##


def affiliate_marketing_disclosure(request):

    """ Load and render the affiliate_marketing_disclosure template """

    title = 'Disclosure';
    template = 'content/legal/affiliate_marketing_disclosure.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def privacy_policy(request):

    """ Load and render the privacy_policy template """

    title = 'Privacy Policy';
    template = 'content/legal/privacy_policy.html'
    context = {
        'title': title,
    }
    return render(request, template, context)


def terms_of_service(request):

    """ Load and render the terms_of_service template """

    title = 'Terms of Service';
    template = 'content/legal/terms_of_service.html'
    context = {
        'title': title,
    }
    return render(request, template, context)
