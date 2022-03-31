import datetime
from django.http import HttpResponse
from addr.models import TestTable


def index(request):
    # x = TestTable.objects.all()
    TestTable.objects.create(val=str(datetime.datetime.now()))
    return HttpResponse(TestTable.objects.values())
    # return HttpResponse('Hello')
