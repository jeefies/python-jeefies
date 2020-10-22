# Jeefies
**Author : Jeef**  
**Email : jeefy163@163.com**  
***
This is a easy package.  
Every one can use it for somethong in it.  
There are some thing for flask, secret some sentence, and so on.

- - -
How to install
--------------
**The only way** is to use pip to download  
But first, make sure you've downloaded python 3.x and pip can use.  
___Advice___: *Do not use the version that earlier than 3.5.*  
Then use
`pip install jeefies`
To install the package.  
You can see [pypi](https://pypi.org/project/jeefies) for more install infomation.


- - -
## Encrypt  
There are two kind of encrypt object: Hashsec, Hexsec.They all depends on BaseSec.
### Basesec
1. File  
    * fromFile  
    > Give a filename or an opened file.  
    > If the filename is not on the work place, the function would search for it's child diretories until find the matched file.
    * toFile
    > Give the either lines or the infile(filename or the opened file) argiment in.  
    > Then the function would read and write them into the outfile(filename or he opened file).  
    > __Do not__ give both of the lines and the infile argiment or only the infile will be used.  
    * more
    > Use `help(object)` to learn more details.

### Hexsec
This is a easy encrypt object, but it's kind of useful because the encrypted sentence only has *numbers and '!'*.  
But it's really easy that people can read it by them self if the know how does it work.

### Hashsec
**Not really hash**  
Hash there is just a kind of joke.  
The encrypt result is like an hash value, but not every where can use it because almost all the letter whether common or uncommon it may use, so use it just when you just for passowrd.
#### Not callable
I don't want it to be so complex, so I made it **Uncallable**  
Do not use
```
from jeefies import Hashsec
sec = Hashsec('password')
```
> If you want a formal encrypted sentence,  
>you can choose to use `Hexsec.encrypt(Hashsec.encrypt(sentence))`.

- - -
## Rand
The package is a easy package to have make some random numbers.  
Type `from jeefies import rand` to import it to use.  
The objects are kind of easy, so You can use  
`help(object)` to see more details of the functions.  
> It is based on the random module.

- - -
## Content
This object is to manage some infomation.
It's easy to use but need to give the data directory or it might be wrong to read the datas.
Also, you can use ***help(object)*** for more infomation

___Now with the new version based on Hylang Lisp___  
You can get the same cache for different process while using.  
However, `Content` for no cache but `content` for cached.  

- - -
## Flask_self
**Do not use it** if you don't understand how does it work.
This is just a package for my self to use.  
Still, you can use `help(object)` for more details.  
> It's a module to use without flask-login and flask-sqalchemy.  
> Also, it has some convnient object.  
> Some were moved into self.

## Self
**Never use it** unless you understand all of the function.  
Just a convenient package, not too important.  

- - -
# Thanks
| **Family**   | **Friends**   | **Teachers** |
| :----------: | :-----------: | :----------: |
| Fu Judong    | Xue Shihan    | Zhang Maoping|
| Lu Mingchun  | Zhang LiangYu | Hu Lubiao    |
| Fu Yongchuan | Zhang Zhenxin | All Books    |