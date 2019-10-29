import os
import sys
pwd = os.getcwd()
if len(sys.argv) == 2:
	mssg = sys.argv[1]
	os.system(f"cd {pwd} && git add . && git commit -m {mssg}")
elif len(sys.argv) == 3:
	mssg = sys.argv[1];os.system(f"cd {pwd} && git add . && git commit -m {mssg} && git push")
else:
    os.system(f"cd {pwd} && git add . && git commit -m auto-commit")
