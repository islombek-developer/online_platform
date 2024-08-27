from rest_framework import serializers
from .models import Comment,Course,Lesson,Teacher,LikeVideo

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class Commentserializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class Lessonserializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class Courseserializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class Emailserializers(serializers.Serializer):
    subject = serializers.CharField(max_length=155)
    massage = serializers.CharField()

class LikeVideserializers(serializers.ModelSerializer):
    class Meta:
        model = LikeVideo
        fields = "__all__"