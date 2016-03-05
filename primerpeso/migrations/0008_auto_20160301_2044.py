# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 20:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerpeso', '0007_auto_20160301_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunitysearch',
            name='location',
        ),
        migrations.AddField(
            model_name='opportunitysearch',
            name='locations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('anywhere_in_pr', 'Cualquier municipio'), ('adjuntas', 'Adjuntas'), ('aguada', 'Aguada'), ('aguadilla', 'Aguadilla'), ('aguas_buenas', 'Aguas Buenas'), ('aibonito', 'Aibonito'), ('anasco', 'Añasco'), ('arecibo', 'Arecibo'), ('arroyo', 'Arroyo'), ('barceloneta', 'Barceloneta'), ('barranquitas', 'Barranquitas'), ('bayamon', 'Bayamón'), ('cabo_rojo', 'Cabo Rojo'), ('caguas', 'Caguas'), ('camuy', 'Camuy'), ('canovanas', 'Canóvanas'), ('carolina', 'Carolina'), ('catano', 'Cataño'), ('cayey', 'Cayey'), ('ceiba', 'Ceiba'), ('ciales', 'Ciales'), ('cidra', 'Cidra'), ('coamo', 'Coamo'), ('comerio', 'Comerio'), ('corozal', 'Corozal'), ('culebra', 'Culebra'), ('dorado', 'Dorado'), ('fajardo', 'Fajardo'), ('florida', 'Florida'), ('guanica', 'Guánica'), ('guayama', 'Guayama'), ('guayanilla', 'Guayanilla'), ('guaynabo', 'Guaynabo'), ('gurabo', 'Gurabo'), ('hatillo', 'Hatillo'), ('hormigueros', 'Hormigueros'), ('humacao', 'Humacao'), ('isabela', 'Isabela'), ('jayuya', 'Jayuya'), ('juana_diaz', 'Juana Diaz'), ('juncos', 'Juncos'), ('lajas', 'Lajas'), ('lares', 'Lares'), ('las_marias', 'Las Marías'), ('las_piedras', 'Las Piedras'), ('loiza', 'Loíza'), ('luquillo', 'Luquillo'), ('manati', 'Manatí'), ('maricao', 'Maricao'), ('maunabo', 'Maunabo'), ('mayaguez', 'Mayagüez'), ('moca', 'Moca'), ('morovis', 'Morovis'), ('naguabo', 'Naguabo'), ('naranjito', 'Naranjito'), ('orocovis', 'Orocovis'), ('patillas', 'Patillas'), ('penuelas', 'Penuelas'), ('ponce', 'Ponce'), ('quebradillas', 'Quebradillas'), ('rincon', 'Rincón'), ('rio_grande', 'Río Grande'), ('sabana_grande', 'Sabana Grande'), ('salinas', 'Salinas'), ('san_german', 'San German'), ('san_juan', 'San Juan'), ('san_lorenzo', 'San Lorenzo'), ('san_sebastian', 'San Sebastian'), ('santa_isabel', 'Santa Isabel'), ('toa_alta', 'Toa Alta'), ('toa_baja', 'Toa Baja'), ('trujillo_alto', 'Trujillo Alto'), ('utuado', 'Utuado'), ('vega_alta', 'Vega Alta'), ('vega_baja', 'Vega Baja'), ('vieques', 'Vieques'), ('villalba', 'Villalba'), ('yabucoa', 'Yabucoa'), ('yauco', 'Yauco')], max_length=255), default=list, size=None, verbose_name='Where is your business located?'),
        ),
    ]
