# Generated by Django 4.1.3 on 2023-08-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0012_alter_agent_accord_alter_agent_datenaissance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conjointe',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]
