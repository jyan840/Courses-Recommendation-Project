# Generated by Django 4.2.9 on 2024-03-12 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0006_savedcourses_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcourses',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]