# Generated by Django 4.0.2 on 2022-02-25 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_libuser_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('7ff4932e-0125-4b78-8c26-432391507837'), primary_key=True, serialize=False),
        ),
    ]
