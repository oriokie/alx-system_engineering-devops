0x01. Shell, permissions


0-iam_betty: The script changes the user ID to betty.

1-who_am_i: The script prints the effective userid of the current user.
2. Groups

2-groups: The script prints all the groups the current user is a part of.
3. New owner

3-new_owner: The script changes the owner of the file hello to the user betty.
4. Empty!

4-empty: The script creates an empty file called hello.
5. Execute

5-execute: The script adds execute permissions to the owner of the file hello.
6. Multiple permissions

6-multiple_permissions: The script adds execute permission to the owner and the group owner, and read permission to other users, for the file hello.
7. Everybody!

7-everybody: The script adds execution permission to the owner, the group owner and the other users, for the file hello.
8. James Bond

8-James_Bond: The script sets the permission for the file hello as follows:
Owner - no permission at all
Group - no permission at all
Other users - all permissoins
9. John Doe

9-John_Doe: The script sets the mode of the file hello to -rwxr-x-wx.
10. Look in the mirror

10-mirror_permissions: The script sets the mode of the file hello the same as the file olleh.
11. Directories

11-directories_permissions: The script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files are not changed.
12. More directories

12-directory_permissions: The script creates a directory my_dir with permissions 751 in the working directory.
13. Change group

13-change_group: The script changes the group owner to school for the file hello.
100. Owner and group

100-change_owner_and_group: The script changes the owner to staff and the group owner to vincent for all the files and directories in the working directory.
101. Symbolic links

101-symbolic_link_permissions: The script changes the owner and the group owner of the file satff_hello to betty and vincent, respectively.
102. If only

102-if_only: The script changes the owner of the file hello to betty only if it is owned by the user guillaume.
103. Star Wars

103-Star_Wars: The script plays Star Wars Episode IV in the terminal.
