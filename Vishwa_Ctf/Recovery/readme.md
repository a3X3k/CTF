# Recovery

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/17.png?raw=true)

- `Download` the `files` given.
- Using `registry viewer` `analyse` the file2.
- Go through the `accounts` folder.

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/21.png?raw=true)

- Under `users` we can see `shreyas account` details but we will not able see the `password hash` without uploading the `syskey` file.

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/20.png?raw=true)

- The `file1` is the `syskey` for the `file2` after uploading the `syskey` in `registry viewer` we will able to see the the `hash key` and more details in `key properties`.
- So using `samdump2` dump all the `username` and `password` `hash`.

```
samdump2 file1 file2 > hashes.txt
```

![](https://github.com/a3x3k/Bi0s/blob/master/CTFs/Vishwa_Ctf/Assets/23.png?raw=true)

- Created a wordlist using python script `cupp.py` with hints given in description 

`The DOB is 10 January 1993 because at the time he changed the password he is 20 yrs old.`

- Using this `python script` if we input the `name,DOB` etc we shall get all possible combinations of `password`.

```
john --wordlist=shreyas.txt --format=NT hashes.txt
```

- Password = `sayerhs_093`

```sh
Flag --> vishwaCTF{sayerhs_093}
```
