from django.shortcuts import render
from django.contrib import messages
from .forms import InputForm
import math
import socket

def calculator_view(request):
    context = {'form': InputForm()}

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                messages.info(request, f"Input 'a' ({a}) is too small.")
            if b == 0:
                messages.info(request, "Input 'b' is 0 and will not affect the result.")
            if c < 0:
                messages.error(request, f"Error: Input 'c' ({c}) is negative.")
            else:
                c_cubed = c ** 3
                sqrt_val = math.sqrt(c_cubed)
                if c_cubed > 1000:
                    intermediate = sqrt_val * 10
                else:
                    intermediate = sqrt_val / a
                final_result = intermediate + b
                context['result'] = final_result
        else:
            messages.error(request, "Error: All inputs must be numeric.")

        context['form'] = form

    context['host'] = socket.gethostname()
    return render(request, 'calculator/result.html', context)
