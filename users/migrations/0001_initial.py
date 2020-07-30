# Generated by Django 3.0.7 on 2020-07-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user_genders',
            },
        ),
        migrations.CreateModel(
            name='SkinTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user_skintypes',
            },
        ),
        migrations.CreateModel(
            name='SkinWorries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user_skinworries',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('userid', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phonenumber', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('login_method', models.CharField(choices=[('userid', 'userid'), ('kakao', 'Kakao')], default='userid', max_length=50)),
                ('genderid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Genders')),
                ('skintype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SkinTypes')),
                ('skinworry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.SkinWorries')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]