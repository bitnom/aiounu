# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiounu']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.3,<4.0.0']

setup_kwargs = {
    'name': 'aiounu',
    'version': '0.1.2',
    'description': 'Asyncio module for unu in Python3 using aiohttp.',
    'long_description': None,
    'author': 'TensorTom',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)