# Generated by Django 4.1 on 2022-09-19 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('top_name', models.CharField(max_length=264, unique=True)),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webpages', to='first_app.topic')),
            ],
            options={
                'verbose_name': 'webpage',
                'verbose_name_plural': 'webpages',
            },
        ),
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.webpage')),
            ],
        ),
    ]