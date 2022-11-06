# Generated by Django 4.1.3 on 2022-11-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0006_blockb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_rooms', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='BlockB',
            new_name='Block',
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('room_type', models.CharField(max_length=200)),
                ('room_no', models.IntegerField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildings.floor')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('item_name', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_value', models.IntegerField()),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildings.rooms')),
            ],
        ),
        migrations.AddField(
            model_name='floor',
            name='block',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildings.block'),
        ),
    ]
