# Generated by Django 5.0.4 on 2024-04-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0006_student_courses_of_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='speciality',
            field=models.CharField(max_length=50, null=True, verbose_name='speciality'),
        ),
    ]
