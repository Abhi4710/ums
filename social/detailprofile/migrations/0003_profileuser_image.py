# Generated by Django 2.1.3 on 2018-12-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailprofile', '0002_remove_profileuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
