# jsonDiff

jsonDiff is a python command line tool for comparing two json structures. The tool will only function when given two json files. The format of the command will be:
```sh
$ python3 jsonDiff.py file1.json file2.json
```

If the program is not given two json files it will terminate. If the program is given two files with json file extensions, but not written in proper json structures, it will also terminate.

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
This command will only work when one is located in the directory of the executable. This means that files will have to have an absolute or relative path provided to run this program. However, one could simply export their directory path to run this program from any directory in your system. This can be done using something like:
```sh
$ export PATH=$PATH":$PWD"
```
This command can be called from the directory where the executable is located. Otherwise, $PWD should be replaced with the path of the executable.

# Logic behind the program
As mentioned before, the program uses the Jaccard coefficient to rate similarity. Since all the Jaccard method does is compare unions and intersections, what actually ends up mattering is how the JSON structures are converted to sets. I spent a lot of time considering what mattered when comparing two JSON structures. Two separate JSON structures could have the same objects stored in two differently named arrays. Does this mean that they differ only by the name of the arrays or the entirity of the arrays? I found this to be the most important question, because it could drastically change the way two files compare to each other. Another comparison I considered was two objects with the same key and two separate values. I believed these should be considered seperate since they contained different values. Finally, I also wondered if two objects should be presented with resemblance values. For example, if two JSON structures contained two objects with the same key and a value that slightly differed, should they count as being same, similar, or different. After asking these questions, I designed a program that doesn't weigh values on depth and only considers two objects to be the same or different. To do so, I iterate through a JSON struct adding each object to a set. If the program comes across an array, the array object gets added as "array_name: []", and all the elements inside get added by object. By doing so, each object and array will be added with the same weight. This seemed fairer than considering two identical arrays with different names to be fully seperate. The program does this for both JSON structs and then compares the resulting sets.

I will begin by stating that this method isn't perfect. A set only stores unique elements, so two identical objects in a single JSON structure will only be added once. Because of this, the similarity score of two JSON structures can be inflated. I did attempt another method of building sets where each object in an array gets added with name of the array. This resulted in something like "array_name: object_key: object_value". However, for this to be fully successful it would have to weigh the difference between two objects stored in an array; which would also require a method for knowing which two objects correlate with each other. Because of the running time complexity this addition would introduce, I found it easier to consider each object with the same weight. Overall, this program can identify if two JSON structures have no similarity or are considered to be identical. As mentioned in the "Programming Excerise", there is no perfect way to do this; however, I believe that this a fast way to get an initial idea of similarity.
