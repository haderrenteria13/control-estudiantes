# Generated by Django 5.1.3 on 2024-12-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0008_estudiantesecundaria_tipo_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantesecundaria',
            name='tipo_media',
        ),
        migrations.AddField(
            model_name='estudiantesecundaria',
            name='tipo_de_media',
            field=models.CharField(blank=True, help_text='Nombre de la media en la cual está estudiando, si aplica.', max_length=10),
        ),
    ]