# File: views.py
# Author: Jocelyn Chan (jchan042@bu.edu) 2/3/2026
# Description: View page for the restaurant app

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# list for items 
special = ['Hot Udon ($17)', 'Spicy Cold Niku Udon ($17)', 'Spicy Hot Udon ($17)', 'Cold Niku Udon ($17)']

# Create your views here.

# main view
def main(request):
    """View for the default and main page"""
    
    # directs to the main.html page 
    template = 'restaurant/main.html'
    
    return render(request, template)

# order view 
def order(request):
    """View for the order form page"""
    
    template = 'restaurant/order.html'
    
    context = {
        'daily_item': random.choice(special),
    }
    
    return render(request, template, context)


# confirmation view
def confirmation(request):
    """View for the confirmation page after submitting the form"""
    
    template = 'restaurant/confirmation.html'
    
    ordered_items = []
    total = 0

    # Default confirmation message
    message = "Thank you for choosing Yume Ga Arukara"
    
    # Menu Items 
    if request.POST.get("tempura"):
        ordered_items.append("Tempura Udon ($18)")
        total += 18

    if request.POST.get("tofu"):
        ordered_items.append("Agedashi Tofu ($12)")
        total += 12

    if request.POST.get("soba"):
        ordered_items.append("Biang Biang Mazesoba ($18)")
        total += 18

    if request.POST.get("yuzu"):
        ordered_items.append("Yuzu Shio Udon ($18)")
        total += 18

        # Yuzu additional options
        if request.POST.get("yuzu-chicken"):
            ordered_items.append("  + Extra Chicken ($3)")
            total += 3

        if request.POST.get("yuzu-shrimp"):
            ordered_items.append("  + Extra Shrimp ($4)")
            total += 4

        if request.POST.get("yuzu-nori"):
            ordered_items.append("  + Extra Nori ($3)")
            total += 3

    # Daily Special 
    if request.POST.get("special"):
        special_item = request.POST.get('special') # get the same daily special
        ordered_items.append(special_item)
        total += 17 # special is always 17 dollars

    # Special instructions
    instructions = request.POST.get("instructions")

    # Customer info
    name = request.POST.get("name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")

    # Ready time: 30–60 minutes from now
    minutes = random.randint(30, 60)
    ready_time = time.strftime(
        "%I:%M %p",
        time.localtime(time.time() + minutes * 60)
    )

    context = {
        "name": name,
        "phone": phone,
        "email": email,
        "ordered_items": ordered_items,
        "total": total,
        "time": ready_time,
        "instructions": instructions,
    }

    return render(request, template, context)