# Generated by Django 4.2.7 on 2023-12-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0003_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postview',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]