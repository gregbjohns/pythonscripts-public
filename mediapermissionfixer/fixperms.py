#!/usr/bin/python3

import os
import pwd
import grp

def modify_permissions(path, username, groupname):
    """
    Recursively modifies file permissions and ownership under a given path.

    Args:
      path: The path to the directory to start from.
      username: The username of the new owner.
      groupname: The group name of the new group.
    """
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.chmod(dir_path, 0o555)  # Set directory permissions to 555
        for file in files:
            file_path = os.path.join(root, file)
            os.chmod(file_path, 0o444)  # Set file permissions to 444

            # Get the UID and GID for the specified user and group
            uid = pwd.getpwnam(username).pw_uid
            gid = grp.getgrnam(groupname).gr_gid
            os.chown(file_path, uid, gid)  # Set file ownership

if __name__ == "__main__":
    start_path = "."  # Start from the current directory
    username = "user"  # Replace with the desired username
    groupname = "users"  # Replace with the desired group name
    modify_permissions(start_path, username, groupname)
