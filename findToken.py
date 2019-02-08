# To find the number of valid and invalid tokens in the C or C++ program
# Author : - Nidhi Mantri
#Student ID : - 2016KUCP1014
#Date : - 8/02/19

import re   # for regular expressions
from collections import Counter # for counting the frequency of each token
from prettytable import PrettyTable # for creating tables 

# total keywords( C and C++)
Keywords = ['auto', 'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel',\
                       'atomic_commit', 'atomic_noexcept', 'bitand', 'bitor', 'bool', 'break',\
                       'case', 'char', 'char16_t', 'char32_t', 'class', 'compl', 'concept', 'const',\
                       'constexpr', 'const_cast', 'continue', 'co_await', 'co_return', 'co_yield', \
                       'decltype', 'default', 'delete',  'do', 'double', 'dynamic_cast', 'else', \
                       'enum', 'explicit', 'export', 'extern', 'false', 'float', 'for', 'friend' 'goto', 'if', \
                      'import', 'inline', 'int', 'long', 'module', 'mutable', 'namespace', 'new', 'noexcept',\
                      'not', 'not_eq', 'nullptr', 'operator', 'or', 'or_eq', 'private', 'protected', 'public',\
                      'register', 'reinterpret_cast', 'requires', 'return', 'short', 'signed', 'sizeof', 'static', \
                      'static_assert', 'static_cast', 'struct', 'switch', 'synchronized', 'template', 'this',\
                      'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned',\
                      'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor', 'xor_eq']

# Operator symbols
Operators = ['+', '-', '*', '/', '%', '++' ,'--', '<', '<=', '>', '>=', '==', '!=', '::', \
                      '&&', '||', '!', '&', '|', '<<', '>>', '~', '^', '=', '+=', '-=', '*=', '/=', '%=', '?', ':']

# Punctuator symbols
Punctuators = [',', ';', '(', ')', '{', '}', '.']

# Spaces
Spaces = "[ \n\t]+"

# regex for digits
Digits = "[-+]?[0-9]*\.[0-9]+|[0-9]+"

# regex for identifiers
Identifiers = "[_a-zA-Z][a-zA-Z0-9_]*"

# preprocessor symbol
Preprocessor = ['#']

#used to perform lexical analysis on the code
#code is in the form of list ...
# outPut is the name of output file
def LexicalAnalyzer(List, outPut):
    keyWs = []      # used to store keywords
    idenFs = []      # used to store identifiers
    digits = []         # used to store digits
    operTs = []      # used to store operators
    puncTs = []     # used to store punctuation marks
    symbolTable = []    # used to store identifiers
    notValid = []       # used to store invalid identifier
    Tokens = []     # used to store all the tokens 
    prePs = []      # used to store preprocessor
    i = 0   # used as a index
    while i < len(List):
        # if the word is a keyword
        if List[i] in Keywords:
            keyWs.append((List[i], Keywords.index(List[i])))
            Tokens.append((List[i], 'Keyword', Keywords.index(List[i])))
        # if the word is a operator
        elif List[i] in Operators:
            operTs.append((List[i], Operators.index(List[i])))
            Tokens.append((List[i],'Operator', Operators.index(List[i])))
        # if the symbol is a '#'
        elif List[i] in Preprocessor:
            prePs.append(List[i])
            Tokens.append((List[i], 'Preprocessor', '0'))
        # if the symbol is a punctuator
        elif List[i] in Punctuators:
            puncTs.append((List[i], Punctuators.index(List[i])))
            Tokens.append((List[i],'Punctuator', Punctuators.index(List[i])))
        # if the word is an identifier
        elif re.findall(Identifiers, List[i]) and List[i] == re.findall(Identifiers, List[i])[0]:
            # if it is a class
            if i > 1 and List[i-1] == 'class':
                q = (List[i], 'Class')
                if q not in symbolTable :
                    symbolTable.append(q)
            # if it is a function
            elif i < len(List)-3 and List[i+1] == '(' :# and List[i+2] == ')':
                q = (List[i], 'Function')
                if q not in symbolTable :
                    symbolTable.append(q)
            # if it is a message
            elif List[i] == 'quote':
                q = (List[i], 'Message')
                if q not in symbolTable :
                    symbolTable.append(q)
            # if it is an identifier
            else:
                q = (List[i], 'Identifier')
                if q not in symbolTable :
                    symbolTable.append(q)
            idenFs.append(q[0])
            Tokens.append((q[0],q[1], symbolTable.index(q)))
        # if word is a digit
        elif re.findall(Digits, List[i]) and List[i] == re.findall(Digits, List[i])[0]: 
            digits.append(List[i])
            Tokens.append((List[i], 'Constant'))
        # if it is not a valid identifier
        else:
            notValid.append(List[i])
        i += 1
    #print symbolTable
        
    # for the frequencies of the elements of respective lists
    keyWs = Counter(keyWs).most_common()
    operTs = Counter(operTs).most_common()
    puncTs = Counter(puncTs).most_common()
    
    # Creating table for Keywords present in the code
    if keyWs :
        #creating table
        keywrdTable = PrettyTable()
        keywrdTable.field_names = ["kW", "[i]", "Freq"]
        for i in range(len(keyWs)):
            keywrdTable.add_row([keyWs[i][0][0], keyWs[i][0][1], keyWs[i][1]])
    outPut.write("Keyword Table for the given code is :- \n")
    outPut.write("%s\n" % keywrdTable)

    # Creating table for Operators present in the code
    if operTs :
        operTsTable = PrettyTable()
        operTsTable.field_names = ["O", "[i]", "Freq"]
        for i in range(len(operTs)):
            operTsTable.add_row([operTs[i][0][0], operTs[i][0][1], operTs[i][1]])
    outPut.write("\nOperator Table for the given code is :- \n")
    outPut.write("%s\n" % operTsTable)

    # Creating table for Punctuators present in the code
    if puncTs :
        puncTsTable = PrettyTable()
        puncTsTable.field_names = ["P", "[i]", "Freq"]
        for i in range(len(puncTs)):
            puncTsTable.add_row([puncTs[i][0][0], puncTs[i][0][1], puncTs[i][1]])
    outPut.write("\nPunctuator Table for the given code is :- \n")
    outPut.write("%s\n" % puncTsTable)

    #calculating total number of valid and invalid tokens
    TotalTokens = len(Tokens)
    TotalInvalid = len(notValid)
    # calculating frequencies of valid and invalid tokens
    Tokens = Counter(Tokens).most_common()
    notValid = Counter(notValid).most_common()
    return symbolTable, TotalTokens, Tokens, TotalInvalid, notValid, outPut

# to form list of code ...
def GeneratingList(code):
    lexeme_ptr = 0  
    read_ptr = 0
    listy = []    # to store code fragments
    #print code
    oPP = Operators + Punctuators + Preprocessor
    while read_ptr < len(code):
        # if operator is of two symbols, ex -> '++', '>=', '/=', etc
        if code[read_ptr] in Operators and code[read_ptr+1] in Operators:
            read_ptr += 2
        else:
            # incrementing the read_ptr while there is no whitespace
            #or not any operator, punctuation mark or preprocessor symbol
            while code[read_ptr] != ' ' and code[read_ptr] not in oPP :
                read_ptr += 1
        # if it is any symbol of oPP(ex : - '}'), then add in list
        if read_ptr == len(code) - 1 and code[read_ptr] in oPP:
            listy.append(code[read_ptr])
        # reading the string
        sub_str = code[lexeme_ptr : read_ptr]
        # if not null then add in the list
        if sub_str:
            listy.append(sub_str)
        # if it is a whitespace, then increment lexeme_ptr by 1 and read_ptr also
        if code[read_ptr] == ' ':
            lexeme_ptr = read_ptr + 1
            read_ptr += 1
        else:
            lexeme_ptr = read_ptr
            read_ptr += 1
            if read_ptr < len(code) and code[lexeme_ptr] in oPP:
                # if operator is of length '2', 
                if code[lexeme_ptr] in Operators and code[read_ptr] in Operators:
                    # decrement so as to scan the full operator
                    read_ptr -= 1
                elif code[read_ptr] != ' ' :
                    #print code[lexeme_ptr]
                    sub_str = code[lexeme_ptr : read_ptr]
                    listy.append(sub_str)
                    lexeme_ptr += 1
    # return the list of the given code
    if read_ptr >= len(code):
        #print listy
        return listy        

# main function of program
def main():
    with open("Input.cpp", "r") as inputFile:
        code = inputFile.read()
        # to replace all the text in double quotes by the word "quote"
        code = re.sub('"(.*?)"', 'quote', code)
        # to replace single line comment by null string
        code = re.sub('//.*\n', '', code)
        # to replace multiline comments by null string
        code = re.sub('\/\*.*?\*\/', '', code, re.DOTALL)
        # ignoring the header file inclusions
        code = re.sub('#.*?<.*?>', '', code)
        # to replace '\n', '\t', ' ', by a single white space
        code = re.sub(Spaces, ' ', code)
    #print code
    outPut = open("Output.txt", 'w')  # to write output in the text file
    # calling first function to generate list of code
    List = GeneratingList(code)
    # to obtain symbol table, tokens, total number of tokens and invalid strings and output file from lexical analysis phase
    symbolTable, TotalTokens, Tokens, TotalInvalid, notValid, outPut = LexicalAnalyzer(List, outPut)
    # printing symbolTable
    outPut.write("\nSymbol Table for the given code is : -\n") # %s\n" % str(symbolTable))
    # creating table output for symbol table
    SymTable = PrettyTable()
    SymTable.field_names = ["[i]", "String", "Type"]
    for index, value in enumerate(symbolTable):
        SymTable.add_row([index, symbolTable[index][0], symbolTable[index][1]])
    outPut.write("%s\n" % SymTable)
    # printing total number of tokens
    outPut.write("\nTotal Valid Tokens in the given code are : - %s\n"% str(TotalTokens))
    # creating table for tokens
    TokenTable = PrettyTable()
    TokenTable.field_names = ["Token", "Type", "[i]", "Freq"]
    # printing all the tokens
    for i in range(len(Tokens)):
        #print Tokens[i]
        if len(Tokens[i][0])  == 3:
            TokenTable.add_row([Tokens[i][0][0], Tokens[i][0][1], Tokens[i][0][2], Tokens[i][1]])
        else: # if any constant entry in the table ( index is null for that entry )
            TokenTable.add_row([Tokens[i][0][0], Tokens[i][0][1], '-', Tokens[i][1]])
    outPut.write("%s\n" % TokenTable)
    #print TokenTable
    if notValid:
        InvalidTable = PrettyTable()
        InvalidTable.field_names = ["Token", "Freq"]
        # printing total number of invalid tokens
        outPut.write("\nTotal Invalid Tokens are : - %s\n" %str(TotalInvalid))
        for i in range(len(notValid)):
            #printing all the invalid strings
            #outPut.write("%s\n"% str(notValid[i]))
            InvalidTable.add_row([notValid[i][0], notValid[i][1]])
        outPut.write("%s\n" % InvalidTable) 
    else:
        # if no invalid string is there
        outPut.write("\nNo invalid Tokens in the Given Code\n")
    
# calling the main function
if __name__ == "__main__":
    main()
