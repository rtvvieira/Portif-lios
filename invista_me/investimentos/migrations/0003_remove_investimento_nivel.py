# Generated by Django 5.1.7 on 2025-03-14 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investimentos', '0002_investimento_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimento',
            name='nivel',
        ),
    ]
