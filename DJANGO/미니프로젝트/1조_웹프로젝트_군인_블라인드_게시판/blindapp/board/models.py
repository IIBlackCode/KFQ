from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model) :
    userid=models.CharField(max_length=50,unique=True)
    pw=models.CharField(max_length=300)
    signdate=models.DateTimeField()
    expiredate=models.DateTimeField()
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    auth=models.CharField(max_length=50)


class Board(models.Model) :
    boardid=models.IntegerField(primary_key=True)
    boardname=models.CharField(max_length=50)
    cre_date=models.DateTimeField()

class Boardcontent(models.Model) :
    boardcontentid=models.IntegerField(primary_key=True)
    boardid=ForeignKey('Board',related_name='category',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    userid=models.ForeignKey('User',related_name='posted_name',on_delete=CASCADE)
    hit=models.IntegerField()
    isnotice=models.BooleanField()
    content=models.TextField()

class Bookmark(models.Model) :
    boardcontentid=models.ForeignKey('Boardcontent',related_name='bookmark_on',on_delete=CASCADE)
    userid=models.ForeignKey('User',related_name='bookmarked_by',on_delete=CASCADE)

class Like(models.Model) :
    # boardcontentid=models.ForeignKey('Boardcontent',related_name='like_or_dislike_this',on_delete=CASCADE)
    boardcontentid=models.ForeignKey(Boardcontent,on_delete=CASCADE)
    cipherid=models.ForeignKey('User',related_name='who_like',on_delete=CASCADE)
    like=models.BooleanField()

class Chatroom(models.Model) :
    chatroomid=models.IntegerField(primary_key=True)
    chatroomname=models.CharField(max_length=50)
    cre_date=models.DateTimeField()


class Chatusers(models.Model) :
    chatroomid=models.ForeignKey('Chatroom',related_name='where_in',on_delete=CASCADE)
    chatroomname=models.CharField(max_length=25)
    cre_date=models.DateTimeField()

class Chat(models.Model) :
    chatid=IntegerField(primary_key=True)
    chatroomid=models.ForeignKey('Chatroom',related_name='where_talk',on_delete=RESTRICT)
    userid=models.ForeignKey('User',related_name='who_chatted',on_delete=RESTRICT)

class Reply(models.Model) :
    replyid=models.IntegerField(primary_key=True)
    boardcontentid=ForeignKey('Boardcontent',related_name='where_replied',on_delete=CASCADE)
    userid=models.ForeignKey('User',related_name='who_id_replied',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    reply=models.TextField()

class Rereply(models.Model) :
    rereplyid=models.IntegerField(primary_key=True)
    replyid=ForeignKey('Reply',related_name='where_rereplied',on_delete=CASCADE)
    cre_date=models.DateTimeField()
    userid=models.ForeignKey('User',related_name='who_name_rereplied',on_delete=CASCADE)
    rereply=models.TextField()

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="", null=True,blank=True)

    def __str__(self):
        return self.title    


