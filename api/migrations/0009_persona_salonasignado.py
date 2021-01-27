# Generated by Django 3.1.1 on 2021-01-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_persona_salonasignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='salonAsignado',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.salones'),
        ),
    ]
