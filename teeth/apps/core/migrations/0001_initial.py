# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aimag_hot', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('sum_duureg', models.CharField(max_length=30, null=True)),
                ('bag_horoo', models.CharField(max_length=30, null=True)),
                ('horoolol_gudamj', models.CharField(max_length=30, null=True)),
                ('bair_hashaa', models.CharField(max_length=30, null=True)),
                ('toot', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('allowed_amount', models.IntegerField(default=0)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=30, null=True)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('register_num', models.CharField(max_length=30, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('phone_number', models.CharField(max_length=30, null=True)),
                ('emd_number', models.CharField(max_length=30, null=True)),
                ('emd_type', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('ndd_number', models.CharField(max_length=30, null=True)),
                ('erkhiin_bichig', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Details',
            },
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsusni_buleg', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('em_buleg', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('heregledeg_jsa', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('tolov', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('arhag_ovchin1', models.CharField(max_length=30, null=True)),
                ('arhag_ovchin2', models.CharField(max_length=30, null=True)),
                ('arhag_ovchin3', models.CharField(max_length=30, null=True)),
                ('arhi_uudag', models.BooleanField(default=False)),
                ('tamhi_tatdag', models.BooleanField(default=False)),
                ('orhiin_emch', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('gerleltiin_baidal', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolovsrol', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('ajil', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('alban_tushaal', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('mergejil', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
                ('baiguullaga', models.CharField(max_length=30, null=True)),
                ('erheldeg_ajil', models.CharField(max_length=30, null=True)),
                ('hariyalal', models.IntegerField(choices=[(1, 'Эрэгтэй'), (2, 'Эмэгтэй')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30)),
                ('is_activeFirst', models.BooleanField(default=False)),
                ('is_activeSecond', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
                ('details', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Details')),
                ('medical', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Medical')),
                ('occupation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Occupation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='profiles',
            field=models.ManyToManyField(blank=True, related_name='profiles', to='core.Profile'),
        ),
    ]
