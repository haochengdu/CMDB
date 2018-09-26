#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

from Client.core import handler

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)


if __name__ == '__main__':

    handler.ArgvHandler(sys.argv)

