# Generated by Django 4.0.1 on 2022-04-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_articles_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='email',
            field=models.TextField(default='null'),
        ),
    ]