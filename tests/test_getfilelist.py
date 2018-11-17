#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from getfilelistpy import getfilelist

resource = {
    "api_key": "#####",
    "id": "#####",
    "fields": "files(id,name)",
}
result = getfilelist.GetFileList(resource)
print(result)
