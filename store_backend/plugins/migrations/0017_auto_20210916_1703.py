# Generated by Django 2.2.24 on 2021-09-16 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plugins', '0016_auto_20210126_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pluginmeta',
            old_name='fan',
            new_name='fans',
        ),
        migrations.RemoveField(
            model_name='pluginmeta',
            name='owner',
        ),
        migrations.CreateModel(
            name='PluginMetaCollaborator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('O', 'Owner'), ('M', 'Maintainer')], default='O', max_length=1)),
                ('meta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plugins.PluginMeta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('meta', 'user')},
            },
        ),
        migrations.AddField(
            model_name='pluginmeta',
            name='collaborators',
            field=models.ManyToManyField(related_name='collab_plugin_metas', through='plugins.PluginMetaCollaborator', to=settings.AUTH_USER_MODEL),
        ),
    ]