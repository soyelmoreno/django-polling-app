from django.db import models

# Each model is represented by a class that subclasses `django.db.models.Model`.

# Each class variable represents a database field in the model.

class Question(models.Model):
    # The name of each Field instance (e.g. question_text or pub_date) is the
    # field's name, in machine-friendly format. You'll use this value in your
    # Python code, and your database will use it as the column name.
    question_text = models.CharField(max_length=200)

    # You can use an optional first positional argument to a Field to designate
    # a human-readable name.
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
