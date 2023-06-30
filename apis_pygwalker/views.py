from django.shortcuts import render
from django.views.generic import View
from django.utils.safestring import mark_safe
import pandas as pd
import pygwalker as pyg

from apis_ontology.models import Person

class Pygwalker(View):
    def get(self, request, *args, **kwargs):
        df = pd.DataFrame(list(Person.objects.all().values()))
        content = mark_safe(pyg.to_html(df))
        return render(request, 'pygwalker.html', {'content': content})
