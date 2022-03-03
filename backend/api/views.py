from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.generics import ListAPIView

from .serializers import TestSerializer
from .models import TestModel

# Create your views here.
@csrf_exempt 
def test_view(request):
    return HttpResponse("Hello world!")

class TestView(ListAPIView):
    model = TestModel
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()

