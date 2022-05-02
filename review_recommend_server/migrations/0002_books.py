# Generated by Django 4.0.4 on 2022-05-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_recommend_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
