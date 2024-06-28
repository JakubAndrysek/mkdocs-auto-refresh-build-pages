# MKDocs Auto Refresh Build Pages Plugin


<p align="center">
<a href="https://hits.seeyoufarm.com/api/count/graph/dailyhits.svg?url=https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=👀&edge_flat=true"/></a>
<a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/JakubAndrysek/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://pypi.org/project/mkdocs-auto-refresh-build-pages/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/stargazers" target="_blank"><img src="https://img.shields.io/github/stars/JakubAndrysek/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/forks" target="_blank"><img src="https://img.shields.io/github/forks/JakubAndrysek/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/issues" target="_blank"><img src="https://img.shields.io/github/issues/JakubAndrysek/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/discussions" target="_blank"><img src="https://img.shields.io/github/discussions/JakubAndrysek/mkdocs-auto-refresh-build-pages?style=flat-square"></a>
<a href="https://pypistats.org/packages/mkdocs-auto-refresh-build-pages" target="_blank"><img src="https://static.pepy.tech/personalized-badge/mkdocs-auto-refresh-build-pages?period=month&units=international_system&left_color=black&right_color=orange&left_text=Downloads"></a>
</p>



MkDocs plugin that automatically refreshes the build pages when the documentation is updated.

## Installation

Install the plugin using pip from [PyPI](https://pypi.org/project/mkdocs-auto-refresh-build-pages/):

```bash
pip install mkdocs-auto-refresh-build-pages
```

## Usage

Add the following lines to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - auto-refresh-build-pages:
      update_message: "The page has been updated. Do you want to reload?"
      yes_button_text: "Yes"
      no_button_text: "No"
      check_interval_seconds: 5
```

- `update_message` (optional): The message that will be displayed when the page is updated. Default: "The page has been updated. Do you want to reload?"
- `yes_button_text` (optional): The text of the "Yes" button. Default: "Yes"
- `no_button_text` (optional): The text of the "No" button. Default: "No"
- `check_interval_seconds` (optional): The interval in seconds at which the page will be checked for updates. Default: 5

## Example screenshot

<img src="./docs/media/popup.png" alt="example" style="border: 2px solid black;">


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Do You Enjoy My Work?
Then you can consider:

- supporting me on GitHub Sponsors: [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/jakubandrysek)

## License

[MIT](https://github.com/JakubAndrysek/mkdocs-auto-refresh-build-pages/blob/main/LICENSE)