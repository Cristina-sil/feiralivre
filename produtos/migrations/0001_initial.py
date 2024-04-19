# Generated by Django 4.2.3 on 2024-04-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmeFrt', models.CharField(max_length=100)),
                ('prcFrt', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qntdDspnvl', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Verduras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmVdx', models.CharField(max_length=100)),
                ('pXcVdX', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stkVxL', models.IntegerField()),
            ],
        ),
    ]
