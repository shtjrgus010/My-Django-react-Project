from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("user", "short_payload", "created_at", "updated_at")
    
    def short_payload(self, obj):
        return obj.payload[:10]
    short_payload.short_description="payload"
    
    

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet", "created_at", "updated_at")