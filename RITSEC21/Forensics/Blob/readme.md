# Blob

![Bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/5.png?raw=true)

- Clone the Repository http://git.ritsec.club:7000/blob.git/
- From the challenge name we shall understand that this challenge is related to `blob`.
- Blob is an abbreviation for `Binary large object`.
- A `blob` in `Git` will contain the same exact data as a file.
- It's just that a blob is stored in the Git object database, and a file is stored on the filesystem. 
- A “blob” is used to store file data- it is generally a file.
- If we take a look at our .git directory we can see that the .git/objects directory has some subdirectories and files.
- So lets navigate to .`git/objects` directory.
- It contains a list of all files in our project with a pointer to the blob object assigned to them (this is how git associates your files with their blob objects).
- Notice that every directory name is two characters long. 
- Git generates a 40- character checksum `(SHA-1) hash` for every object and the first two characters of that checksum are used as the directory name and other 38 as a file (object) name.
- The first kind of object that git creates when we commit some files are blob objects.
-  Let's use the command `git cat-file` to show the contents of the hashed files in `.git/objects`.
-  `git cat-file` provides content or type and size information for repository objects.
-  The tree object contains one line per file or subdirectory, with each line giving file permissions, object type, object hash, and filename. 
-  An object type is usually one of `blob` for a file or `tree` for a subdirectory.
-  Now use `-p` to view the object contents.
-  In our case the third directory `d0` contains the flag. 

![Bi0s](https://github.com/a3X3k/Bi0s/blob/master/CTFs/RITSEC21/Assets/4.png?raw=true)

```
Flag --> RS{refs_can_b3_secret_too}
```
