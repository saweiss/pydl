# -*- encoding: utf-8 -*-
# PyDL v0.1.0
# IDL functionality in Python
# Copyright © 2018, Samuel A. Weiss.
# See /LICENSE for licensing information.

"""
IDL-like plotting in Python.

:Copyright: © 2018, Samuel A. Weiss.
:License: BSD (see /LICENSE).
"""

import numpy as np
import matplotlib.pyplot as plt


class Graphic():
    """
    A mimic of the return value for IDL graphics functions.
    """

    def __init__(self, antialias=True, arrow_style=1, aspect_ratio=0, axes=None,
                 background_color=[255, 255, 255], background_transparency=100,
                 clip=True, color=[0, 0, 0], crosshair=None, eqn_samples=1000,
                 eqn_userdata=None, equation=None, fill_background=False,
                 fill_color=[128, 128, 128], fill_level=None,
                 fill_transparency=0, font_color=[0, 0, 0],
                 font_name='DejaVu Sans', font_style=0, grid_units=None,
                 head_angle=30, head_indent=0.4, head_size=1, hide=False,
                 histogram=False, interpolate=False, linestyle=0, mapgrid=None,
                 mapprojection=None, map_projection=None, max_value=None,
                 min_value=None, name=None, position=[0, 0, 1, 1], rgb_table=0,
                 scale_center=None, scale_factor=1, stairstep=False,
                 sym_color=[0, 0, 0], sym_filled=False, sym_fill_color=None,
                 sym_increment=1, sym_object=None, sym_size=1, sym_thick=1,
                 sym_transparency=0, symbol=None, thick=1, title=None,
                 transparency=0, uvalue=None, vert_colors=None, window=None,
                 window_title=None, xrange=None, yrange=None, zvalue=0):
        """
        Unless specified, initialize ``Graphic``'s properties to match
        the default arguments in an IDL graphics function.
        """
        self.antialias = antialias
        self.arrow_style = arrow_style
        self.aspect_ration = aspect_ratio
        self.axes = axes
        self.background_color = background_color
        self.background_transparency = background_transparency
        self.clip = clip
        self.color = color
        self.crosshair = crosshair
        self.eqn_samples = eqn_samples
        self.eqn_userdata = eqn_userdata
        self.equation = equation
        self.fill_background = fill_background
        self.fill_color = fill_color
        self.fill_level = fill_level
        self.fill_transparency = fill_transparency
        self.font_color = font_color
        self.font_name = font_name
        self.font_style = font_style
        self.grid_units = grid_units
        self.head_angle = head_angle
        self.head_indent = head_indent
        self.head_size = head_size
        self.hide = hide
        self.histogram = histogram
        self.interpolate = interpolate
        self.linestyle = linestyle
        self.mapgrid = mapgrid
        self.mapprojection = mapprojection
        self.map_projection = map_projection
        self.max_value = max_value
        self.min_value = min_value
        self.name = name
        self.position = position
        self.rgb_table = rgb_table
        self.scale_center = scale_center
        self.scale_factor = scale_factor
        self.stairstep = stairstep
        self.sym_color = sym_color
        self.sym_filled = sym_filled
        self.sym_fill_color = sym_fill_color
        self.sym_increment = sym_increment
        self.sym_object = sym_object
        self.sym_size = sym_size
        self.sym_thick = sym_thick
        self.sym_transparency = sym_transparency
        self.symbol = symbol
        self.thick = thick
        self.title = title
        self.transparency = transparency
        self.uvalue = uvalue
        self.vert_colors = vert_colors
        self.window = window
        self.window_title = window_title
        self.xrange = xrange
        self.yrange = yrange
        self.zvalue = zvalue
