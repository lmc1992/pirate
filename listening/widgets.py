from django.forms import widgets
from django.utils.safestring import mark_safe


class AudioWiget(widgets.URLInput):

    def render(self, name, value, attrs=None, renderer=None):
        if value is not None:
            self.template_name = 'audio.html'
        return super().render(name, value, attrs, renderer)
