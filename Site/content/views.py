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

from .affiliate_marketing import AffiliateLinks
from .models import RUNNING_LOCALLY


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

    title = 'About Non-Corn-Pone Opinions';

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    template = loader.get_template('content/about.html')
    context = {
        'title': title,
        'afl_content': afl_content,
        'afl_button': afl_button,
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


def opinions_list(request):

    """ Load and render the opinions_list template """


    if RUNNING_LOCALLY == '0':
        include_drafts = False
    else:
        include_drafts = True

    title = 'List of Non-Corn-Pone Opinions';

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    template = loader.get_template('content/opinions_list.html')
    context = {
        'include_drafts': include_drafts,
        'title': title,
        'afl_content': afl_content,
        'afl_button': afl_button,
    }
    return HttpResponse(template.render(context, request))


def opinion_files(request, opinion_file_no_ext='opinion-outline'):

    """ Load and render the specified opinion_files template """

    if opinion_file_no_ext == 'book-alexander_hamilton':
        title = 'Hamilton and Jefferson'
    elif opinion_file_no_ext == 'book-deep_work':
        title = "Deep Work by Cal Newport"
    elif opinion_file_no_ext == 'book-dorie_clark':
        title = "Review of one or more of Dorie Clark's Books"
    elif opinion_file_no_ext == 'book-four_hour_work_week':
        title = 'Review: 4 Hour Workweek'
    elif opinion_file_no_ext == 'book-to_sell_is_human':
        title = 'Review: To Sell Is Human'
    elif opinion_file_no_ext == 'opinion-outline':
        title = 'Opinion Outline'
    elif opinion_file_no_ext == 'opinion-nothing_on_this_page_is_real':
        title = 'Nothing on This Page Is Real'
    elif opinion_file_no_ext == 'rant-facebook_is_the_new_tobacco':
        title = 'FB Rant'
    elif opinion_file_no_ext == 'rant-tech_shortage':
        title = 'Tech Shortage Is BS Rant'
    else:
        title = '** TITLE NOT SET ***'

    afl_links = AffiliateLinks()
    afl_content = afl_links.afl_content
    afl_button = afl_links.afl_content

    template_file = 'content/opinion_files/' + opinion_file_no_ext + '.html'
    template = loader.get_template(template_file)
    context = {
        'title': title,
        'afl_content': afl_content,
        'afl_button': afl_button,
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

    title = 'Versions'
    template = loader.get_template('content/versions.html')
    context = {
        'django_version_1': django_version_1,
        'django_version_2': django_version_2,
        'python_version': python_version,
        'DJANGO_DEBUG': DJANGO_DEBUG,
        'RUNNING_LOCALLY': RUNNING_LOCALLY,
        'title': title,
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
