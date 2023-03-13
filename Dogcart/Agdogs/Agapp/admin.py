from django.contrib import admin
from .models import Dogs,DogsBreed

@admin.register(Dogs)
class DogsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'breed', 'age', 'price', )


@admin.register(DogsBreed)
class DogsBreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'breed' )
    
