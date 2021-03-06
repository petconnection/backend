# Generated by Django 2.0.7 on 2018-07-31 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('size', models.CharField(choices=[('S', 'small'), ('M', 'medium'), ('B', 'big')], default='M', max_length=2)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2)),
                ('registration', models.DateTimeField(auto_now_add=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=120)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Animal')),
                ('vaccines', models.TextField(blank=True, max_length=256, null=True)),
                ('castrated', models.NullBooleanField(default=False)),
                ('chip', models.NullBooleanField(default=False)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='breed',
            name='species_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Species'),
        ),
        migrations.AddField(
            model_name='animal',
            name='breed_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Breed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Entity'),
        ),
    ]
