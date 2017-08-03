# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 14:24:26 2017

@author: zck

Download the nyu_depth_v2 dataset.

Website: http://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html
"""


from urllib2 import urlopen # Python 2
# from urllib.request import urlopen # Python 3

def run():
    url = 'http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/nyu_depth_v2_labeled.mat'
    response = urlopen(url)
    CHUNK = 10 * 1024 * 1024
    total = 0
    with open('nyu_depth_v2_labeled.mat', 'wb') as f:
        while True:
            chunk = response.read(CHUNK)
            if not chunk:
                break
            f.write(chunk)
            total += len(chunk)
            print('{} MB data have downloaded.'.format(total/(1024*1024)))

if __name__ == '__main__':
    run()
