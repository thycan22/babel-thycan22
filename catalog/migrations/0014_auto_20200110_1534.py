# Generated by Django 3.0.2 on 2020-01-10 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20200110_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Author', verbose_name='Auteur'),
        ),
    ]
