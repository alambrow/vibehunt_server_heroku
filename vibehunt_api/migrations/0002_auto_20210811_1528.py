# Generated by Django 3.2.6 on 2021-08-11 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vibehunt_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='venueId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vibehunt_api.venue'),
            preserve_default=False,
        ),
    ]
