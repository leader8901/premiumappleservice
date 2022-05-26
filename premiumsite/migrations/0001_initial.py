# Generated by Django 4.0.2 on 2022-05-19 15:16

from django.db import migrations, models
import django.db.models.deletion
import premiumsite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_colors', models.CharField(help_text='Введите цвет на англ.', max_length=200, verbose_name='Название цвета')),
            ],
            options={
                'verbose_name': 'Цвета',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='iPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iphone_name', models.CharField(db_index=True, max_length=150, verbose_name='Название моделей iPhone')),
            ],
            options={
                'verbose_name': 'iPhone',
                'verbose_name_plural': 'iPhone',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MacBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macbook_name', models.CharField(db_index=True, max_length=150, verbose_name='Название моделей MacBook')),
            ],
            options={
                'verbose_name': 'MacBook',
                'verbose_name_plural': 'MacBook',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_info', models.CharField(help_text='Введите память в формате ...гб', max_length=100)),
            ],
            options={
                'verbose_name': 'Объем памяти',
                'verbose_name_plural': 'Объем памяти',
            },
        ),
        migrations.CreateModel(
            name='Model_iMac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imac_name', models.CharField(db_index=True, max_length=150)),
            ],
            options={
                'verbose_name': 'iMac',
                'verbose_name_plural': 'iMac',
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_os', models.CharField(help_text='Введите название Mac OS', max_length=200)),
            ],
            options={
                'verbose_name': 'Операционная система',
                'verbose_name_plural': 'Операционная система',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=100, null=True, verbose_name='Название Региона')),
            ],
            options={
                'verbose_name': 'Регионы',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_phone', models.IntegerField(verbose_name='Стоимость')),
                ('photo_phone', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото файлы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('availability_phone', models.BooleanField(default=True, verbose_name='В наличии')),
                ('new_or_used', models.BooleanField(default=True, verbose_name='Новый')),
                ('colors_phone', models.ForeignKey(help_text='Выберите цвет', on_delete=django.db.models.deletion.PROTECT, to='premiumsite.allcolors', verbose_name='Цвет')),
                ('memory_phone', models.ForeignKey(help_text='Выберите память', on_delete=django.db.models.deletion.PROTECT, to='premiumsite.memory', verbose_name='Память')),
                ('model_phone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='premiumsite.iphone', verbose_name='Название')),
                ('region_phone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='premiumsite.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Новые iPhone',
                'verbose_name_plural': 'Новые iPhone',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='iMac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_imac', models.CharField(max_length=100)),
                ('region_imac', models.CharField(max_length=150, null=True, verbose_name=premiumsite.models.Region)),
                ('model_id', models.CharField(max_length=155)),
                ('articles', models.CharField(max_length=155)),
                ('operating_system', models.CharField(max_length=250)),
                ('photo_phone', models.ImageField(blank=True, upload_to='photos_imac/%Y/%m/%d')),
                ('diagonal', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('chip', models.CharField(max_length=100)),
                ('new_or_used', models.BooleanField(default=True, verbose_name='Новый')),
                ('colors_imac', models.ForeignKey(help_text='Выберите цвет', on_delete=django.db.models.deletion.PROTECT, to='premiumsite.allcolors')),
                ('imac_serial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='premiumsite.model_imac')),
                ('memory_imac', models.ForeignKey(help_text='Выберите память', on_delete=django.db.models.deletion.PROTECT, to='premiumsite.memory')),
            ],
            options={
                'verbose_name': 'iMac',
                'verbose_name_plural': 'iMac',
            },
        ),
    ]
