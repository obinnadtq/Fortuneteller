from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
    fort = random.choice(fortunelist)
    context = {"fortune": fort}
    return render(request, "randomfortune/fortune.html", context)


fortunelist = [
    "All will go well with your new project.",
    "If you continually give, you will continually have.",
    "Self-knowledge is a life long process.",
    "You are busy, but you are happy.",
    "Your abilities are unparalleled.",
    "Those who care will make the effort.",
    "Now is the time to try something new.",
    "Miles are covered one step at a time.",
    "Don’t just think, act!"
]
