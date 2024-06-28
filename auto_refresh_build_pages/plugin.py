# Author: Jakub Andrýsek
# Email: email@kubaandrysek.cz
# Website: https://kubaandrysek.cz
# License: MIT
# GitHub: https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages
# PyPI: https://pypi.org/project/mkdocs-auto-refresh-build-pages/


from pathlib import Path

from mkdocs.config import Config
from mkdocs.plugins import BasePlugin
import os
from jinja2 import Environment, FileSystemLoader
import mkdocs.config.config_options as c


class AutoRefreshBuildPagesConfig(Config):
    update_message = c.Type(
        str, default="The page has been updated. Do you want to reload?"
    )
    yes_button_text = c.Type(str, default="Yes")
    no_button_text = c.Type(str, default="No")
    check_interval_seconds = c.Type(int, default=60)  # in seconds


class AutoRefreshBuildPages(BasePlugin[AutoRefreshBuildPagesConfig]):
    def on_config(self, config, **kwargs):
        """
        Event trigger on config.
        See https://www.mkdocs.org/user-guide/plugins/#on_config.
        """
        config["extra_javascript"].append("js/auto_refresh_build_pages.js")

    def on_post_build(self, config):
        """
        Event trigger on post build.
        See https://www.mkdocs.org/user-guide/plugins/#on_post_build.
        """
        template_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "js")),
            autoescape=True,
        )
        template = template_env.get_template("auto_refresh_build_pages.js.jinja")

        rendered_js = template.render(
            update_message=self.config.update_message,
            yes_button_text=self.config.yes_button_text,
            no_button_text=self.config.no_button_text,
            check_interval_seconds=self.config.check_interval_seconds,
        )

        js_output = Path(config["site_dir"]) / "js" / "auto_refresh_build_pages.js"
        js_output.parent.mkdir(parents=True, exist_ok=True)

        with open(js_output, "w") as f:
            f.write(rendered_js)
