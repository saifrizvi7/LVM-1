import subprocess

def execute(command):
    com = command.split()
    out = subprocess.run(com,capture_output=True,text=True)
    if "create" in com:
        return out.returncode
    else:
        return out.stdout

