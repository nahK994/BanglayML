# Generated by Django 2.1.5 on 2019-12-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0027_auto_20191121_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardsinfo',
            name='card_title',
            field=models.CharField(max_length=70),
        ),
    ]
