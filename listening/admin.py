from django.contrib import admin
from django.shortcuts import reverse
from listening.models import Sentence
from listening.widgets import AudioWiget
from listening.models import AudioField
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.http import HttpResponseRedirect

# Register your models here.


class SentenceResource(resources.ModelResource):

    class Meta:
        model = Sentence


class SentenceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'audio_play', 'content_play')
    formfield_overrides = {AudioField: {'widget': AudioWiget}}
    resource_class = SentenceResource
    ordering = ('id', )

    def response_change(self, request, obj):
        if obj.id and "_addandnext" in request.POST:
           redirect_url = reverse('admin:listening_sentence_change', kwargs={'object_id': obj.id + 1})
           return HttpResponseRedirect(redirect_url)
        return super(ImportExportModelAdmin,self).response_change(request,obj)


admin.site.register(Sentence, SentenceAdmin)
