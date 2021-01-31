# Useful scripts

```
$ python3 gameChanger.py -h

USAGE
	./mytool file newfile
DESCRIPTION	
	file	file to copy containing the games
	newfile	name of the new file
	nb	number of lines you want to copy to the new file

```

```
$ python3 gameCutter.py -h

USAGE
	./mytool file newfile start end
DESCRIPTION	
	file	file to copy containing the games
	newfile	name of the new file
	start	the start line of the copy
	end	the end line of the copy

```

To merge games you can simply use the command line:
```
cat file1.txt file2.txt > file3.txt
```