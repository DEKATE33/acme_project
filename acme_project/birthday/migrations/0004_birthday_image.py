# Generated by Django 3.2.16 on 2023-10-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0003_birthday_unique person constraint'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото'),
        ),
    ]
