#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "henols"

import os
import argparse
from pathlib import Path
import shutil
from datetime import datetime

class FileTreeMaker(object):

    def collect(self, parent_path, file_list, name, date, level):
        file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
        for sub_path in enumerate(file_list):

            full_path = os.path.join(parent_path, sub_path)
            
            if os.path.isdir(full_path):
                if name == None:
                    name = sub_path
                elif date == None:
                    date = sub_path
                self.collect(full_path, os.listdir(full_path), name, date, level + 1)
                if level == 1:
                    myDate = datetime.now()
                    date_obj = datetime.strptime(date, '%Y%m%d')
                    if( date_obj.date() < myDate.date()) :
                        print("delete path:" , full_path)
                        shutil.rmtree(full_path)
                    date = None
                elif level == 0:
                    name = None
            elif os.path.isfile(full_path):
                self.move(name, date, sub_path, full_path)

    def move(self, device_name, date, file_name, src_path):
        to_file_name = "%s-%s-%s%s" % (date, file_name[8:14], device_name, Path(src_path).suffix)
        to_path = os.path.join(self.dest_dir, date)
        
        if not os.path.exists(to_path):
            os.makedirs(to_path)
            print("Directory " , to_path , " Created ")

        print("moving" , to_file_name , "to", to_path)
        shutil.move(src_path, os.path.join(to_path, to_file_name))
        #shutil.copy(src_path, os.path.join(to_path, to_file_name))

    def make(self, args):
        self.root = args.root
        self.dest_dir = args.dest_dir

        print("root:" , self.root)
        print("dest_dir:" , self.dest_dir)
        self.collect(self.root, os.listdir(self.root), None, None, 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root", help="root of file tree", default=".")
    parser.add_argument("-o", "--dest_dir", help="dest dir", default="./tmp/")
    args = parser.parse_args()
    FileTreeMaker().make(args)
