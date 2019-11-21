from django.contrib import admin
from core1.models import Test_model2

@admin.register(Test_model2)
class Test2_Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'len'
    )
# Register your models here.
