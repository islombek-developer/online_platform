from django.conf import settings
from django.core.mail import send_mail

from rest_framework import generics, filters,permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import (Commentserializers,Userserializers,LikeVideserializers,
                          Courseserializers,Lessonserializers,Emailserializers)
from .permissions import CoursePermission,CastomPermission
from .models import Comment,Course,Lesson,Teacher,LikeVideo,User

class UserView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = Userserializers
    permission_classes = [CastomPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Courseserializers
    permission_classes = [CoursePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class LessonView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = Lessonserializers
    permission_classes = [CastomPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']



class EmailView(APIView):
    def post(self,request:Request):

        serializer = Emailserializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_users=[]

        for user in users:
            email_users.append(user.email)
        email_users.append('islombekbotiraliyev1@gmail.com')


        send_mail(
            serializer.validated_data.get('subject'),
            serializer.validated_data.get('massage'),
            settings.EMAIL_HOST_USER,
            email_users,
            fail_silently=False,
        )
        return Response({"massage":"success"})

class LikesView(APIView):

    def get(self, request,pk):
        likes = len(LikeVideo.objects.filter(like_or_dislike=True,video_model_id=pk))
        dislikes = len(LikeVideo.objects.filter(like_or_dislike=False,video_model_id=pk))
        return Response({'likes':likes,'dislikes': dislikes})


    # def delete(self, request, pk, *args, **kwargs):
    #     try:
    #         like = LikeVideo.objects.get(pk=pk)
    #         like.delete()
    #         return Response({"massage":"like ochirildi"})
    #     except :
    #         return Response({'massage': 'Like topilmadi'})


class LikecreateView(APIView):
    def post(self, request):
        try:
            likes_or_dislikes = LikeVideo.objects.filter(author_id=request.data.get("author"))
            for lord in likes_or_dislikes:
                lord.delete()
        except:
            pass

        serializer = LikeVideserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()
        return Response(LikeVideserializers(like_or_dislike).data)