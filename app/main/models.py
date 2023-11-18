# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cinema(models.Model):
    cinema_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    operating_hours_start = models.DateTimeField()
    operating_hours_end = models.DateTimeField()
    contact_number = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'cinema'


class Country(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    contact_number = models.CharField(max_length=12, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    base_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'film'


class FilmGenre(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)  # The composite primary key (film_id, genre_id) found, that is not supported. The first column is selected.
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'film_genre'
        unique_together = (('film', 'genre'),)


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'genre'


class Hall(models.Model):
    hall_id = models.IntegerField(primary_key=True)
    seating_capacity = models.IntegerField()
    cinema = models.ForeignKey(Cinema, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hall'


class ProductionCountry(models.Model):
    film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)  # The composite primary key (film_id, country_id) found, that is not supported. The first column is selected.
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'production_country'
        unique_together = (('film', 'country'),)


class Seat(models.Model):
    seat_id = models.IntegerField(primary_key=True)
    seat_number = models.IntegerField()
    row_number = models.IntegerField()
    class_coefficient = models.FloatField()
    hall = models.ForeignKey(Hall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seat'


class Seller(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    seller_id = models.IntegerField(primary_key=True)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=30)
    cinema = models.ForeignKey(Cinema, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seller'


class Showtime(models.Model):
    showtime_id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hall = models.ForeignKey(Hall, models.DO_NOTHING)
    film = models.ForeignKey(Film, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'showtime'


class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    purchase_date = models.DateField(blank=True, null=True)
    price = models.FloatField()
    status = models.CharField(max_length=30)
    seller = models.ForeignKey(Seller, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    showtime = models.ForeignKey(Showtime, models.DO_NOTHING)
    seat = models.ForeignKey(Seat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket'
