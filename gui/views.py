# Create your views here.
import logging
from gui.models import *
log = logging.getLogger(__name__)
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from users.views import is_logged_in

#######################
# App Related Methods
#######################
def front_page(request):
    if is_logged_in(request) is False:
        return render_to_response('users/signup.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))
    else:
        return render_to_response('gui/front_page.html', {'is_logged_in': is_logged_in(request)},
            context_instance=RequestContext(request))

def configuration_form(request):
    if is_logged_in(request) is False:
        return render_to_response('users/signup.html', {'is_logged_in': is_logged_in(request)},
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
    return render_to_response('template/404.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))

def my_custom_500_view(request):
    return render_to_response('template/500.html', {'is_logged_in': is_logged_in(request)},
        context_instance=RequestContext(request))

