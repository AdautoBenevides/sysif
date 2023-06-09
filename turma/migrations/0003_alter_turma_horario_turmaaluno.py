# Generated by Django 4.1.3 on 2022-12-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_alter_aluno_id_curso'),
        ('turma', '0002_alter_turma_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.TimeField(verbose_name='Horario'),
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aluno.aluno')),
                ('id_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
    ]
