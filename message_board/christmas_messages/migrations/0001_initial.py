# Generated by Django 4.2.7 on 2023-12-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChristmasMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('gift_list', models.TextField()),
                ('kindness_level', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('has_cavities', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
