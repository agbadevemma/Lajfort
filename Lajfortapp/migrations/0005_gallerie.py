# Generated by Django 5.0.6 on 2024-09-30 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lajfortapp', '0004_about_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', null=True, upload_to='')),
            ],
        ),
    ]
