# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('shelftype', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShelfContainsBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('bookid', models.ForeignKey(to='backend.Book')),
                ('shelfid', models.ForeignKey(to='backend.Shelf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('apt', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='shelfcontainsbooks',
            unique_together=set([('shelfid', 'bookid')]),
        ),
        migrations.AddField(
            model_name='shelf',
            name='userid',
            field=models.ForeignKey(to='backend.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='shelf',
            unique_together=set([('userid', 'shelftype')]),
        ),
    ]
