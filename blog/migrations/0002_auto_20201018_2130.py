# Generated by Django 3.1.2 on 2020-10-18 20:30

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletext',
            name='text',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='article_category',
            field=models.CharField(max_length=50),
        ),
    ]
