# Generated by Django 2.1.5 on 2019-11-10 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0017_auto_20191110_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('upload', models.ImageField(upload_to='')),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='cardID',
        ),
        migrations.DeleteModel(
            name='image',
        ),
    ]
