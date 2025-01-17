# Generated by Django 4.2.16 on 2024-11-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_coba', '0002_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('topic', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('num_pages', models.IntegerField()),
            ],
        ),
    ]
