# Generated by Django 2.0.4 on 2018-04-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
