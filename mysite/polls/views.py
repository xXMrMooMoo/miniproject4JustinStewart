### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 4

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages





def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def register(request):
    if request.method == "POST":
        print("Form submitted")  # Debug: Confirm POST request
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug: Confirm form validation
            form.save()
            messages.success(request, "User created successfully!")
            return redirect("polls:login")
        else:
            print("Form is invalid")  # Debug: Print validation errors
            print(form.errors)  # Debug: Print form errors
    else:
        form = UserCreationForm()

    return render(request, "polls/register.html", {"form": form})

def home(request):
    # Render the fancy home page
    return render(request, "polls/home.html")



class CustomLoginView(LoginView):
    template_name = 'polls/login.html'

    def form_valid(self, form):
        messages.success(self.request, "You are now logged in!")  # Add toast message
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass a modal message to the template
        if self.request.method == "POST":
            context['modal_message'] = "You are now logged in!" if self.request.user.is_authenticated else "Invalid login credentials. Please try again."
        return context

