#!/usr/bin/python

import bintrees

def event_stream(filename):
    root = bintrees.AVLTree()
    with open(filename, 'r') as log:
        while True:
            line = log.readline().split()
            if len(line) > 0:
                root.insert(line[0], ' '.join(line))
                if (float(root.max_key()) - float(root.min_key())) > 300:
                    yield str(root.pop(root.min_key()))
            else:
                pass 

if __name__ == "__main__":
    for event in event_stream('1'):
        print event
