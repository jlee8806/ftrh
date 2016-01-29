from django.contrib import admin

# Register your models here.
from .models import user
from .models import game

# class PostModelAdmin(admin.ModelAdmin):
# 	list_display = ["username", "email"]



# 	class Meta:
# 		model = game
		

admin.site.register(game)
admin.site.register(user)