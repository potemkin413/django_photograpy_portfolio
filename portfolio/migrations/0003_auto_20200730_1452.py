# Generated by Django 3.0.8 on 2020-07-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Фотография в портфолио'),
        ),
    ]