'''
运行文件
__author__ = ‘zhourong‘
'''
# -*- coding: utf-8 -*-

import pytest

# pytest.main(["-m test","--html=testreport/report.html"])
pytest.main(["-m smoke","--html=testreport/report.html"])
# pytest.main(["","--html=testreport/report.html"])