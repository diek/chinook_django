from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Album(models.Model):
    title = models.CharField(max_length=160),
    artist = models.ForeignKey(Artist, models.PROTECT)


class Composer(models.Model):
    composer = models.CharField(max_length=30)

    def __str__(self):
        return self.composer

    class Meta:
        ordering = ('composer',)


class MediaType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Track(models.Model):
    title = models.CharField(max_length=200)
    composer = models.ManyToManyField(Composer)
    album = models.ForeignKey(Album, models.PROTECT)
    media_type = models.ForeignKey(MediaType, models.PROTECT)
    genre = models.ForeignKey(Genre, models.PROTECT)
    composer_name = models.CharField(max_length=220),
    milliseconds = models.PositiveSmallIntegerField()
    byte = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
