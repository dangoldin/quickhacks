import os
import re
import subprocess
import pprint
import sys
from collections import defaultdict

if len(sys.argv) == 1:
    root = os.path.realpath(os.path.dirname(__file__))
else:
    root = sys.argv[1]

RE_FILE = re.compile(r'[\'\"](.+?)[\"\']')

def create_tree(parent, pairs):
    tree = {}
    for i,j in pairs:
        if j == parent:
            tree[i] = create_tree(i, pairs)
    return tree

def create_tree_multiple(parents, pairs):
    tree = {}
    for parent in parents:
        tree[parent] = create_tree(parent,pairs)
    return tree

def get_file_pairs(command):
    pairs = []
    out = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE).communicate()[0]
    for l in out.split("\n"):
        data = l.split(':')
        if len(data) == 2:
            filename = data[0]
            m = RE_FILE.search(data[1])
            if m:
                match = m.group(1)

                filename = os.path.relpath(os.path.realpath(os.path.join(root, filename)))
                match = os.path.relpath(os.path.realpath(os.path.join(root, 'templates', match)))

                pairs.append((filename,match))

    return pairs

def child_nodes(pairs):
    children = set()
    for i,j in pairs:
        children.add(i)
    #print 'Children:',children
    return children

def parent_nodes(pairs):
    parents = set()
    children = child_nodes(pairs)
    for i,j in pairs:
        if j not in children:
            parents.add(j)
    #print 'Parents:',parents
    return parents

extend_pairs = get_file_pairs('(cd %s; find . -name "*.html" -exec grep -Hi "{%% extends" {} \;)' % root)
extend_parents = parent_nodes(extend_pairs)
extend_tree = create_tree_multiple(extend_parents, extend_pairs)
print 'Extends:', pprint.pformat(extend_tree, indent=1)

# Need to switch the order for these so we see the file that's calling the include first
include_pairs = [(j,i) for i,j in get_file_pairs('(cd %s; find . -name "*.html" -exec grep -Hi "{%% include" {} \;)' % root)]
#include_pairs = get_file_pairs('find . -name "*.html" -exec grep -Hi "{% include" {} \;')
include_parents = parent_nodes(include_pairs)
include_tree = create_tree_multiple(include_parents, include_pairs)
print 'Includes:', pprint.pformat(include_tree, indent=1)
