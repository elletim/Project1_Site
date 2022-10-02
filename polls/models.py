from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
class Url(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    url_text = models.CharField(max_length=500)
    def __str__(self):
        return self.url_text