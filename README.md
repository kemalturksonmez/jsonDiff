# jsonDiff

jsonDiff is a python command line tool for comparing two json structures. The tool will only function when given two json files. The format of the command will be:
```sh
$ python3 jsonDiff.py file1.json file2.json
```

If the program is not given two json files it will terminate. If the program is given two files with json extensions, but not written in proper json structures, it will also terminate.

The similarity scoring system used is the Jaccard Coefficient method. This method compares the intersection between two files with their union. Becaues of this, it is always guranteed to provide a score between 0 and 1.

# Setting it up as a command line tool
When pulled from the repository, the user will be presented with the program jsonDiff.py, a Makefile, and a README.md. Running the makefile on a UNIX system will convert the program to an executable. To run the Makefile, the user should call:
```sh
$ make
```

After running make, the program can be run using the command below:
```sh
$ jsonDiff file1.json file2.json
```
This command will only work when one is located in the directory of the executable. This means that files will have to have their paths, absolute or relative, provided to functionally run this program. However, one could simply export their directory path to run this program from any directory in your system. This can be done using something like:
```sh
$ export PATH=$PATH":$PWD"
```
This command can be called from the directory where the executable is located. Otherwise, PWD should be replaced with the path of the executable.

# Logic behind the program
As mentioned before, the program uses the Jaccard coefficient to rate similarity. Since all the Jaccard method does is compare unions and intersections, what actually ends up mattering is how the JSON structures are converted to sets. I spent a lot of time considering what mattered when comparing two JSON structures. Two separate JSON structures could have the same objects stored in two differently names arrays. Does this mean that they differ only by the name of an arrays or the entirity of the arrays? I found this to be the most important question, because it could drastically change the way two files compare to each other. Another comparison I considered was two objects with separate values. I believed these should be considered seperate since they contained different values. Finally, I also wondered if two objects should be presented with resemblance values. For example, if two JSON structures contained two objects with the same key and a value that slightly differed, should they count as being same, similar, or different. After asking these question, I designed a program doesn't weigh values on depth and only considers two objects to be the same or different. To do so, I parse through a JSON struct adding each object to a set. If the program comes across an array, the array gets added as "array_name: []". By doing so, each object and array will be added with the same weight. This seemed fairer than considering two identical arrays that were named differently to be seperate. 
