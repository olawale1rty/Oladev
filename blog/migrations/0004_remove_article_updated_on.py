# Generated by Django 3.1.2 on 2020-10-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_updated_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_on',
        ),
    ]