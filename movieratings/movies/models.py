from django.db import models

# Create your models here.

class Rater(models.Model):
    age = models.IntegerField()
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return "Rater {}".format(self.id)

class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return "{} / {}".format(self.movie, self.rater)
