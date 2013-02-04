# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from movies.models import Movie, Code, User, Static
from multimedia.utils import *
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import simplejson as json

def is_logged_in(request):
    try:
        my_return = request.session['is_logged_in']
    except:
        my_return = False;
    return my_return

def forgot_password(request):
    logged = is_logged_in(request)
    request.session['last_visited_movie'] = None
    return render_to_response('movies/forgot_password.html',context_instance=RequestContext(request))

@require_http_methods(["POST"])
def process_create_account(request):
    s = get_object_or_404(Static, pk=5)
    try:
        u = User.objects.filter(email=request.POST['email'])
    except:
        u = False # user does not exist in database
    if u:
        return render_to_response('movies/signup.html', {'error_message': "Email is already taken",'code': request.POST['code_1']},context_instance=RequestContext(request))
    u = User(email=request.POST['email'],password=request.POST['password'])
    u.save()
    from django.core.mail import send_mail
    send_mail('Registration Complete', 'This message confirms that your registration at http://movies.chooseinteresting.com/ is complete', 'noreply@mobovivo.com', [request.POST['email']])
    request.session['is_logged_in'] = True
    request.session['email'] = request.POST['email']
    # code
    try:
        c = Code.objects.get(code_key=request.POST['code_1'])
    except:
        c = False
    if c:
        if c.user is None:
            c.user = u
            c.save()
            if request.session['last_visited_movie'] is not None:
                return redirect('/enjoy-the-show/'+ request.session['last_visited_movie'] +'/',False)
            return redirect('/',False)
        else:
            # code is taken
            return render_to_response('movies/frontpage.html',
                {'static': s,
                 'is_logged_in':is_logged_in(request),
                 'code_error_message':"Code Is In Use",
                 },context_instance=RequestContext(request))
    else:
        # code is invalid
        if request.POST['code_1']:
            return render_to_response('movies/frontpage.html',
                {'static': s,
                 'is_logged_in':is_logged_in(request),
                 'code_error_message':"Code is invalid",
                 },context_instance=RequestContext(request))
    return redirect('/',False)

@require_http_methods(["POST"])
def process_sign_up(request):
    try:
        u = User.objects.get(email=request.POST['email_2'],password=request.POST['password_2'])
    except:
        u = False # user does not exist in database
    if u:
        request.session['is_logged_in'] = True
        request.session['email'] = request.POST['email_2']
    else:
        return render_to_response('movies/signup.html', {'error_message': "Email and Password Don't Match",'code': request.POST['code_2']},context_instance=RequestContext(request))
        # code
    try:
        c = Code.objects.get(code_key=request.POST['code_2'])
    except:
        c = False
    if c:
        if c.user is None:
            c.user = u
            c.save()
            if request.session['last_visited_movie'] is not None:
                return redirect('/enjoy-the-show/'+ request.session['last_visited_movie'] +'/',False)
    return redirect('/',False)