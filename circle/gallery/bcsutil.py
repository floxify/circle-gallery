#!/usr/bin/env python
#coding:utf8

import os
import logging
import pybcs

pybcs.init_logging(logging.INFO)

AK = 'X5QlEt746l0sXLmuTqKo5a7u'
SK = 'Ku0yGkDm4RW5SlHtpSuFtPR44IUBzgia'
BUCKET='circle-android'
SIGNED_URL = 'http://bcs.duapp.com/circle-android{}?sign=MBO:X5QlEt746l0sXLmuTqKo5a7u:2uovpD7fGzCTslbocWn8vt%2BCi3U%3D'

bcs = pybcs.BCS('http://bcs.duapp.com/', AK, SK, pybcs.HttplibHTTPC)
b = bcs.bucket(BUCKET)

def list_buckets():
    lst = bcs.list_buckets()
    return lst

def list_objects():
    objects = b.list_objects_raw()
    return objects
    
def generate_url(obj_path):
    return SIGNED_URL.format(obj_path)


def list_obj_urls():
    objects = list_objects()
    urls = [generate_url(o['object']) for o in objects]
    for u in urls:
        print u
    return urls



if __name__ == "__main__":
#    buckets = bucket_list()
#    for b in buckets:
#        print b
#    b.make_public()
#    objects = list_objects()
#    if objects is not None:
#        for o in objects:
#            print generate_url(o['object'])

    urls = list_obj_urls()
    if urls is not None:
        for u in urls:
            print u
