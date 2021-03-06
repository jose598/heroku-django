# Generated by Django 3.0.5 on 2020-08-21 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='No disponible', max_length=50)),
                ('descripcion', models.CharField(blank=True, default='No disponible', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, choices=[('FIEC', 'Facultad de Ingenieria en Electricidad y Computacion'), ('FCNM', 'Facultad de Ciencias Naturales y Matematicas'), ('EDCOM', 'Escuela de Diseno y Comunicacion '), ('FICT', 'Facultad de Ingenieria en Ciencias de la Tierra'), ('FIMCP', 'Facultad de Ingenieria en Mecanica y Ciencias de la Produccion')], default='Sin Especificar', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='No disponible', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='Sin Especificar', max_length=50)),
                ('apellido', models.CharField(blank=True, default='Sin Especificar', max_length=50)),
                ('email', models.EmailField(blank=True, default='Sin Especificar', max_length=100)),
                ('telefono', models.CharField(blank=True, default='0999999999', max_length=13)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('lugar_origen', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Persona')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='fecha_registro')),
                ('fecha_log', models.DateTimeField(auto_now_add=True, verbose_name='ultimo_ingreso')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_editor', models.BooleanField(default=False)),
                ('is_supervisor', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Persona')),
                ('rol', models.CharField(blank=True, choices=[('LECTOR', 'Lector'), ('ESCRITOR', 'Escritor'), ('PROPIETARIO', 'Propietario ')], default='Sin Especificar', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(blank=True, default='Invalido', max_length=250)),
                ('persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, default='Sin Especificar', max_length=50)),
                ('descripcion', models.CharField(blank=True, default='Sin Especificar', max_length=300)),
                ('administrador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Persona')),
                ('descripcion', models.CharField(blank=True, default='Sin Especificar', max_length=150)),
                ('foto', models.CharField(blank=True, default='Sin Especificar', max_length=150)),
                ('facultad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Facultad')),
                ('habilidad', models.ManyToManyField(to='api.Habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='No disponible', max_length=50)),
                ('descripcion', models.CharField(blank=True, default='Dato no ingresado', max_length=300)),
                ('banner', models.CharField(blank=True, default='No posee banner', max_length=300)),
                ('estado', models.BooleanField(default=1)),
                ('fecha_inicio', models.DateField(auto_now_add=True, null=True)),
                ('fecha_termino', models.DateField(null=True)),
                ('vacantes', models.IntegerField(default=0)),
                ('cant_interesados', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Categoria')),
                ('habilidad', models.ManyToManyField(to='api.Habilidad')),
                ('interesados', models.ManyToManyField(blank=True, to='api.Consumidor')),
            ],
        ),
    ]
