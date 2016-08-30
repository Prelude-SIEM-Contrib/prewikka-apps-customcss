from __future__ import absolute_import, division, print_function, unicode_literals

import pkg_resources

from prewikka import version, view, template, hookmanager, database, response, theme

"""Custom CSS plugin"""

import os
import lesscpy

_LESS_MAIN_PARAM = { "primary-color" : N_("Primary color"),
                     "primary-background-color": N_("Primary background"),
                     "fieldset-background": N_("Fieldset background"),
                     "chart-background": N_("Background color for graphs")
                   }

_LESS_TEXT_COLOR = { "link": N_("Color for Web Links"),
                     "active-text": N_("Color for text on the main content area")
                   }

_LESS_OTHER = { "border": N_("Color for borders in Prewikka"),
                "active-background": N_("Background color for the main content area"),
                "table-header": N_("Color of the table Header"),
                "table-row-even": N_("Color for Even rows in a table"),
                "table-row-odd": N_("Color for Odd rows in a table"),
                "table-background": N_("Background color for tables")
              }

_ALL_LESS = dict(_LESS_MAIN_PARAM, **dict(_LESS_TEXT_COLOR, **_LESS_OTHER))

def write_less_file(path):
    with open(path, 'w') as less_file:          
        for i in _ALL_LESS.keys():
            less_file.write("@%s: %s;\n" % (i, env.request.parameters.get(i)))

class CssParameters(view.Parameters):

    def register(self):
        for i in _ALL_LESS.keys():
            self.optional(i, str)

        self.optional("action_serv",str)
        self.optional("theme_name",str)
        self.optional("name",str)

class CustomCSS(view.View): 
    plugin_name = "CustomCSS"
    plugin_author = "David Casier, Thomas Andrejak"
    plugin_license = version.__license__
    plugin_version = version.__version__
    plugin_copyright = version.__copyright__
    plugin_description = N_("A plugin that allow you to customize your CSS")
    plugin_htdocs = (("customcss", pkg_resources.resource_filename(__name__, 'htdocs')),)

    view_parameters = CssParameters

    @view.route("/customcss", methods=['GET','POST'], menu=(N_('CustomCSS'), N_('CustomCSS')))
    def render(self):
        prewikka_path = pkg_resources.resource_filename("prewikka","htdocs")
        file_style = "%s/css/style.less" % prewikka_path
        file_tmp = "%s/less/tmp.less" % pkg_resources.resource_filename("customcss", "htdocs")
        dir_themes = "%s/css/themes/" % prewikka_path
        cur_theme = env.request.user.get_property("theme", default="cs")
        dataset = {}
        dataset["less_main_param"] = _LESS_MAIN_PARAM
        dataset["less_text_color"] = _LESS_TEXT_COLOR
        dataset["less_other"] = _LESS_OTHER
        dataset["cur_theme"] = cur_theme
        dataset["list_base_themes"] = ["cs", "blue", "bright", "green", "classic", "dark", "yellow"]
        dataset["list_themes"] = theme.getThemes()

        if env.request.parameters.get("action_serv") == "Save":
            name = env.request.parameters.get("theme_name")
            if name and name.isalnum():
                    write_less_file(file_tmp)
                    os.system("lesscpy -I %s %s > %s%s.css" % (file_tmp, file_style, dir_themes, name))
                    os.remove(file_tmp)
            return response.PrewikkaRedirectResponse(url_for("."))

        return template.PrewikkaTemplate(__name__, "templates/customcss.mak").render(**dataset)

    @view.route("/customcss/switch", methods=['POST'])
    def switch(self):
        user = env.request.user
        user.begin_properties_change()
        user.set_property("theme", env.request.parameters.get("name"))
        user.set_locale()
        user.commit_properties_change()
        return response.PrewikkaDirectResponse({"type": "reload"})

    @view.route("/customcss/remove", methods=['POST'])
    def remove(self):
        dir_themes = "%s/css/themes/" % pkg_resources.resource_filename("prewikka","htdocs")
        os.remove(dir_themes+env.request.parameters.get("name")+".css")
        return response.PrewikkaRedirectResponse(url_for("customcss"))
