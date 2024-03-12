MCB 185 Notes
====================

+ generally alphabetize. example: alphabetize nucleotides

+ nucleotides should be lowercase, generally all variable lowercase
+ amino acids can be uppercase letters

+ use ifs when events are independent 
+ use elifs when events are reliant on prior if statements

+ Write problems/ issues out first, then do the work
+ Weed out problems/ potential errors (like when you want positives or things)
  then you can solve 
  
+ expand everything out, variable for everything
  makes it easier to debug things
  
# Keyboard Shortcuts
+ Ctrl + A: puts you at beginning of line
+ Ctrl + X: Cuts

**test functions with small check-able values, then expand range once it works**

**use """ not ''' to comment stuff out**

**write a line, then run it; test and retest each line before adding new things**
**Debug each line before writing new lines**

# While loop
while < condition is True/False >
	output/ function here
	
# Style Checker
**python3 ~/Code/MCB185/src/stylint.py <yourfile.py>**

# Printing Codes
\n = vertical spacing 
\t = tab, lines up text

# Compound Assignment Variables
+= means increments (ex: a +=1, a increasing in increments of 1)
-= means decrement (ex: a -= 1, a decreasing by increments of 1)
*= means multiply and assign 
	
# Markdown 
+ Use spaces not tabs in markdown 

# Modifying Lists
+ <list>.append()
  allows you to add elements to end of a list 
+ <list>.pop()
  removes things from the end of a list
+ <list>.sort
  sorts the list 
  *invert sort by using (reverse = True)*
+ <list>.split()
  splits lists into strings
+ '<delimiter>'.join(<list>)
   turns list into string by joining list items by whatever delimiter 
   (ex: '' joins by nothing, ',' would join by commas)

# Opening Files
```
with open(path) as fp:
    for line in fp:
        do_something_with(line)
```
for a zipped file
```
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')
```
#puts terminal values from terminal into list
for x in sys.argv[1:]:  
	val.append(int(x))

# Sliding Window Algorithm
```{python}
w = 10 #sets the size of window
s = 1 #sets step size
for i range(0, len(seq) - w +1, s): #moves window along
	subseq = seq[i: i + w]
```

#Permissions
+ read (4)
+ write (2)
+ execute (1)
**Many different ways to assign this**

0
1
2
3
4: R
5: RX
6: RW (ReadMe, Python)
7: RWX

Ex: 644 = author can read and write, everyone else can only read (user/group/public)

<chmod> allows you to change permissions 



	
