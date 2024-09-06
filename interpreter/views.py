from django.shortcuts import render
from pplox.scanner import Scanner
from pplox.parser import Parser, ParseError
from pplox.ast_printer import AstPrinter
from pplox.interpreter import Interpreter, to_string

# Create your views here.
def index(request):
    context = {
        'output': "Hello World",
    }
    return render(request, 'index.html', context=context)

def runcode(request):
    if request.method == 'POST':
        scanner = Scanner(request.POST.get("code") + ";")
        output = ""
        tokens = scanner.scan_tokens()
        for token in tokens:
            output += token.to_string() + "\n"
        parser = Parser(tokens)
        statements = parser.parse()
        for i, statement in enumerate(statements):
            try:
                output += AstPrinter().print(statement.expression) + "\n"
                interpreter = Interpreter()
                output += to_string(interpreter.evaluate(statement.expression)) + "\n"
            except:
                output += "Could not print statement " + str(i+1) + ".\n"
        context = {"output" : output}
        return render(request, 'index.html', context=context)
    