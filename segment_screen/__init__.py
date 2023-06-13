# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SegmentScreen
                                 A QGIS plugin
 This plugin doing segment to shape
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-19
        copyright            : (C) 2023 by KH.Pang
        email                : ggen652@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SegmentScreen class from file SegmentScreen.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .segment_screen import SegmentScreen
    return SegmentScreen(iface)