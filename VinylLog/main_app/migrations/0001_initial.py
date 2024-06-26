# Generated by Django 4.1.7 on 2023-03-02 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('length', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('country_of_origin', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('length', models.PositiveIntegerField(default=0)),
                ('models', models.TextField(max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.album')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country_of_origin', models.TextField(max_length=20)),
                ('pressing_year', models.TextField(max_length=4)),
                ('cover_rating', models.CharField(choices=[('MINT', 'M'), ('NEAR MINT', 'NM'), ('VERY GOOD PLUS', 'VG+'), ('VERY GOOD', 'VG'), ('GOOD', 'G'), ('POOR', 'P')], max_length=20)),
                ('disc_rating', models.CharField(choices=[('MINT', 'M'), ('NEAR MINT', 'NM'), ('VERY GOOD PLUS', 'VG+'), ('VERY GOOD', 'VG'), ('GOOD', 'G'), ('POOR', 'P')], max_length=20)),
                ('obs', models.TextField(max_length=255)),
                ('collection', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.collection')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.artist'),
        ),
    ]
