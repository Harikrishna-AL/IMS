# Generated by Django 4.1.3 on 2022-11-05 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0007_floor_rename_blockb_block_rooms_item_floor_block'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rooms',
            new_name='room',
        ),
    ]
