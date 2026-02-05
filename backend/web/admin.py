from django.contrib import admin

# Register your models here.
from web.models.user import UserProfile

from web.models.character import Character


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)  # 逗号不能删，保证传的是列表


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ("author",)
