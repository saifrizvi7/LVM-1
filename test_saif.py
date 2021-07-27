import unittest
import cli
from runner import execute
import subprocess

class Task(unittest.TestCase):
    disk = " ".join(cli.disk_name)
    
    #test physical volume created or not
    def test_pvcreate(self):
        execute("pvcreate {}".format(Task.disk))
        self.output = execute("pvdisplay" ) 
        for i in cli.disk_name:
            self.assertRegex(self.output,i, "{} is not present" .format(i))


    def test_vgcreate(self):
        execute("pvcreate {}" .format(Task.disk))
        execute("vgcreate {} {}".format(cli.vgname,Task.disk))
        self.output = execute("vgdisplay" )
        self.assertRegex(self.output,cli.vgname)


    #test volume group created or not
    def test_xlvcreate(self):
        execute("pvcreate {}" .format(Task.disk))
        execute("vgcreate {} {}" .format(cli.vgname, Task.disk))
        execute("lvcreate --size {} --name {} {}".format(cli.size,cli.lvname,cli.vgname))
        self.output = execute("lvdisplay")
        self.assertRegex(self.output,cli.lvname)

    def tearDown(self):
    
        disk = " ".join(cli.disk_name)
        if(cli.cmd == "pvcreate"):
            execute("pvremove {}".format(disk))

      
        if(cli.cmd == "vgcreate"):
            execute("vgremove {}".format(cli.vgname))
            execute("pvremove {}" .format(disk))

       
        if(cli.cmd == 'lvcreate'):
            s =  "lvremove {}" .format(cli.vgname)
            subprocess.run(s.split(" "))
            execute("vgremove {}".format(cli.vgname))
            execute("pvremove {}" .format(disk))

