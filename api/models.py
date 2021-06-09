from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    dob = models.DateField(auto_created=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(verbose_name='description', null=True)
    created_date = models.DateField(auto_now=True)
    url = models.URLField(verbose_name='url', null=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='question')
    choice1 = models.TextField(verbose_name='choice1', null=True)
    choice2 = models.TextField(verbose_name='choice2', null=True)
    choice3 = models.TextField(verbose_name='choice3', null=True)
    choice4 = models.TextField(verbose_name='choice4', null=True)
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.question
