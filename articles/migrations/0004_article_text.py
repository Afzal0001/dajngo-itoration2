# Generated by Django 4.1.3 on 2022-12-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
