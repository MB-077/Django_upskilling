from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'
    
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context

class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review
    
    
# V3
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = 'reviews/review.html'
#     success_url = '/thank-you'
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
# V2
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {"form": form})
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
        
#         return render(request, 'reviews/review.html', {"form": form})
    
# V2
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank_you.html', {"has_error": False})
    
# V2
# class ReviewListView(TemplateView):
#     template_name = 'reviews/review_list.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context

# V2
# class SingleReviewView(TemplateView):
#     template_name = 'reviews/single_review.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context
    
    
    
# V1
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             # review = Review(
#             #     user_name = form.cleaned_data['user_name'],
#             #     review_text = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating'])
#             # review.save()
#             # print(form.cleaned_data)
#             return HttpResponseRedirect('/thank-you')
        
#     #     entered_username = request.POST['username']
        
#     #     if entered_username == "" and len(entered_username) >= 100:
#     #         return render(request, 'reviews/review.html', {"has_error": True})
        
#     #     print(entered_username)
#     #     return HttpResponseRedirect('/thank-you')
    
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {"form": form})

# def thank_you(request):
#     return render(request, 'reviews/thank_you.html', {"has_error": False})