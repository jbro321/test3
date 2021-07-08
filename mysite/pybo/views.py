from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 매우 환영합니다.")