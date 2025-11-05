from django.contrib import admin
from .models import Skill, Technology, Project, Screenshot, Formation, ContactInfo


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('order', 'name')


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'color')
    search_fields = ('name',)
    ordering = ('name',)


class ScreenshotInline(admin.TabularInline):
    model = Screenshot
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'is_featured', 'order', 'created_at')
    list_filter = ('project_type', 'is_featured', 'created_at')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'subtitle', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('technologies',)
    inlines = [ScreenshotInline]
    ordering = ('order', '-created_at')

    fieldsets = (
        ('Informations de base', {
            'fields': ('title', 'subtitle', 'slug', 'project_type')
        }),
        ('Description', {
            'fields': ('short_description', 'full_description')
        }),
        ('Médias', {
            'fields': ('cover_image', 'header_image', 'video_demo')
        }),
        ('Technologies et caractéristiques', {
            'fields': ('technologies', 'features')
        }),
        ('Métadonnées', {
            'fields': ('is_featured', 'order'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Screenshot)
class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'order')
    list_filter = ('project',)
    list_editable = ('order',)
    ordering = ('project', 'order')


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'is_active', 'order')
    list_filter = ('is_active',)
    list_editable = ('is_active', 'order')
    search_fields = ('title', 'description')
    ordering = ('order', 'title')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'whatsapp')

    def has_add_permission(self, request):
        # Ne permettre qu'une seule instance
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Ne pas permettre la suppression
        return False


# Personnalisation de l'admin
admin.site.site_header = "Administration Portfolio Urbain Balogou"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Gestion du portfolio"
