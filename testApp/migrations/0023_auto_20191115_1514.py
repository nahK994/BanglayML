# Generated by Django 2.1.5 on 2019-11-15 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testApp', '0022_auto_20191115_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='card_table',
            fields=[
                ('cardID', models.AutoField(primary_key=True, serialize=False)),
                ('serialNO', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('paragraph', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='categoryTable',
            fields=[
                ('categoryID', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='code_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('serialNO', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
        migrations.CreateModel(
            name='image_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('serialNO', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('upload', models.ImageField(upload_to='')),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
        migrations.CreateModel(
            name='recommendation_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('serialNO', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=300)),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
        migrations.AddField(
            model_name='card_table',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.categoryTable'),
        ),
    ]