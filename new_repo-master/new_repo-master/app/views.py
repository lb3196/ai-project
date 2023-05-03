from django.shortcuts import render

def admin_info(request):
    return render(request, 'admin_info.html')

def admin_page(request):
    return render(request, 'admin_page.html')

def candidate_info(request):
    return render(request, 'candidate_info.html')

def candidate(request):
    return render(request, 'candidate.html')

def format(request):
    return render(request, 'format.html')

def index(request):
    return render(request, 'index.html')

def score(request):
    return render(request, 'score.html')

def test(request):
    return render(request, 'test.html')
