# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-04 14:39
from __future__ import unicode_literals

from django.db import migrations

OLD_VALUE = "Dear {{ article.correspondence_author.full_name }},<br><br>We are requesting that you make some changes to your paper. Details of the changes required are below:<br><br>{{ revision.editor_note }}<br><br>You can access your revision here: <a href=\"{% journal_url 'do_revisions' article.pk revision.pk  %}\">{% journal_url 'do_revisions' article.pk revision.pk  %}</a><br><br>Your revisions are due on {{ revision.date_due }}.<br><br>Regards, <br>{{ request.user.signature|safe }}"
NEW_VALUE = "Dear {{ article.correspondence_author.full_name }},<br><br>We are requesting that you make some changes to your paper. Details of the changes required are below:<br><br>{{ revision.editor_note }}<br><br>You can access you revision here: <a href=\"{% journal_url 'do_revisions' article.pk revision.pk  %}\">{% journal_url 'do_revisions' article.pk revision.pk  %}</a><br><br>{% if revision.date_due %}Your revisions are due on {{ revision.date_due }}.<br><br>{% endif %}Regards, <br>{{ request.user.signature|safe }}"


def replace_template(apps, schema_editor):
    SettingValueTranslation = apps.get_model('core', 'SettingValueTranslation')
    settings = SettingValueTranslation.objects.filter(hvad_value=OLD_VALUE)

    for setting in settings:
        setting.hvad_value = NEW_VALUE
        setting.save()


def reverse_code(apps, schema_editor):
    SettingValueTranslation = apps.get_model('core', 'SettingValueTranslation')
    settings = SettingValueTranslation.objects.filter(hvad_value=NEW_VALUE)
    for setting in settings:
        setting.hvad_value = OLD_VALUE
        setting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0079_auto_20230208_1233'),
    ]

    operations = [
        migrations.RunPython(replace_template, reverse_code=reverse_code),
    ]
