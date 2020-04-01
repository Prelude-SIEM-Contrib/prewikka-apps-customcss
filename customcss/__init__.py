from __future__ import absolute_import, division, print_function, unicode_literals

import os
import pkg_resources
import re
import tempfile

from prewikka import error, response, template, theme, view

"""Custom CSS plugin"""

_PROTECTED_THEMES = ["blue", "bright", "classic", "cs", "dark", "green", "yellow"]

_LESS_VARIABLES = [
    ("Main colors", [
        ("primary-color", N_("Primary color")),
        ("primary-background-color", N_("Primary background")),
        ("fieldset-background", N_("Fieldset background")),
    ]),
    ("Link and text colors", [
        ("link", N_("Color for web links")),
        ("active-text", N_("Color for text on the main content area")),
    ]),
    ("Table colors", [
        ("table-header", N_("Color of the table header")),
        ("table-row-even", N_("Color for even rows in a table")),
        ("table-row-odd", N_("Color for odd rows in a table")),
        ("table-background", N_("Background color for tables")),
    ]),
    ("Other colors", [
        ("border", N_("Color for borders")),
        ("active-background", N_("Background color for the main content area")),
        ("chart-background", N_("Background color for graphs")),
        ("tooltip-text", N_("Text color for tooltips")),
        ("tooltip-background", N_("Background color for tooltips")),
    ])
]


class CustomCSS(view.View):
    plugin_name = "CustomCSS"
    plugin_author = "David Casier, Thomas Andrejak"
    plugin_license = "GPL"
    plugin_version = "5.1.0"
    plugin_copyright = "CSSI"
    plugin_description = N_("A plugin that allows you to customize your CSS")
    plugin_htdocs = (("customcss", pkg_resources.resource_filename(__name__, 'htdocs')),)

    def _check_theme(self, theme):
        if not (theme and re.match("[a-z]+$", theme)):
            raise error.PrewikkaUserError(None, "Invalid name")

        if theme in _PROTECTED_THEMES:
            raise error.PrewikkaUserError(None, "Cannot alter protected theme")

    @view.route("/customcss", menu=(N_('Themes'), N_('Themes')))
    def render(self):
        return template.PrewikkaTemplate(__name__, "templates/customcss.mak").render(
            less_variables=_LESS_VARIABLES,
            current_theme=env.request.user.get_property("theme", default="cs"),
            themes=theme.get_themes()
        )

    @view.route("/customcss/save", methods=['POST'])
    def save(self):
        theme = env.request.parameters.get("theme")
        self._check_theme(theme)

        prewikka_path = pkg_resources.resource_filename("prewikka", "htdocs")
        style = os.path.join(prewikka_path, "css", "style.less")
        output = os.path.join(prewikka_path, "css", "themes", "%s.css" % theme)

        tmp_file = tempfile.NamedTemporaryFile()
        with open(tmp_file.name, "w") as f:
            for category, variables in _LESS_VARIABLES:
                for name, label in variables:
                    f.write("@%s: %s;" % (name, env.request.parameters.get(name)))

        os.system("lesscpy -I %s %s > %s" % (tmp_file.name, style, output))
        return response.PrewikkaResponse({"type": "reload", "target": "window"})

    @view.route("/customcss/switch", methods=['POST'])
    def switch(self):
        env.request.user.set_property("theme", env.request.parameters.get("theme"))
        env.request.user.sync_properties()
        return response.PrewikkaResponse({"type": "reload", "target": "window"})

    @view.route("/customcss/remove", methods=['POST'])
    def remove(self):
        theme = env.request.parameters.get("theme")
        self._check_theme(theme)

        filename = os.path.join(pkg_resources.resource_filename("prewikka", "htdocs"), "css", "themes", "%s.css" % theme)
        os.remove(filename)

        return response.PrewikkaResponse({"type": "reload", "target": "view"})
