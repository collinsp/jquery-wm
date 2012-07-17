#!/usr/bin/python

import httplib, urllib, sys, os

# Define the parameters for the POST request and encode them in
# a URL-safe format.

js_code = open('jquery-wm.js', 'r').read()

params = urllib.urlencode([
    ('js_code', js_code),
    ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
    ('output_format', 'text'),
    ('output_info', 'compiled_code'),
  ])

# Always use the following value for the Content-type header.
headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
data = response.read()
conn.close

os.remove('jquery-wm.min.js')
f = open('jquery-wm.min.js','w')
f.write(data)
f.close()

