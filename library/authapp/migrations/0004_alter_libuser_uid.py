# Generated by Django 4.0.2 on 2022-02-25 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_alter_libuser_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6d9bf283-1f8e-42f0-ab27-8ee83cd44a8b'), primary_key=True, serialize=False),
        ),
    ]