# Generated by Django 4.1.4 on 2023-01-06 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_deploytemplate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploytemplate',
            name='docker_env_vars',
            field=models.TextField(default='{}', max_length=500, verbose_name='Docker Environment Variables'),
        ),
    ]
