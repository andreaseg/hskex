# Python script to embed external code into markdown files

The script will look for markdown files in its own folder and attempt to replace linked code with markdown code-blocks. The generated files will be placed in the target folder. The syntax for linked code is given by

```
[code][<language>](<path>)
```
where _language_ decides the syntax highlighting and _path_ is the path of the code to be included.