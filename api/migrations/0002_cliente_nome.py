# Generated by Django 4.2.6 on 2023-10-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=10, max_length=255),
            preserve_default=False,
        ),
    ]
