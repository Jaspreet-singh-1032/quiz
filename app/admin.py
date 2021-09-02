from django.contrib import admin

# Register your models here.
from .models import (
    Quiz,
    Question,
    Option
)


admin.site.register((Quiz , Question , Option))