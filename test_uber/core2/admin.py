from django.contrib import admin
from core2.models import Test_model1

@admin.register(Test_model1)
class Test1_Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'count'
    )
# Register your models here.
