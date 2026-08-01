import subprocess

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "asd"])
subprocess.run(["git", "push", "-u", "origin", "main"])
input("a")