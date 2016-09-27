# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companero',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'Companero',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('aprobado', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Universidad',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Usuario',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='companero',
            name='id_universidad',
            field=models.ForeignKey(to='prueba.Universidad'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companero',
            name='id_usuario_dos',
            field=models.ForeignKey(related_name='companero', to='prueba.Usuario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='companero',
            name='id_usuario_uno',
            field=models.ForeignKey(related_name='usuario', to='prueba.Usuario'),
            preserve_default=True,
        ),
    ]
