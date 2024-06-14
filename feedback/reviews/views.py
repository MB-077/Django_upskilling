from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect

def review(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        
        if entered_username == "" and len(entered_username) >= 100:
            return render(request, 'reviews/review.html', {"has_error": True})
        
        print(entered_username)
        return HttpResponseRedirect('/thank-you')
        
    return render(request, 'reviews/review.html')


def thank_you(request):
    return render(request, 'reviews/thank_you.html', {"has_error": False})