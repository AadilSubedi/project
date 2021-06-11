from django.contrib import admin

from .models import Category, Clothing
# Register your models here.

# admin.site.register(Category)

# admin.site.register(Clothing)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('image','category','name','slug','price','available','created','updated')
    list_filter = ['available','created','updated']
    list_editable = ['price','available']

    prepopulated_fields = {'slug':('name',)}