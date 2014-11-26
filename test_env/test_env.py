def test_base_urls():
    try:
        from django.conf.urls import patterns,url,include
    except ImportError:
        print "***FAIL:from django.conf.urls import patterns,url,include ***"
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
def test_events_models():
    try: 
        from datetime import datetime,timedelta
    except ImportError:
        print "***FAIL: from datetime import datetime,timedelta ***"
    try:
        from django.db import models
    except ImportError:
        print "***FAIL: from django.db import models ***"
    
    try:
        from django.contrib.auth.models import User
    except ImportError:
        print "***FAIL: from django.contrib.auth.models import User ***"
    try:
        from django.db.models.query import QuerySet
    except ImportError:
        print "***FAIL: from django.db.models.query import QuerySet ***"
