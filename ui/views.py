# Create your views here.
import logging

log = logging.getLogger(__name__)
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
import simplejson as json
from datetime import datetime, timedelta
import pytz


# View Methods

# User Related Methods
def is_logged_in(request):
    try:
        my_return = request.session['is_logged_in']
    except:
        my_return = False;
    return my_return


def enter(request):
    if is_logged_in(request):
        return redirect('/', False)
    return render_to_response('ui/signup.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))


def not_found(request):
    return render_to_response('ui/404.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))


def exit_request(request):
    request.session['is_logged_in'] = False
    request.session['email'] = None
    return redirect('/', False)


def forgot_password(request):
    if is_logged_in(request) is True:
        return redirect('/', False)
    else:
        return render_to_response('ui/forgot_password.html', context_instance=RequestContext(request))


@require_http_methods(["POST"])
def process_create_account(request):
    try:
        u = User.objects.filter(email=request.POST['email'])
    except:
        u = False # user does not exist in database
    if u:
        return render_to_response('ui/signup.html', {'error_message': "Email is already taken"},
            context_instance=RequestContext(request))
    u = User(email=request.POST['email'], password=request.POST['password'])
    u.save()
    from django.core.mail import send_mail

    send_mail('Registration Complete',
        'This message confirms that your registration at http://apns.t-mobile.com/ is complete', 'noreply@t-mobile.com',
        [request.POST['email']])
    request.session['is_logged_in'] = True
    request.session['email'] = request.POST['email']
    return redirect('/', False)


@require_http_methods(["POST"])
def process_sign_up(request):
    try:
        u = User.objects.get(email=request.POST['email_2'], password=request.POST['password_2'])
    except:
        u = False # user does not exist in database
    if u:
        request.session['is_logged_in'] = True
        request.session['email'] = request.POST['email_2']
    else:
        return render_to_response('ui/signup.html', {'error_message': "Email and Password Don't Match"},
            context_instance=RequestContext(request))
        # code
    return redirect('/', False)


@require_http_methods(["POST"])
def process_forgot_password(request):
    try:
        u = User.objects.get(email=request.POST['email'])
    except:
        u = False # user does not exist in database
    if u:
        #from django.core.mail import send_mail
        #send_mail('Password Recovery', 'Your password at http://movies.chooseinteresting.com/ is:' + u.password, 'noreply@t-mobile.com', [request.POST['email']])
        return render_to_response('ui/forgot_password.html',
            {'my_error_message': "An email with the password has been sent to: " + u.email},
            context_instance=RequestContext(request))
    else:
        return render_to_response('ui/forgot_password.html', {'my_error_message': "Email Is Not Found"},
            context_instance=RequestContext(request))


# App Related Methods
def home_list_options(request):
    if is_logged_in(request) is False:
        return render_to_response('ui/signup.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))
    else:
        user = User.objects.filter(email=request.session['email'])
        return render_to_response('ui/home_list_options.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))

    def configuration_form(request, app_id):
        if is_logged_in(request) is False:
            return render_to_response('ui/signup.html', {'is_logged_in': is_logged_in(request)},
                context_instance=RequestContext(request))
        params = request.REQUEST
        user = params.get('user_id', None) # required
        server = params.get('server_id', None) # required
        host = params.get('host_id', None) # required
        data_center = params.get('data_center_id', None) # required
        cluster = params.get('cluster_id', None) # required
        cpu = params.get('cpu', None) # required
        memory = params.get('memory', None) # required

        # Verify Permission
        try:
            u = User.objects.get(email=request.session['email'])
        except:
            u = None

        return render_to_response('ui/form_success.html',
            {'is_logged_in': is_logged_in(request), 'server': server, 'cpu': cpu, 'memory': memory},
            context_instance=RequestContext(request))

    # Custom 404 and 500
    def my_custom_404_view(request):
        return render_to_response('ui/404.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))

    def my_custom_500_view(request):
        return render_to_response('ui/500.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))