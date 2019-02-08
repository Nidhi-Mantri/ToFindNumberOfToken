Requirements :
1. Python2.7
2. Libraries : - re, prettytable, collections
3. It consists of 2 functions 
	a. GeneratingList(code)
	b. LexicalAnalyzer(listy, output_file)
#Here, code is the preprocessed code in which all the comments header files are ignored.
#All the tab spaces, newline spaces and multiple spaces are removed.
#The quoted string is replaced by the word 'quote'.

Input file is a C or C++ file.
Output file consists of multiple tables : -
1. Keyword Table : - it consists of all the keywords present in the code with its frequency and index of the actual Keyword List.
2. Operator Table : - consists of operators present in the code with frequency and index of the corresponding operator in the Operators List.
3. Punctuator Table : - consists of punctuators present in the code with frequency and index of the corresponding punctuator in the Punctuators List.
4. Symbol Table : - consists of identifiers[functions and classes are specifically identified]
5. Token Table : - consists of all the valid tokens with their index, frequency, type.
6. Invalid token table : - if invalid tokens exist, then it will store the string with its frequency.