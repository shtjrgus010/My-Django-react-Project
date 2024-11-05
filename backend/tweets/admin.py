from django.contrib import admin
from .models import Tweet, Like

class WordFilter(admin.SimpleListFilter):
    
    title = "Filter by Elon"
    
    parameter_name = "elon_musk"
    
    def lookups(self, request, model_admin):
        return [
            ("elon_musk", "Contains Elon Musk"),
            ("not_elon_musk", "Not contain Elon Musk"),
        ]
        
    def queryset(self, request, payloads):
        word = self.value()
        if word == "elon_musk":
            return payloads.filter(payload__contains="Elon Musk")
        elif word == "not_elon_musk":
            return payloads.exclude(payload__contains="Elon Musk")
        else:
            return payloads

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "short_payload",
        "like_count",
        "created_at",
        "updated_at",
    )
    
    list_filter = (
        WordFilter,
        "created_at",
    )
    
    search_fields = (
        "payload",
        "user__username",
    )

    
    def short_payload(self, obj):
        return obj.payload[:10]

    short_payload.short_description = "payload"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )
    
    list_filter = (
        "created_at",
    )
    
    search_fields = (
        "user__username",
    )
