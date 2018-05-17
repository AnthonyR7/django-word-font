from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request,"new_word/index.html")
def process(request):
    request.session['choose_color'] = request.POST.get('choose_color')
    #if statement
    if request.POST.get('red',False) == True:
        for word in request.session['choose_color']:
            word  = word.format('color:red')
            
    elif request.POST.get('blue',False) == True:
        for word in request.session['choose_color']:
            word  = word.format('color:blue')
    else:
        for word in request.session['choose_color']:
            word  = word.format('color:green')
    #if the box was checked for font
    if request.POST.get('word_size',False) == True:
        request.session['shape'] = "up"
    #The idea is to increase font-size if up is
    #present in request.session['shape'] in html
    else:
        request.session['shape'] = "down"

    return redirect('/result')

def result(request):
    context = {
        'name': request.session['choose_color'],
        'shape': request.session['shape'],
    }
    return render(request, 'new_word/index.html', context)
