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
def test_events_views():
    try:
        from django.utils.translation import ugettext
    except ImportError:
        print "***FAIL: from django.utils.translation import ugettext ***"
    try:
        from django.shortcuts import render_to_response, get_object_or_404
    except ImportError:
        print "***FAIL: from django.shortcuts importi render_to_response,get_object_or_404 ***"
    try:
        from django.template import RequestContext
    except ImportError:
        print "***FAIL: from django.template import RequestContext ***"
    try:
        from dateutil.parser import parse
    except ImportError:
        print "***FAIL: from dateutil.parser import parse ***"
    try:
        from django.core import serializers
    except ImportError:
        print "***FAIL: from django.core import serializers ***"
    try:
        from django.http import HttpResponseRedirect, HttpResponse, Http404
    except ImportError:
        print "***FAIL: from django.http import HttpResponseRedirect,HttpResponse,Http404 ***"
    try:
        from django.views.decorators.http import requre_POST
    except ImportError:
        print "***FAIL: from django.views.decorators.http import require_POST ***"
    try:
        from django.core.urlresolvers import reverse
    except ImportError:
        print "***FAIL: form django.core.urlresolvers import reverse ***"
