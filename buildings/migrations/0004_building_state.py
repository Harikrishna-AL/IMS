# Generated by Django 3.1.13 on 2022-11-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_remove_building_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='state',
            field=models.CharField(default='state', max_length=200),
        ),
    ]
