from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt,name='dispatch')
class CandidateAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Candidate.objects.get(id=id)
            serializer = CandidateSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Candidate.objects.all()
        serializer = CandidateSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json') 


    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CandidateSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    def put(self,request,*args,**kwargs):
        json_data =  request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Candidate.objects.get(id = id)
        serializer = CandidateSerializer(stu,data = pythondata,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type = 'application/json')


    def delete(self,request,*args,**kwargs):
        json_data =  request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Candidate.objects.get(id = id)
        stu.delete()
        res = {'msg':'Data Deleted !!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')
