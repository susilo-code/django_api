# Generated by Django 4.2.16 on 2024-11-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('deptid', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
