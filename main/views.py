from django.shortcuts import render

def index(request):
    # DB를 사용하지 않으므로, 단순히 index.html 파일을 보여줍니다.
    return render(request, 'index.html')