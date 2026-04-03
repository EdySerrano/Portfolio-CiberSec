# File permissions in Linux

## Project description

I used Linux command-line tools to manage file and directory permissions within a secure environment. The goal was to examine current permissions, interpret the permissions string, and modify access rights using the `chmod` command. This ensures that sensitive files are protected and that the principle of least privilege is applied to system users.

## Check file and directory details

To inspect the current permissions of files and directories, I used the list command with the long format option: `ls -l` This command outputs a detailed list where the first column represents the permissions string (e.g., `-rwxr-xr--`). It allows me to verify who is the owner, which group the file belongs to, and what access rights (Read, Write, Execute) are assigned to the User, Group, and Others.

## Describe the permissions string

The permissions string is a 10-character code at the start of the `ls -l` output.

* **1st Character:** Indicates the file type (`-` for a regular file, `d` for a directory).  
* **Next 3 Characters (User):** Permissions for the file owner.  
* **Middle 3 Characters (Group):** Permissions for the group assigned to the file.  
* **Last 3 Characters (Others):** Permissions for anyone else.  
* **r, w, x:** These stand for **R**ead, **W**rite, and e**X**ecute. If a hyphen `-` is present, that permission is denied.

## Change file permissions

I modified file permissions to restrict unauthorized access using the `chmod` command.

* **Example:** To remove write permissions for "others" to prevent them from modifying a specific file, I used the command: `chmod o-w project_file.txt`  
* **Example:** To verify the change, I ran `ls -l` again to confirm the write flag (`w`) was removed from the "others" section of the string.

## Change file permissions on a hidden file

Hidden files in Linux differ because they start with a period (e.g., `.hidden_data`).

1. First, I viewed the hidden files using `ls -la` (the `-a` flag shows all files, including hidden ones).  
2. Then, I changed the permissions to ensure only the user has read and write access, removing all permissions for group and others: `chmod u=rw,go-rwx .project_x.txt` *.*

## Change directory permissions

Directory permissions function slightly differently than files. The "execute" (`x`) permission on a directory is required to enter it (using `cd`).

* I ensured that the project directory allowed the group to read and enter, but not write (create or delete files): `chmod g+rx,g-w /home/analyst/projects` This ensures collaboration is possible without risking the deletion of the directory structure by group members.

## Summary

Through this activity, I demonstrated the ability to secure a Linux environment by managing permissions. I learned how to inspect attributes with `ls -l` and `ls -la`, decode the 10-character permission string, and enforce access control using `chmod`. Mastering these commands is essential for maintaining the confidentiality and integrity of data in any operating system.  
