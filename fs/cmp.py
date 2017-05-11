# coding: utf8

import sys
import os
import argparse

def find_same_diff(path_a, path_b):
    same = []
    diff = []
    for r, ds, fs in os.walk(path_a):
        for f in fs:
            #print os.path.join(f)
            r_b = r.replace(path_a, path_b)
            fn_a = os.path.join(r, f)
            fn_b = os.path.join(r_b, f)
            if not os.path.exists(fn_b):
                diff.append(fn_a)
            else:
                same.append(f)
    return same, diff

if __name__=="__main__":
    
    if len(sys.argv)<3:
        print "Arg Error. command format: python cmp.py path_a path_b"
        exit(0)
    path_a = sys.argv[1]
    path_b = sys.argv[2]
    
    same = []
    diff = []
    same, in_a_not_in_b = find_same_diff(path_a, path_b)
    
    print u"共同的文件共 %s 个\n" % len(same)
    
    print u"%s 没有以下 %s 个文件:" % (path_b, len(in_a_not_in_b), )
    for fn in in_a_not_in_b:
        print fn
    
    print u""
    
    same, in_b_not_in_a = find_same_diff(path_b, path_a)
    print u"%s 没有以下 %s 个文件:" % (path_a, len(in_b_not_in_a), )
    for fn in in_b_not_in_a:
        print fn
    
    