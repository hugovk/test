#!/usr/bin/env python

try:
    print("Try to import PyQt5...")
    from PyQt5.QtGui import QImage, qRgb, qRgba
    print("PyQt5 imported!")
except Exception as e:
        print("PyQt5 not imported")
        print str(e)
    try:
        print("Try to import PyQt4...")
        from PyQt4.QtGui import QImage, qRgb, qRgba
        print("PyQt4 imported!")
    except Exception as e:
        print("PyQt4 not imported")
        print str(e)
