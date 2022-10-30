from django.contrib import admin
from .models import Rubric, Article
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Article)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)