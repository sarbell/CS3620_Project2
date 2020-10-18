from django.db import models


# Create your models here.
class Lib(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    text = models.TextField(default="This is a bad mad lib because it isn't one.")
    noun = models.IntegerField(default=0)
    plural_noun = models.IntegerField(default=0)
    body_part = models.IntegerField(default=0)
    accessory = models.IntegerField(default=0)
    clothing_item = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    feeling = models.IntegerField(default=0)
    car_name_or_type = models.IntegerField(default=0)
    spice = models.IntegerField(default=0)
    time_of_day = models.IntegerField(default=0)
    unit_of_measurement = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    exclamation = models.IntegerField(default=0)
    unit_of_time = models.IntegerField(default=0)
    nickname = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    large_number = models.IntegerField(default=0)
    name_of_famous_person = models.IntegerField(default=0)
    adjective = models.IntegerField(default=0)
    adverb = models.IntegerField(default=0)
    verb = models.IntegerField(default=0)
    verb_ending_in_ing = models.IntegerField(default=0)



class List(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=500)
    template = models.CharField(max_length=200, default="home")
