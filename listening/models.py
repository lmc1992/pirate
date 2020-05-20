from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class AudioField(models.URLField):
    pass


class Sentence(models.Model):
    audio = AudioField()
    content = RichTextField(help_text='标记错误（红）发音问题（黄）')

    def audio_play(self):
        return format_html(
            '<audio src={} controls="controls"></audio>',
            self.audio
        )

    def content_play(self):
        return mark_safe(self.content)


