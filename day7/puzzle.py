"""Day 7
"""

from __future__ import annotations
from typing import List
import sys

class Directory(object):
    def __init__(self, name: str):        
        self.name = name
        self.parent = None
        self.subdirs = []
        self.files = {}
    
    def get_size(self):
        subdir_size = sum([sd.get_size() for sd in self.subdirs])
        file_size = sum(self.files.values())
        return subdir_size + file_size
    
    def get_subdirs_with_max_size(self, max_size: int) -> List[Directory]:
        max_size_subdirs = []
        for sd in self.subdirs:
            if sd.get_size() < max_size:
                max_size_subdirs.append(sd)

            # Also check recursively
            max_size_subdirs.extend(sd.get_subdirs_with_max_size(max_size))

        return max_size_subdirs
    
    def get_recursive_sizes(self):
        sizes = [self.get_size()]
        for sd in self.subdirs:
            sizes.extend(sd.get_recursive_sizes())
        return sizes
    
    def print(self, level=0):
        print(' ' * 2*level, end='')
        print(f'{self.name} (total size: {self.get_size()})')

        for k,v in self.files.items():
            print(' ' * 2*(level+1), end='')
            print(f'{k} {v}')
        
        for sd in self.subdirs:
            sd.print(level+1)

def parse_directories(fname: str = 'input.txt') -> Directory:
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    root = Directory('/')
    curr_dir = root
    for l in lines[1:]: # Skip first line for root dir
        if l.startswith('$ cd'):
            # Change directories
            cd_name = l.split()[-1]
            if cd_name == '..':
                curr_dir = curr_dir.parent
            else:
                new_dir = Directory(l.split()[-1] + '/')

                curr_dir.subdirs.append(new_dir)
                new_dir.parent = curr_dir

                curr_dir = new_dir
        elif l.startswith('$ ls') or l.startswith('dir'):
            continue
        else:
            # We must be a file size/name line
            size = int(l.split()[0])
            name = l.split()[1]

            curr_dir.files[name] = size
        
    #root.print()
    
    return root

def sum_max_size_dirs(fname: str = 'input.txt', max_size: int = 100000) -> None:
    root = parse_directories(fname)

    subdirs_with_max_size = root.get_subdirs_with_max_size(max_size)

    print(f'Combined size of all subdirs under size {max_size}: {sum([sd.get_size() for sd in subdirs_with_max_size])}')

def find_min_dir_to_del_size(fname: str = 'input.txt', allowed_size: int = 40000000) -> None:
    root = parse_directories(fname)
    min_dir_size = root.get_size() - allowed_size

    sizes = sorted(root.get_recursive_sizes())
    for size in sizes:
        if size < min_dir_size:
            continue

        print(f'Size of smallest directory to delete: {size}')
        return

if __name__ == '__main__':
    if len(sys.argv) == 2:
        sum_max_size_dirs(sys.argv[1])
        find_min_dir_to_del_size(sys.argv[1])
    else:
        sum_max_size_dirs()
        find_min_dir_to_del_size()