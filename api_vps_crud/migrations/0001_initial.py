# Generated by Django 3.2.16 on 2022-11-13 14:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vps',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpu', models.SmallIntegerField()),
                ('hdd', models.SmallIntegerField()),
                ('ram', models.SmallIntegerField()),
                ('status', models.CharField(choices=[('SR', 'started'), ('BL', 'blocked'), ('SP', 'stopped')], default='SR', max_length=2)),
            ],
        ),
    ]
