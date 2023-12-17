# Path Traversal

* Try the Intruder default wordlist to fuzz. It tests url encoding and double url encoding.
* Try adding the expected filetype .type, preceded by null-byte, \n, etc.
* If the path is absolute, the backend can verify that the static section of the path is correct. Try to insert the payload after the fixed section (Example: /var/www/resource/img.png -> /var/www/resource/../../../etc/passwd)
