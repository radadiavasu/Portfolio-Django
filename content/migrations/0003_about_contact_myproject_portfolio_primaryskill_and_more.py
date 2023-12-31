# Generated by Django 4.1.4 on 2022-12-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_profile_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_about', models.TextField()),
                ('short_about', models.TextField()),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150)),
                ('heading', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'MyProject',
                'verbose_name_plural': 'MyProjects',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
        migrations.CreateModel(
            name='PrimarySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='Primaryskill/')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'PrimarySkill',
                'verbose_name_plural': 'PrimarySkills',
            },
        ),
        migrations.CreateModel(
            name='SecondarySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='Secondaryskill/')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'SecondarySkill',
                'verbose_name_plural': 'SecondarySkills',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Testomonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='testomonial/client')),
                ('image_name', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('quote', models.TextField()),
            ],
            options={
                'verbose_name': 'Testomonial',
                'verbose_name_plural': 'Testomonials',
            },
        ),
    ]
