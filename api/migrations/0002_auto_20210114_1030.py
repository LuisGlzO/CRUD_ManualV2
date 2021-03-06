# Generated by Django 3.1.1 on 2021-01-14 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('edificio', models.CharField(max_length=30)),
                ('capacidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='salon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.salones'),
            preserve_default=False,
        ),
    ]
