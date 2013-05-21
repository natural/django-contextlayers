#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

from contextlayers.models import LayerBase


class ThemeLayer(LayerBase):
    """Layer that provides additional CSS at matched paths."""

    markup = models.TextField(_('markup'), default='', blank=True,
        help_text=_("""
        CSS styles and other HTML markup inserted into the template.
        """))

    class Meta:
        verbose_name = 'Theme Layer'

    class LayerMeta:
        pass

    def contribute_to_context(self, layer_context, global_context):
        """Appends the markup for this theme to the layer context."""
        layer_context.setdefault('theme', []).append(self.markup)


class VersionLayer(LayerBase):
    """Layer that provides version information at matched paths.

    Note that this model is a specialized variation of a more generic
    "key-value" layer.  We're using the specific name "Version" to imply the
    versioning semantics.

    """

    version = models.CharField(_('version'), default='0', blank=True,
        max_length=128, help_text=_("""Version number or string."""))

    class Meta:
        verbose_name = 'Version Layer'

    class LayerMeta:
        pass

    def contribute_to_context(self, layer_context, global_context):
        """Appends the version text for this record to the layer context."""
        layer_context.setdefault('version', []).append(self.version)
