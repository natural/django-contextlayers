Context Layers for Django
==========================

This app provides "context layers" for Django templates.  A context
layer is a model object that contributes data to a template during
rendering.

Context layers match on URL paths.  When a match is found, the model
record is asked for data to contribute, and that data is sent along to
the template context.

Context layers have activation dates.  You can set the layer to turn
on (become active) at a specific date/time, and also to turn off
(become inactive).

Context layers were originally developed to provide:

  * Additional CSS to a page; see the sample app for an implementation
  * Selective enabling or disabling of adverts
  * Conditional markup during a site beta period

This package doesn't provide any concrete models, so you still have to
provide your own models to specify what your layers do (in other
words, how your layers contribute to the context).  Again, see the
sample app for an implementation.


Install
-------

Pull down the app:

    $ pip install django-contextlayers

Add it to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
      ...
      'contextlayers'
    )

Then include the context processor in your settings:

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'contextlayers.context_processors.layer_tool',
    )


Making Your Own Layers
----------------------

First you define a layer class.  You'll probably want to subclass
`LayerBase`, but it's not strictly necessary.  You must include a
`LayerMeta` property, and you must supply a `contribute_to_context`
method.  Example from the sample:

    from contextlayers.models import LayerBase

    class ThemeLayer(LayerBase):
        markup = models.TextField(...)

        class LayerMeta:
            pass

        def contribute_to_context(self, layer_context, global_context):
            layer_context.setdefault('theme', []).append(self.markup)

When this layer is matched, the content of the `markup` field will be added
to the template at `layers.theme`.

Next, sync your database:

    $ ./manage.py syncdb

The layers won't be visible until you add support to your templates.
For example:

    {% for css in layers.theme %}
      {{ css|safe }}
    {% endfor %}

What you do with `layers.*` depends on what the layer provides to the
context and how your templates should use it.

Finally, define the layer records in the Django admin.  Take note of
the help text for the dates and path values.
