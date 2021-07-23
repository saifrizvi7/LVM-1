import argparse
import unittest
from unittest.suite import TestSuite
from runner import execute
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--test", help = "command to execute", choices=['pvcreate','vgcreate','lvcreate'])

parser.add_argument("--disk",nargs='+', help = "disk name")
parser.add_argument('--lvname', help="name of the logical volume")
parser.add_argument('--size', help="size of the lv")
parser.add_argument('--vgname', help="volume group name to allocate lv")
args = parser.parse_args()

cmd = args.test
disk_name = args.disk
lvname = args.lvname
size = args.size
vgname = args.vgname


if __name__ == '__main__':
    import test_file
    suite = TestSuite()
    loader = unittest.TestLoader()
    if cmd == 'pvcreate':
        suite.addTests(loader.loadTestsFromName("test_file.Task.test_pvcreate"))
    if cmd == 'vgcreate':
        suite.addTests(loader.loadTestsFromName("test_file.Task.test_vgcreate"))
    if cmd == 'lvcreate':
        suite.addTests(loader.loadTestsFromName("test_file.Task.test_xlvcreate"))


    runner = unittest.TextTestRunner()
    runner.run(suite)


