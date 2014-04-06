#    This file is part of Autorerun
# 
#    Autorerun is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    Autorerun is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
        'watchdog',
    ]

setup(name='autorerun',
      version='0.1.1',
      description='autorerun',
      long_description=""" Starts and automatically restarts a given command if certain files change. Good for development to rerun server when code is changed. """,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Database",
        ],
      author='Bradley Arsenault',
      author_email='bradley.allen.arsenault@gmail.com',
      url='http://autorerun.readthedocs.org/en/latest/',
      keywords='process management automatic rerun development',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="autorerun",
      entry_points="""\
      [console_scripts]
      autorerun = autorerun.autorerun:main
      """,
      )

