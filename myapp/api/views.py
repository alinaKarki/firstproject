

from myapp.api.serializers import StudentSerializer
from myapp.models import Student
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet

# @csrf_exempt
# def student_list(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'GET':
#         data = Student.objects.all()
#         serializer = StudentSerializer(data, many=True)
#         return JsonResponse(serializer.data, status=201, safe=False)
    
# @csrf_exempt
# def student(request, pk):
#     if request.method == 'PUT':
#         qs = Student.objects.get(id=pk)
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(qs,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'GET':
#         data = Student.objects.get(id=pk)
#         serializer = StudentSerializer(data)
#         return JsonResponse(serializer.data, status=201, safe=False)
    
#     elif request.method == 'DELETE':
#         data = Student.objects.get(id=pk)
#         data.delete()
#         return JsonResponse({"id":pk}, status=201, safe=False)
    
class student_list(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentViewset(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
