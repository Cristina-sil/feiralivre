# Generated by Django 4.2.3 on 2024-04-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtPgto', models.CharField(max_length=50)),
                ('vlrTotal', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
