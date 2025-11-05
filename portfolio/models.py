from django.db import models
from django.utils.text import slugify

class Skill(models.Model):
    """Compétences techniques"""
    name = models.CharField(max_length=100, verbose_name="Nom")
    icon = models.CharField(max_length=50, verbose_name="Icône Font Awesome",
                           help_text="Ex: fa-brands fa-python")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Technology(models.Model):
    """Technologies utilisées dans les projets"""
    name = models.CharField(max_length=100, verbose_name="Nom")
    icon = models.CharField(max_length=50, verbose_name="Icône Font Awesome",
                           blank=True, help_text="Ex: fa-brands fa-react")
    color = models.CharField(max_length=7, default="#667eea", verbose_name="Couleur",
                            help_text="Code couleur hexadécimal")

    class Meta:
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Projets du portfolio"""
    PROJECT_TYPES = [
        ('application', 'Application Mobile'),
        ('web', 'Site Web'),
        ('cloud', 'Solution Cloud'),
        ('game', 'Jeu'),
    ]

    # Informations de base
    title = models.CharField(max_length=200, verbose_name="Titre")
    subtitle = models.CharField(max_length=200, verbose_name="Sous-titre")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL slug")
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES,
                                   default='application', verbose_name="Type de projet")

    # Description
    short_description = models.TextField(verbose_name="Description courte",
                                        help_text="Pour la liste des projets")
    full_description = models.TextField(verbose_name="Description complète")

    # Images et médias
    cover_image = models.ImageField(upload_to='projects/covers/',
                                   verbose_name="Image de couverture",
                                   help_text="Pour la liste des projets")
    header_image = models.ImageField(upload_to='projects/headers/',
                                     verbose_name="Image d'en-tête",
                                     blank=True, null=True)
    video_demo = models.FileField(upload_to='projects/videos/', blank=True, null=True,
                                 verbose_name="Vidéo de démonstration")

    # Technologies
    technologies = models.ManyToManyField(Technology, verbose_name="Technologies utilisées")

    # Caractéristiques
    features = models.JSONField(default=list, verbose_name="Caractéristiques",
                               help_text="Liste des fonctionnalités principales")

    # Métadonnées
    is_featured = models.BooleanField(default=False, verbose_name="Projet mis en avant")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Screenshot(models.Model):
    """Captures d'écran des projets"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                               related_name='screenshots', verbose_name="Projet")
    image = models.ImageField(upload_to='projects/screenshots/', verbose_name="Image")
    caption = models.CharField(max_length=200, blank=True, verbose_name="Légende")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Capture d'écran"
        verbose_name_plural = "Captures d'écran"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Screenshot {self.order}"


class Formation(models.Model):
    """Formations proposées"""
    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    duration = models.CharField(max_length=50, verbose_name="Durée",
                               help_text="Ex: 3 mois, 40 heures")
    icon = models.CharField(max_length=50, verbose_name="Icône Font Awesome",
                           help_text="Ex: fa-solid fa-code")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    """Informations de contact (singleton)"""
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    location = models.CharField(max_length=200, verbose_name="Localisation")

    # Réseaux sociaux
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn")
    github_url = models.URLField(blank=True, verbose_name="GitHub")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter")

    # Analytics
    google_analytics_id = models.CharField(max_length=20, blank=True,
                                          verbose_name="Google Analytics ID")
    google_tag_manager_id = models.CharField(max_length=20, blank=True,
                                            verbose_name="Google Tag Manager ID")

    class Meta:
        verbose_name = "Informations de contact"
        verbose_name_plural = "Informations de contact"

    def __str__(self):
        return "Informations de contact"

    def save(self, *args, **kwargs):
        # Assurer qu'il n'y a qu'une seule instance
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
