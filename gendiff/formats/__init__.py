"""Formats."""
from gendiff.formats.json import render_json
from gendiff.formats.simple import render_diff as render_simple
from gendiff.formats.plain import render_diff as render_plain

JSON, SIMPLE, PLAIN = 'json', 'simple', 'plain'
