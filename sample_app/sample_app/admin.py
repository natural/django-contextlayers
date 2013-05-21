#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from contextlayers.admin import LayerAdmin
from .models import ThemeLayer, VersionLayer


class ThemeLayerAdmin(LayerAdmin):
    """Theme Layer admin."""


class VersionLayerAdmin(LayerAdmin):
    """Version Layer admin."""






admin.site.register(ThemeLayer, ThemeLayerAdmin)
admin.site.register(VersionLayer, VersionLayerAdmin)
