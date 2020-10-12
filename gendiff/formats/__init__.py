"""Imported formats."""

# TODO: fix # noqa F401
from gendiff.formats.json import render_json as json
from gendiff.formats.simple import render_diff as simple
from gendiff.formats.plain import render_diff as plain

FORMATS = (
    JSON,
    SIMPLE,
    PLAIN,
) = (
    'json',
    'simple',
    'plain',
)
