# Generated by Django 4.1 on 2022-09-04 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_set_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.set'),
        ),
    ]