"""Formats."""
from gendiff.formats.json import render_json  # noqa: F401
from gendiff.formats.simple import render_diff as render_simple  # noqa: F401
from gendiff.formats.plain import render_diff as render_plain  # noqa: F401, I001


JSON, SIMPLE, PLAIN = 'json', 'simple', 'plain'
