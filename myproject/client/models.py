from django.db import models

class Profile(models.Model):
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    country = models.ForeignKey(
        "Country", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(
        'State', blank=True, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(
        "City", on_delete=models.SET_NULL, null=True, blank=True)
    street = models.ForeignKey(
        'Street', on_delete=models.SET_NULL, null=True, blank=True)

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class State(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]


class Street(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-name"]# Create your models here.
