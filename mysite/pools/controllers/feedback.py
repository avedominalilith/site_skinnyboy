
from django.shortcuts import redirect
from pools.models import Feedback

def create(request):

    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.text = request.POST.get("text")
    feedback.save()

    return redirect("/")