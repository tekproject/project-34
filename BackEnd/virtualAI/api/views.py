from rest_framework.decorators import api_view 
from rest_framework.response import Response
from api.models import Url, BookMark, CustomUser
from api.serializers import BookMarkSerializer, CustomUserSerializer, UrlSerializer, CreateBookMarkSerializer, ChangePasswordSerializer
from rest_framework import status

@api_view(['GET'])
def home(request):
    data = {'message': 'Hello from the API'}
    return Response(data)

@api_view(['GET'])
def urlList(request):
    url = Url.objects.exclude(private=True)
    serializer = UrlSerializer(url, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def myBookMarks(request):
    user = CustomUser.objects.get(id=request.user.id)
    bookmarks = BookMark.objects.filter(user=user)
    serializer = BookMarkSerializer(bookmarks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['GET','POST'])
def urlCreate(request):
    if request.method =='POST':
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = UrlSerializer()
    return Response(serializer.data)


@api_view(['GET','POST'])
def bookmarkCreate(request):
    if request.method =='POST':
        serializer = CreateBookMarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = CreateBookMarkSerializer()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def userEntry(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = CustomUserSerializer()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def userUpdate(request):
    '''Password is required User should give the same password stored in db'''
    user = CustomUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        serializer = CustomUserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def passwordUpdate(request):
    '''Password is required User should give the same password stored in db'''
    user = CustomUser.objects.get(id=request.user.id)
    serializer = ChangePasswordSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)