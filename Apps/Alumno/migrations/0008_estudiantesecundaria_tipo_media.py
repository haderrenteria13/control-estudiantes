# Generated by Django 5.1.3 on 2024-12-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0007_alter_estudianteprimaria__grado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantesecundaria',
            name='tipo_media',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]