# Generated by Django 4.0.4 on 2022-05-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_registration',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
