import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class FoodModel(models.Model):
    title = models.CharField(verbose_name="Title", max_length=222)
    about = models.TextField(verbose_name="About")
    price = models.FloatField(verbose_name="Price",
                              validators=[
                                  MinValueValidator(0),
                                  MaxValueValidator(100)]
                              )
    exclusive = models.BooleanField(verbose_name="Exclusive", default=False)
    image = models.ImageField(verbose_name="Image", upload_to="food_images/")
    category = models.ManyToManyField('CategoryModel', verbose_name="Category",)
    tags = models.ManyToManyField('TagsModel', verbose_name="Tags", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class TagsModel(models.Model):
    tag = models.CharField(verbose_name='Tag', max_length=100)

    def __str__(self):
        return self.tag


class CategoryModel(models.Model):
    category_name = models.CharField(verbose_name="Category name", max_length=222)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['created']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ChefModel(models.Model):
    full_name = models.CharField(verbose_name="Full name", max_length=222)
    picture = models.ImageField(verbose_name="Picture", upload_to="chefs/")
    level = models.ForeignKey('ChefLevel', verbose_name="Level", on_delete=models.CASCADE)
    facebook = models.URLField(verbose_name="Facebook", max_length=255, blank=True, null=True)
    x_twitter = models.URLField(verbose_name="X", max_length=255, blank=True, null=True)
    instagram = models.URLField(verbose_name="Instagram", max_length=255, blank=True, null=True)
    skype = models.URLField(verbose_name="Skype", max_length=255, blank=True, null=True)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'


class ChefLevel(models.Model):
    ch_level = models.CharField(verbose_name="Chef level", max_length=222)

    def __str__(self):
        return self.ch_level


def past_date_validator(value):
    if value < datetime.date.today():
        raise ValidationError('The date cannot be in the past. ')
    return value


def past_time_validator(value):
    current_time = datetime.datetime.now()

    if value.hour < current_time.hour and current_time.date() == datetime.date.today():
        raise ValidationError('The date cannot be in the past for today.')
    return str(value)


class BookingModel(models.Model):
    name = models.CharField(verbose_name="Booking name", max_length=222)
    email = models.EmailField(verbose_name="Email", max_length=255, blank=True, null=True)
    num_of_g = models.IntegerField(verbose_name="Number of guests", default=0)
    phone_number = models.CharField(verbose_name="Phone number", max_length=13)
    date = models.DateField(verbose_name="Date", validators=[past_date_validator])
    time = models.TimeField(verbose_name="Time", validators=[past_time_validator])
    note = models.TextField(verbose_name="Your Note", blank=True, null=True)

    def __str__(self):
        return self.name
