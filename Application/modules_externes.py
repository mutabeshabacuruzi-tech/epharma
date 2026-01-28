from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

def verification_de_session():
    def intern(vue):
        @wraps(vue)
        def __vue_decore(request, *args, **kwargs):
            if not 'user' in request.session:
                messages.error(request, "! Une erreur de session")
                return redirect(reverse('acc'))
            return vue(request, *args, **kwargs)
        return __vue_decore
    return intern