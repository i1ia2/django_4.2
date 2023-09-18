# Generated by Django 4.1.7 on 2023-09-11 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tegs', to='articles.tag', verbose_name='разделы'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.TextField(max_length=90),
        ),
    ]