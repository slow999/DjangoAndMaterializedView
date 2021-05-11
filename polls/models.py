from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(null=True, default=None)


class Question2021(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField(null=True, default=None)

    class Meta:
        managed = False
        db_table = 'polls_question_materialized_view_2021'

