# Generated by Django 4.2.2 on 2023-07-17 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_card_card_set_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='card_set_id',
            new_name='card_set',
        ),
    ]
