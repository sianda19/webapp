# Generated by Django 4.0.1 on 2022-04-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_articles_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='email',
            field=models.TextField(default='null'),
        ),
    ]