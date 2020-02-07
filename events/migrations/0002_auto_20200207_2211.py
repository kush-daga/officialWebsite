# Generated by Django 2.2.5 on 2020-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='topics', to='events.Topic'),
        ),
    ]
