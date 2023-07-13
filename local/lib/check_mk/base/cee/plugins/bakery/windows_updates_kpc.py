#!/usr/bin/env python3
# Copyright (C) 2023 K&P Computer Service- und Vertriebs-GmbH - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Matthias Binder m.binder@kpc.de, July 2023
#
################################################################################################################
# For Support and Sales Please Contact K&P Computer!
#
# E-Mail: hds@kpc.de
#
# 24/7 Helpdesk-Support:
# International: +800 4479 3300
# Germany: +49 6122 7071 330
# Austria: +43 1 525 1833
#
# Web Germany: https://www.kpc.de
# Web Austria: https://www.kpc.at
# Web International: https://www.kpc.de/en
#
################################################################################################################

from pathlib import Path
from .bakery_api.v1 import FileGenerator, OS, Plugin, register
from typing import Any, Dict

def get_windows_updates_kpc_files(conf: Dict[str, Any]) -> FileGenerator:
        yield Plugin(
            base_os=OS.WINDOWS,
            source=Path("windows_updates_kpc.ps1"),
            interval=10800,
            timeout=600,
            asynchronous=True)

register.bakery_plugin(
    name="windows_updates_kpc",
    files_function=get_windows_updates_kpc_files,
)
