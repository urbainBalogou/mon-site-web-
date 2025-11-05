from django.core.management.base import BaseCommand
from django.core.files import File
from portfolio.models import Skill, Technology, Project, Screenshot, Formation, ContactInfo
import os
from pathlib import Path


class Command(BaseCommand):
    help = 'Populate database with initial portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting data population...')

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Screenshot.objects.all().delete()
        Project.objects.all().delete()
        Technology.objects.all().delete()
        Skill.objects.all().delete()
        Formation.objects.all().delete()

        # Create Contact Info
        self.stdout.write('Creating contact info...')
        contact = ContactInfo.objects.create(
            email='urbainbalogou19@gmail.com',
            phone='+228 70 43 60 43',
            whatsapp='+228 70 43 60 43',
            location='Lomé, Togo',
            google_analytics_id='G-DGYQ8V3DTJ',
            google_tag_manager_id='GTM-W7DWHD3J'
        )
        self.stdout.write(self.style.SUCCESS('✓ Contact info created'))

        # Create Skills
        self.stdout.write('Creating skills...')
        skills_data = [
            ('Python', 'fa-brands fa-python', 1),
            ('Django', 'fa-solid fa-code', 2),
            ('JavaScript', 'fa-brands fa-js', 3),
            ('React', 'fa-brands fa-react', 4),
            ('Flutter', 'fa-solid fa-mobile', 5),
            ('PostgreSQL', 'fa-solid fa-database', 6),
            ('Git', 'fa-brands fa-git-alt', 7),
            ('Docker', 'fa-brands fa-docker', 8),
        ]

        for name, icon, order in skills_data:
            Skill.objects.create(name=name, icon=icon, order=order)
        self.stdout.write(self.style.SUCCESS(f'✓ {len(skills_data)} skills created'))

        # Create Technologies
        self.stdout.write('Creating technologies...')
        tech_data = {
            'Django': ('fa-solid fa-code', '#092E20'),
            'Python': ('fa-brands fa-python', '#3776AB'),
            'Flutter': ('fa-solid fa-mobile', '#02569B'),
            'Dart': ('fa-solid fa-code', '#0175C2'),
            'Firebase': ('fa-solid fa-fire', '#FFCA28'),
            'React': ('fa-brands fa-react', '#61DAFB'),
            'JavaScript': ('fa-brands fa-js', '#F7DF1E'),
            'HTML/CSS': ('fa-brands fa-html5', '#E34F26'),
            'Bootstrap': ('fa-brands fa-bootstrap', '#7952B3'),
            'PostgreSQL': ('fa-solid fa-database', '#4169E1'),
            'SQLite': ('fa-solid fa-database', '#003B57'),
            'Git': ('fa-brands fa-git-alt', '#F05032'),
        }

        technologies = {}
        for name, (icon, color) in tech_data.items():
            tech = Technology.objects.create(name=name, icon=icon, color=color)
            technologies[name] = tech
        self.stdout.write(self.style.SUCCESS(f'✓ {len(tech_data)} technologies created'))

        # Create Projects
        self.stdout.write('Creating projects...')

        # Project 1: E-commerce
        p1 = Project.objects.create(
            title='Plateforme E-commerce',
            subtitle='Application mobile de commerce en ligne',
            slug='application-ecommerce',
            project_type='application',
            short_description='Une application mobile complète pour le commerce électronique avec gestion des produits, panier et paiement.',
            full_description='Plateforme e-commerce mobile moderne développée avec Flutter, offrant une expérience utilisateur fluide pour l\'achat en ligne. Intègre un système de panier, de paiement sécurisé et de suivi des commandes.',
            features=[
                'Catalogue de produits avec recherche et filtres',
                'Panier d\'achats et gestion des commandes',
                'Système de paiement sécurisé',
                'Profil utilisateur personnalisé',
                'Notifications push',
                'Suivi des livraisons'
            ],
            cover_image='projects/covers/ecommerce1.png',
            is_featured=True,
            order=1
        )
        p1.technologies.add(technologies['Flutter'], technologies['Dart'], technologies['Firebase'])

        # Project 2: Galaxy Game
        p2 = Project.objects.create(
            title='Galaxy Space Game',
            subtitle='Jeu spatial interactif',
            slug='application-galaxy',
            project_type='game',
            short_description='Un jeu spatial développé en Python où le joueur navigue dans l\'espace et affronte des ennemis.',
            full_description='Jeu d\'arcade spatial développé en Python, offrant une expérience de jeu immersive avec des graphismes dynamiques et des mécaniques de jeu engageantes.',
            features=[
                'Contrôles fluides et réactifs',
                'Système de score et de niveaux',
                'Effets visuels et animations',
                'Difficulté progressive',
                'Système de vies et de power-ups'
            ],
            cover_image='projects/covers/galaxy.jpg',
            is_featured=False,
            order=2
        )
        p2.technologies.add(technologies['Python'])

        # Project 3: Plant Analyzer
        p3 = Project.objects.create(
            title='Analyseur de Plantes',
            subtitle='Application d\'identification de maladies',
            slug='application-plant',
            project_type='application',
            short_description='Application mobile utilisant l\'IA pour identifier les maladies des plantes à partir de photos.',
            full_description='Application mobile intelligente permettant aux agriculteurs et jardiniers d\'identifier rapidement les maladies des plantes en prenant simplement une photo. Utilise l\'apprentissage automatique pour fournir des diagnostics précis et des recommandations de traitement.',
            features=[
                'Reconnaissance d\'images par IA',
                'Identification des maladies',
                'Recommandations de traitement',
                'Historique des analyses',
                'Base de données de plantes',
                'Mode hors ligne'
            ],
            cover_image='projects/covers/plant.webp',
            is_featured=True,
            order=3
        )
        p3.technologies.add(technologies['Flutter'], technologies['Dart'], technologies['Python'])

        # Project 4: Location de voitures
        p4 = Project.objects.create(
            title='Système de Location de Voitures',
            subtitle='Plateforme de réservation automobile',
            slug='application-location',
            project_type='application',
            short_description='Application complète pour la location de véhicules avec système de réservation et de gestion.',
            full_description='Plateforme digitale moderne pour la location de véhicules, permettant aux utilisateurs de parcourir le catalogue, réserver et gérer leurs locations en toute simplicité.',
            features=[
                'Catalogue de véhicules avec filtres',
                'Système de réservation en ligne',
                'Calcul automatique des tarifs',
                'Gestion des documents',
                'Historique des locations',
                'Notifications de rappel'
            ],
            cover_image='projects/covers/location.png',
            is_featured=False,
            order=4
        )
        p4.technologies.add(technologies['Flutter'], technologies['Firebase'], technologies['Dart'])

        # Project 5: Road Alert
        p5 = Project.objects.create(
            title='Road Alert',
            subtitle='Système d\'alertes routières',
            slug='application-road-alert',
            project_type='application',
            short_description='Application de signalement et d\'alertes en temps réel pour les incidents routiers.',
            full_description='Application mobile collaborative permettant aux conducteurs de signaler et de recevoir des alertes sur les incidents routiers, les embouteillages et les dangers en temps réel.',
            features=[
                'Signalement d\'incidents en temps réel',
                'Alertes géolocalisées',
                'Carte interactive',
                'Partage communautaire',
                'Notifications push',
                'Historique des trajets'
            ],
            cover_image='projects/covers/road_alert.jpg',
            is_featured=False,
            order=5
        )
        p5.technologies.add(technologies['Flutter'], technologies['Firebase'], technologies['Dart'])

        # Project 6: Barbershop
        p6 = Project.objects.create(
            title='Beauty Salon App',
            subtitle='Application de gestion de salon',
            slug='application-barbershop',
            project_type='application',
            short_description='Application de réservation et de gestion pour salons de beauté et barbiers.',
            full_description='Solution digitale complète pour les salons de beauté et barbiers, permettant la prise de rendez-vous en ligne, la gestion des clients et l\'organisation des services.',
            features=[
                'Réservation en ligne',
                'Gestion du calendrier',
                'Profils des stylistes',
                'Galerie de réalisations',
                'Notifications de rendez-vous',
                'Système de fidélité'
            ],
            cover_image='projects/covers/barbershop.png',
            is_featured=False,
            order=6
        )
        p6.technologies.add(technologies['Flutter'], technologies['Firebase'], technologies['Dart'])

        # Project 7: Restaurant Website
        p7 = Project.objects.create(
            title='Site Web Restaurant',
            subtitle='Site vitrine pour restaurant',
            slug='site-restaurant',
            project_type='web',
            short_description='Site web élégant pour restaurant avec menu en ligne et système de réservation.',
            full_description='Site web professionnel pour restaurant offrant une présentation élégante du menu, des informations sur l\'établissement et un système de réservation en ligne.',
            features=[
                'Menu interactif',
                'Galerie de photos',
                'Système de réservation',
                'Informations de contact',
                'Design responsive',
                'Intégration Google Maps'
            ],
            cover_image='projects/covers/restaurant.jpg',
            is_featured=False,
            order=7
        )
        p7.technologies.add(technologies['HTML/CSS'], technologies['JavaScript'], technologies['Bootstrap'])

        # Project 8: Cloud PME
        p8 = Project.objects.create(
            title='Cloud PME',
            subtitle='Solution cloud pour PME',
            slug='cloud-pme',
            project_type='cloud',
            short_description='Plateforme cloud complète pour la gestion d\'entreprise (CRM, facturation, gestion de projet).',
            full_description='Solution cloud tout-en-un pour les petites et moyennes entreprises, intégrant CRM, gestion de projets, facturation et collaboration d\'équipe.',
            features=[
                'CRM et gestion clients',
                'Gestion de projets',
                'Facturation automatisée',
                'Tableau de bord analytique',
                'Collaboration d\'équipe',
                'Stockage cloud sécurisé'
            ],
            cover_image='projects/covers/cloud_pme.png',
            is_featured=True,
            order=8
        )
        p8.technologies.add(technologies['Django'], technologies['Python'], technologies['PostgreSQL'], technologies['React'])

        self.stdout.write(self.style.SUCCESS('✓ 8 projects created'))

        # Create Formations
        self.stdout.write('Creating formations...')
        Formation.objects.create(
            title='Développement Web Full Stack',
            description='Formation complète en développement web avec Django, React et bases de données.',
            duration='3 mois',
            icon='fa-solid fa-code',
            is_active=True,
            order=1
        )
        Formation.objects.create(
            title='Développement Mobile avec Flutter',
            description='Apprenez à créer des applications mobiles cross-platform avec Flutter.',
            duration='2 mois',
            icon='fa-solid fa-mobile',
            is_active=True,
            order=2
        )
        Formation.objects.create(
            title='Python pour Data Science',
            description='Formation en analyse de données avec Python, Pandas et Machine Learning.',
            duration='2.5 mois',
            icon='fa-solid fa-chart-line',
            is_active=True,
            order=3
        )
        self.stdout.write(self.style.SUCCESS('✓ 3 formations created'))

        self.stdout.write(self.style.SUCCESS('\n✓ Data population completed successfully!'))
        self.stdout.write('\nNext steps:')
        self.stdout.write('1. Copy project images to media/projects/covers/')
        self.stdout.write('2. Create a superuser: python manage.py createsuperuser')
        self.stdout.write('3. Run the server: python manage.py runserver')
