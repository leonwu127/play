# Generated by Django 2.0.10 on 2019-02-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("tournament", "0006_remove_tournament_single_snake_per_team")]

    operations = [
        migrations.AddField(
            model_name="tournament",
            name="engine_url",
            field=models.CharField(
                default="https://engine.battlesnake.io/", max_length=128
            ),
        )
    ]
