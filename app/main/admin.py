from django.contrib import admin

from .models import *


class ModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ModelAdmin, self).__init__(model, admin_site)


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'operating_hours_start', 'operating_hours_end', 'contact_number', 'total_showtimes']

    def total_showtimes(self, obj):
        return Showtime.objects.filter(hall__cinema=obj).count()

    total_showtimes.short_description = 'Total Showtimes'


class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'base_price', 'total_showtimes']

    def total_showtimes(self, obj):
        return Showtime.objects.filter(film=obj).count()

    total_showtimes.short_description = 'Total Showtimes'


class HallAdmin(admin.ModelAdmin):
    list_display = ['seating_capacity', 'total_showtimes', 'total_tickets_sold']

    def total_showtimes(self, obj):
        return Showtime.objects.filter(hall=obj).count()

    def total_tickets_sold(self, obj):
        return Ticket.objects.filter(showtime__hall=obj).count()

    total_showtimes.short_description = 'Total showtimes'
    total_tickets_sold.short_description = 'Tickets Sold'


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_films']

    def total_films(self, obj):
        return FilmGenre.objects.filter(genre=obj).count()

    total_films.short_description = 'Total films'


class SellerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'total_tickets_sold']

    def total_tickets_sold(self, obj):
        return Ticket.objects.filter(seller=obj).count()

    total_tickets_sold.short_description = 'Tickets sold'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'total_tickets_purchased']

    def total_tickets_purchased(self, obj):
        return Ticket.objects.filter(customer=obj).count()

    total_tickets_purchased.short_description = 'Tickets purchased'


class ProductionCountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'total_films']

    def total_films(self, obj):
        return Film.objects.filter(productioncountry=obj).count()

    total_films.short_description = 'Films Total'


admin.site.register(Country, ModelAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(FilmGenre, ModelAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(ProductionCountry, ProductionCountryAdmin)
admin.site.register(Seat, ModelAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Showtime, ModelAdmin)
admin.site.register(Ticket, ModelAdmin)
admin.site.register(Cinema, CinemaAdmin)
