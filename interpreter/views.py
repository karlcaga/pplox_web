from django.shortcuts import render
from pplox.scanner import Scanner

# Create your views here.
def index(request):
    context = {
        'output': "Hello World",
    }
    return render(request, 'index.html', context=context)

def runcode(request):
    if request.method == 'POST':
        scanner = Scanner(request.POST.get("code"))
        output = ""
        for token in scanner.scan_tokens():
            output += token.to_string()
        context = {"output" : output}
        return render(request, 'index.html', context=context)
