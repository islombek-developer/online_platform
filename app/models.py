from django.db import models
from django.core.validators import FileExtensionValidator 
from django.contrib.auth.models import User

class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    program = models.ForeignKey(Program,on_delete=models.CASCADE,related_name='salom')
    author = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.program.name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'mp3', 'AVI', 'WMV'])
    ])

    def __str__(self) -> str:
        return self.title


    
class Comment(models.Model):
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description   

class LikeVideo(models.Model):
    author = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    video_model = models.ForeignKey(Lesson,on_delete=models.SET_NULL,null=True)
    like_or_dislike = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.video_model.title
