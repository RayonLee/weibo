# Generated by Django 4.1.7 on 2023-03-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_total_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='if_collect_flag',
            field=models.BooleanField(default=False),
        ),
    ]