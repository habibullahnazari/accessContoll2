# Generated by Django 5.0.2 on 2024-02-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserReg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeru',
            name='allowed',
            field=models.BooleanField(default=False),
        ),
    ]
