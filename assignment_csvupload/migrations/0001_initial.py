# Generated by Django 3.1 on 2020-08-15 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventsForm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
    ]
