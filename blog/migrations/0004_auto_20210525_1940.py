# Generated by Django 3.2.3 on 2021-05-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cook_time',
            new_name='production_time',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='blog.post'),
        ),
    ]
