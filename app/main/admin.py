from django.contrib import admin

from .models import *


class ModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ModelAdmin, self).__init__(model, admin_site)


admin.site.register(Cinema, ModelAdmin)
admin.site.register(Country, ModelAdmin)
admin.site.register(Customer, ModelAdmin)
admin.site.register(Film, ModelAdmin)
admin.site.register(FilmGenre, ModelAdmin)
admin.site.register(Genre, ModelAdmin)
admin.site.register(Hall, ModelAdmin)
admin.site.register(ProductionCountry, ModelAdmin)
admin.site.register(Seat, ModelAdmin)
admin.site.register(Seller, ModelAdmin)
admin.site.register(Showtime, ModelAdmin)
admin.site.register(Ticket, ModelAdmin)
