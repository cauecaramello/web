# Generated by Django 5.1.4 on 2024-12-05 04:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_curso_foto_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='quantidade_estoque',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracao',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_compra', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
