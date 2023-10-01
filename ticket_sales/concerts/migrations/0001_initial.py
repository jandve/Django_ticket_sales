# Generated by Django 4.2.5 on 2023-10-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=80)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=50)),
                ('session', models.CharField(choices=[('user', 'user'), ('po', 'place_owner'), ('bo', 'band_owner')], default='user', max_length=10)),
            ],
        ),
    ]