# Generated by Django 4.2.7 on 2023-12-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0002_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
