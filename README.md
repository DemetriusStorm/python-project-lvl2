[![Build Status](https://travis-ci.com/travis-ci/travis-web.svg?branch=master)](https://travis-ci.com/travis-ci/travis-web)
[![Maintainability](https://api.codeclimate.com/v1/badges/67902e4998249efb97a2/maintainability)](https://codeclimate.com/github/DemetriusStorm/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/67902e4998249efb97a2/test_coverage)](https://codeclimate.com/github/DemetriusStorm/python-project-lvl2/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Python CI](https://github.com/DemetriusStorm/python-project-lvl2/workflows/Python%20CI/badge.svg)

## python-project-lvl2
Comparison of two files. The output data with specified format type.
### How to Install and run package.<br>
``pip install git+https://github.com/DemetriusStorm/python-project-lvl2``
### Usefull
Usage: ``gendiff [-h] [-f [--format] FORMAT] first_file second_file``

Format comparing files supports are: ``'.json'``, ``'.yml'``
>More about [json](https://en.wikipedia.org/wiki/JSON), [yaml](https://en.wikipedia.org/wiki/YAML)

Getting help:
``gendiff -h``

Run with the DEFAULT output format (stylish). Or with specify formats:

``gendiff first_file second_file``

Stylish output, plain text output or json output

``gendiff --format=stylish first_file second_file``

``gendiff --format=plain first_file second_file``
 
``gendiff --format=json first_file second_file``

Comparing JSON files
[![asciicast](https://asciinema.org/a/365554.svg)](https://asciinema.org/a/365554)

Comparing YAML files
[![asciicast](https://asciinema.org/a/365555.svg)](https://asciinema.org/a/365555)

Comparing nested
[![asciicast](https://asciinema.org/a/365557.svg)](https://asciinema.org/a/365557)

Result in PLAIN
[![asciicast](https://asciinema.org/a/365559.svg)](https://asciinema.org/a/365559)

Result in JSON
[![asciicast](https://asciinema.org/a/365560.svg)](https://asciinema.org/a/365560)
