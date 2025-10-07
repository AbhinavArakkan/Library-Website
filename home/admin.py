from django.contrib import admin
from django.utils.html import format_html
from .models import Member, Image, NewsItem

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'img']
    search_fields = ['name', 'position']
    list_filter = ['position']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'image_preview']
    search_fields = ['id']
    
    def image_preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;"/>',
                obj.img.url
            )
        return '-'
    image_preview.short_description = 'Preview'

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['headline', 'uploaded_date', 'image_preview']
    search_fields = ['headline', 'content']
    list_filter = ['uploaded_date']
    date_hierarchy = 'uploaded_date'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 5px;"/>',
                obj.image.url
            )
        return '-'
    image_preview.short_description = 'Preview'

    