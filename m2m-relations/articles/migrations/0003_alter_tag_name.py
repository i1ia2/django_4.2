# Generated by Django 4.1.7 on 2023-09-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=90),
        ),
    ]
