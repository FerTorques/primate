# Generated by Django 3.2.4 on 2021-09-01 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20210831_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntasrespondidas',
            name='usuario',
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='quizUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='Quiz.quizusuario'),
            preserve_default=False,
        ),
    ]