# Ex C.1.1: 9 - 3 --> 6
# Ex C.1.2: 8 * 2.5 --> 20.0
# Ex C.1.3: 9 / 2 --> 4
# Ex C.1.4: 9 / -2 --> -5
# Ex C.1.5: 9 % 2 --> 1
# Ex C.1.6: 9 % -2 --> -1
# Ex C.1.7: -9 % 2 --> 1
# Ex C.1.8: 9 / -2.0 --> -4.5
# Ex C.1.9: 4 + 3 * 5 --> 19
# Ex C.1.10: (4 + 3) * 5 --> 35

# Ex C.2.1: x = 100
# Ex C.2.2: x = x + 10 --> x = 110
# Ex C.2.3: x += 20 --> x = 130
# Ex C.2.4: x = x - 40 --> x = 90
# Ex C.2.5: x -= 50 --> x = 40
# Ex C.2.6: x *= 3 --> x = 120
# Ex C.2.7: x /= 5 --> x = 24
# Ex C.2.8: x %= 3 --> x = 0

# Ex C.3: First, Python will evaluate the right expression (x-x) before 
# looking at the operator. After Python evaluates (x - x) which is 0, it will
# evalute the '+=' operator which takes the current value of x and adds the
# value fo the right expression (0) to it. Hence, the value of x remains 
# unchanged. So if x has an initial value of 3, it will have a final value
# of 3 a well. 

# Ex C.4.1: 1j + 2.4j --> 3.4j
# Ex C.4.2: 4j * 4j --> -16 + 0j
# Ex C.4.3: (1+2j) / (3+4j) --> 0.44 + 0.08j

# Ex C.4.1: (1+2j) * (1+2j) --> -3 + 4j
# Ex C.4.2: 1+2j * 1+2j --> 1 + 4j
# The above answers are different because Python treats complex numbers with
# the same order of operations they do with regular numbers. In the first
# example, the parenthesis distribute the two complex numbers as if they are
# binomials. In the second example, Python does multiplication before addition
# so we get 1 + 2j + 2j = 1 + 4j. 

# Ex C.5.1: cmath.sin (-1.0 + 2.0j) --> (-3.165778513216168+1.959601041421606j)
# Ex C.5.2: cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# Ex C.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# The first option is better because in the case of import math *, you are
# importing everything from the math module which can cause variable confusion 
# (for example if you had a variable named pi) and name clash where some
# functions become unusable because they share their name with another function. 
# Therefore, 'import math' avoids the possible variable confusion because 
# you would have to write the 'module.function' to reference a function which is
# very specific and thus avoids name clash and variable confusion.

# Ex C.6.1: "foo" + 'bar' --> 'foobar'
# Ex C.6.2: "foo" 'bar' --> 'foobar'
# Ex C.6.3: a = 'foo'
#           b = "bar"
#           a + b
#           --> 'foobar'
# Ex C.6.4: a = 'foo'
#           b = "bar"
#           a b
#           --> invalid syntax: <string>, line 1, pos 3

# Ex C.7: x ='A\nB\nC'

# Ex C.8: x = 80 * '-'

# Ex C.9: x = 'first line\nsecond line\nthird line'

# Ex C.10:
x = 3
y = 12.5
print 'The rabbit is %d.' %x
print 'The rabbit is %d years old.' %x
print '%.1f is average.' %y
print '%.1f * %d' %(y,x)
print '%.1f * %d is %.1f.' %(y,x, y*x)

# Ex C.11:
num = float(raw_input ("Enter a number: "))
print num

# Ex C.12:

def quadratic (a,b,c,x):
    answer = a * x * x + b * x + c
    return answer

# Ex C. 13:

def GC_content (DNAseq):
    '''This function inputs a given DNA Sequence (string) and returns the 
    proportion of the bases which are either G or C (as a float). This ratio
    often represents how stable a DNA molecule typically is because C/G bases 
    bind more strongly than A/T bases.'''
    DNAseq = DNAseq.upper()  # always good to ensure it's in caps...
    G_count = DNAseq.count('G')
    C_count = DNAseq.count ('C')
    totalLength = float(len(DNAseq))
    return ((G_count+C_count) / totalLength)


    