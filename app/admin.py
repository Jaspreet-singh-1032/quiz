from django.contrib import admin

# Register your models here.
from .models import (
    Quiz,
    Question,
    Option,
    Answer
)


admin.site.register((Quiz , Question , Option, Answer))