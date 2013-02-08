# Create your views here.
import logging

from gui.models import *
log = logging.getLogger(__name__)
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods
from django.utils.encoding import *
from django.utils.hashcompat import md5_constructor, sha_constructor

#######################
# User Related Methods
#######################
def get_hexdigest(algorithm, salt, raw_password):
    """
    Returns a string of the hexdigest of the given plaintext password and salt
    using the given algorithm ('md5', 'sha1' or 'crypt').
    """
    raw_password, salt = smart_str(raw_password), smart_str(salt)
    if algorithm == 'crypt':
        try:
            import crypt
        except ImportError:
            raise ValueError('"crypt" password algorithm not supported in this environment')
        return crypt.crypt(raw_password, salt)

    if algorithm == 'md5':
        return md5_constructor(salt + raw_password).hexdigest()
    elif algorithm == 'sha1':
        return sha_constructor(salt + raw_password).hexdigest()
    raise ValueError("Got unknown password algorithm type in password.")

def check_password(raw_password, enc_password):
    """
    Returns a boolean of whether the raw_password was correct. Handles
    encryption formats behind the scenes.
    """
    algo, salt, hsh = enc_password.split('$')
    return hsh == get_hexdigest(algo, salt, raw_password)

def is_logged_in(request):
    try:
        my_return = request.session['is_logged_in']
    except:
        my_return = False;
    return my_return


def enter(request):
    if is_logged_in(request):
        return redirect('/', False)
    return render_to_response('gui/signup.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))


def not_found(request):
    return render_to_response('gui/404.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))


def exit_request(request):
    request.session['is_logged_in'] = False
    request.session['email'] = None
    return redirect('/', False)


def forgot_password(request):
    if is_logged_in(request) is True:
        return redirect('/', False)
    else:
        return render_to_response('gui/forgot_password.html', context_instance=RequestContext(request))


@require_http_methods(["POST"])
def process_create_account(request):
    try:
        u = User.objects.filter(email=request.POST['email'])
    except:
        u = False # user does not exist in database
    if u:
        return render_to_response('gui/signup.html', {'error_message': "Email is already taken"},
            context_instance=RequestContext(request))
    u = User(email=request.POST['email'], password=get_hexdigest('crypt','salt',request.POST['password']))
    u.save()

    # send_mail('Registration Complete','This message confirms that your registration is complete', 'noreply@t-mobile.com',[request.POST['email']])
    request.session['is_logged_in'] = True
    request.session['email'] = request.POST['email']
    return redirect('/', False)


@require_http_methods(["POST"])
def process_sign_up(request):
    try:
        u = User.objects.get(email=request.POST['email_2'], password=get_hexdigest('crypt','salt',request.POST['password_2']))
    except:
        u = False # user does not exist in database
    if u:
        request.session['is_logged_in'] = True
        request.session['email'] = request.POST['email_2']
    else:
        return render_to_response('gui/signup.html', {'error_message': "Email and Password Don't Match"},
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
        return render_to_response('gui/forgot_password.html',
            {'my_error_message': "An email with the password has been sent to: " + u.email},
            context_instance=RequestContext(request))
    else:
        return render_to_response('gui/forgot_password.html', {'my_error_message': "Email Is Not Found"},
            context_instance=RequestContext(request))

#######################
# App Related Methods
#######################
def front_page(request):
    if is_logged_in(request) is False:
        return render_to_response('gui/signup.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))
    else:
        return render_to_response('gui/front_page.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))

def configuration_form(request):
    if is_logged_in(request) is False:
        return render_to_response('gui/signup.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))
    else:
        if request.method == 'POST': # If the form has been submitted...
            user = User.objects.get(email=request.session['email'])
            if user:
                form = ConfigurationForm(request.POST) # A form bound to the POST data
                if form.is_valid():
                    configuration = form.save(commit=False)
                    configuration.user = user
                    configuration.save()
                    return render_to_response('gui/front_page.html', {'is_logged_in': is_logged_in(request),'feedback':'A new record has been added.'},
                        context_instance=RequestContext(request))
            else:
                return redirect('exit_request')
        else:
            form = ConfigurationForm() # An unbound form
        return render_to_response('gui/configuration_form.html', {'is_logged_in': is_logged_in(request),'form': form}, context_instance=RequestContext(request))


# Custom 404 and 500
def my_custom_404_view(request):
    return render_to_response('gui/404.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))

def my_custom_500_view(request):
    return render_to_response('gui/500.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))

