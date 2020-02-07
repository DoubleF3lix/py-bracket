# py-bracket
Adds curly bracket support to Python for use with Visual Studio Code


To use, simply download the `convert.py` files and the `.vscode` folder and drop them into your workspace folder. Then use CTRL + SHIFT + B and your file will be run. It will convert the py-bracket script into a valid python file, run it, then delete it.
EX: `my_file.pyb` => `my_file.py`


The syntax is incredibly simple:
```
var = 2
if var == 2 {
    var = 3
    
    if var == 3:
        var += 1
}

while var < 5 {
    print(var)
    var += 1
}
```
=>
```
var = 2
if var == 2:
    var = 3
    
    if var == 3:
        var += 1
     
while var < 5:
    print(var)
    var += 1
```
