# Generated by Django 5.2 on 2025-05-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_student_file_remove_student_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=500)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
    ]
