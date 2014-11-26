def test_base_urls():
    try:
        from django.conf.urls.defaults import *
    except ImportError:
        print "***FAIL:from django.conf.urls.defaults import * ***"
    try:
        from django.conf import settings
    except ImportError:
        print "***FAIL: from django.conf import settings ***"
    try:
        from django.contrib import admin
    except ImportError:
        print "***FAIL: from django.contrib import admin ***"
    try:
        from django.contrib.auth.decorators import login_required
    except ImportError:
        print "***FAIL: from django.contrib.auth.decorators import login_required ***"
    try:
        from django.contrib.auth.models import User
    except ImportError:
        print "***FAIL: from django.contrib.auth.models import User ***"
    try:
        from django.views.generic.list_detail import object_list
    except ImportError:
        print "***FAIL: from django.views.generic.list_detail import object_list ***"
