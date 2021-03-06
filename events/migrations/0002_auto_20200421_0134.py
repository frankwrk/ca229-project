# Generated by Django 3.0.5 on 2020-04-21 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.DateField(default=django.utils.timezone.now, help_text='Date of the event', verbose_name='Date of the event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, help_text='Event Notes', null=True, verbose_name='Event Notes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, help_text='Event Description', null=True, verbose_name='Event Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='End time', verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(help_text='Starting time', verbose_name='Starting time'),
        ),
    ]
