from django.db import models

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    apt = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    def __str__(self):
        return self.username
    def user_addr(self):
        return ', '.join([' '.join([self.street, self.apt]), self.city, ' - '.join([self.state, self.zipcode])] )


class Shelf(models.Model):
    #shelfid = models.AutoField(primary_key=True)
    shelftype = models.CharField(max_length=1)
    userid = models.ForeignKey(User)
    def __str__(self):
        return self.shelf_id()
    def shelf_id(self):
        return '_'.join([str(userid), shelftype])
    class Meta:
        unique_together = (("userid", "shelftype"),)


class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class ShelfContainsBook(models.Model):
    shelfid = models.ForeignKey(Shelf)
    bookid = models.ForeignKey(Book)
    class Meta:
        unique_together = (("shelfid", "bookid"),)
