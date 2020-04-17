from django.contrib import admin
from listening.models import Sentence
from listening.widgets import AudioWiget
from listening.models import AudioField
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.


class SentenceResource(resources.ModelResource):

    class Meta:
        model = Sentence


class SentenceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'audio_play', 'content_play')
    formfield_overrides = {AudioField: {'widget': AudioWiget}}
    resource_class = SentenceResource
    ordering = ('id', )


admin.site.register(Sentence, SentenceAdmin)
