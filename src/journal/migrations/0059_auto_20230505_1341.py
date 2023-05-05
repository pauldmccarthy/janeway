# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-05 12:41
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations

OLD_VALUE = """
Dear {{ article.correspondence_author.full_name }},
<br/><br/>
We are requesting that you make some changes to your paper. Details of the changes required are below:
<br/><br/>
{{ revision.editor_note }}
<br/><br/>
You can access your revision here: {{ do_revisions_url }}
<br/><br/>
Your revisionsare due on {{ revision.date_due }}.
<br/><br/>
Regards,
<br/>
{{ request.user.signature|safe }}
""".strip().replace('\n', '')

NEW_VALUE = """
Dear {{ article.correspondence_author.full_name }},
<br/><br/>
We are requesting that you make some changes to your paper. Details of the changes required are below:
<br/><br/>
{{ revision.editor_note }}
<br/><br/>
You can access your revision here: {{ do_revisions_url }}
<br/><br/>
{% if revision.date_due %}Your revisions are due on {{ revision.date_due }}.
<br><br>
{% endif %}
Regards,
<br/>
{{ request.user.signature|safe }}
""".strip().replace('\n', '')


def apply(apps, schema_editor, value):
    Setting = apps.get_model("core", "Setting")
    SettingValue = apps.get_model("core", "SettingValue")
    Journal = apps.get_model("journal", "Journal")
    call_command('load_default_settings')

    setting = Setting.objects.get(name='request_revisions')

    for journal in [None] + list(Journal.objects.all()):
        setting_value = SettingValue.objects.filter(
            journal=journal,
            setting=setting,
        ).first()
        if setting_value is not None:
            setting_value.value = value
            if setting_value.value_en is not None:
                setting_value.value_en = value
            if setting_value.value_en_us is not None:
                setting_value.value_en_us = value
            setting_value.save()

def forwards_func(apps, schema_editor):
    apply(apps, schema_editor, NEW_VALUE)

def reverse_func(apps, schema_editor):
    apply(apps, schema_editor, OLD_VALUE)


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0058_auto_20230505_1137'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_code=reverse_func),
    ]
