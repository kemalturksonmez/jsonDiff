all:
	cp jsonDiff.py jsonDiff
	chmod u+x jsonDiff
	export PATH=$PATH":$PWD"