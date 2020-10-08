# Generated by Django 2.2.3 on 2020-09-27 16:02

import ckeditor_uploader.fields
import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, validators=[core.validators.validate_only_letters, django.core.validators.MinLengthValidator(7)], verbose_name='Nombre')),
                ('lema', models.CharField(max_length=50, validators=[core.validators.validate_only_letters, django.core.validators.MinLengthValidator(7)], verbose_name='Lema')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='business', verbose_name='Logo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('direccion', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(7)], verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=12, validators=[core.validators.validate_only_numbers, django.core.validators.MinLengthValidator(5)], verbose_name='Telefono')),
                ('horarios', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Horarios')),
                ('mision', models.TextField(verbose_name='Misión')),
                ('vision', models.TextField(verbose_name='Vision')),
                ('historia', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Historia')),
                ('creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('edicion', models.DateField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
