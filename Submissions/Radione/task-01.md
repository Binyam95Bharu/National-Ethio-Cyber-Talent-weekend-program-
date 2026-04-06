## Task #1
 Q1: First we need to know which numbers corrispond to which permision
 | Permissions   | Octal(numeric)   | Letters(Symbolic)   |
 | :-----------: | :-----: | :-------: |
 | no permission |    0    |   ---     |
 | Execute       |    1    |   --x     |
 | Write         |    2    |   -w-     | 
 | Write+Execute |    3    |   -wx     |
 | Read          |    4    |   r--     |
 | Read+Execute  |    5    |   r-x     | 
 | Read+Write    |    6    |   rw-     | 
 | Read+Write+Execute|    7    |   rwx     |
 
 then from this we can `sudo chmod 640 file` 
 
 Q2: `sudo chmod 755 file`

 Q3: `sudo chmod 664`

 Q4: `640`

 Q5: the file can't be accesable anymore, has the permissions has been locked even for the root, so no he can't cat it but the root can still change the file's permissions to enable read,write,and exec again

 Q6: `touch Audit.txt && sudo chmod 750`

 Q7: As shown above in the table, `741` = `rwxr----x`

 Q8: `500` = `r-x`

 Q9: `r-xrw-r--` = `564`
