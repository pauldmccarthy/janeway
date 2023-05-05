# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-05-05 10:19
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations

editor_revisions_complete_receipt = """
<p>Dear {{ editor.full_name }},</p>
<p>{{ revision.article.correspondence_author.full_name}} has completed revisions for the article \"{{ revision.article.title }}\".</p>
<p>The revisions made were as follows:</p>
<ul>
{% for action in actions %}<li>{{ action.logged }} - {{ action.text }}{% endfor %}
</ul>
<p>Please log into the paper handling website to handle this revision.</p>
""".strip().replace('\n', '')


class Migration(migrations.Migration):

    def forwards_func(apps, schema_editor):
        Setting = apps.get_model("core", "Setting")
        SettingValue = apps.get_model("core", "SettingValue")
        SettingGroup = apps.get_model("core", "SettingGroup")
        Journal = apps.get_model("journal", "Journal")
        call_command('load_default_settings')

        setting, c = Setting.objects.get_or_create(
            name='editor_revisions_complete_receipt',
            types='rich-text',
            group=SettingGroup.objects.filter(name='email'),
            is_translatable=True,
            pretty_name='Editor Revisions Complete Receipt',
            description='Email sent to the handling editor(s) when an author completes revisions.',
        )

        setting_value, _ = SettingValue.objects.get_or_create(
            journal=None,
            setting=setting,
        )
        setting_value.value = editor_revisions_complete_receipt
        setting_value.save()

    reverse_func = migrations.RunPython.noop

    dependencies = [
        ('journal', '0057_auto_20230208_1233'),
    ]


    operations = [
        migrations.RunPython(forwards_func, reverse_code=reverse_func),
    ]
