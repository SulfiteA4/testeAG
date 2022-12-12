# Generated by Django 4.1.4 on 2022-12-12 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_controle_motorista_alter_controle_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='motorista',
            field=models.ForeignKey(db_column='Motorista_id', on_delete=django.db.models.deletion.CASCADE, to='core.motorista'),
        ),
        migrations.AlterField(
            model_name='controle',
            name='veiculo',
            field=models.ForeignKey(db_column='Veiculo_id', on_delete=django.db.models.deletion.CASCADE, to='core.veiculo'),
        ),
    ]
