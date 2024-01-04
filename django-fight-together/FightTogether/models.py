from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)

    like_posts = models.ManyToManyField('Blog', blank=True, related_name='like_users')
    like_posts1 = models.ManyToManyField('Incident', blank=True, related_name='like_users')
    like_posts2 = models.ManyToManyField('Love', blank=True, related_name='like_users')
    like_posts3 = models.ManyToManyField('Politics', blank=True, related_name='like_users')
    like_posts_refute = models.ManyToManyField('Refute', blank=True, related_name='like_users')
    def __str__(self):
        return self.nickname

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()


    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Refute(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()


    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Love(models.Model): #연애와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()


    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Politics(models.Model): #정치/사회와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()


    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Incident(models.Model): #사건/사고와 관련된 디비
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length = 50,null = True)
    body = models.TextField()
    

    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
