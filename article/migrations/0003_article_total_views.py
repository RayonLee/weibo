# Generated by Django 4.1.7 on 2023-03-04 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
