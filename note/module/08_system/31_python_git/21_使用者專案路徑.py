import os

print(os.environ["USERPROFILE"])

print(os.path.join(os.environ["USERPROFILE"], "Documents"))