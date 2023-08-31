# Generated by Django 4.1.3 on 2023-08-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0023_alter_enfant_aquafun_reservations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='categorie',
            field=models.CharField(blank=True, choices=[('hc', 'HC'), ('tam', 'TAM'), ('oe', 'OE'), ('gm', 'GM'), ('gc', 'GC'), ('pm', 'PM'), ('pc', 'PC')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='conjointe',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], default='F', max_length=2),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], default='F', max_length=2),
        ),
    ]
