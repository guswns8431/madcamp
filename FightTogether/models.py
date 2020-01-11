from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Love(models.Model): #연애와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Politics(models.Model): #정치/사회와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Incident(models.Model): #사건/사고와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]