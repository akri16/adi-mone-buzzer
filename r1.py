from random import *
from qa import *
from f1 import *
from functions import *
from intro import *
g1=g1
g2=g2
g1n1=g1n1
g2n2=g2n2
print g1
 
print ('guruji subjects please')
osub1 ()
 
blank()

print 'So your buzzer question is........'
      
x=randint(0,5)
print bq[x]
b=(raw_input('type 1,2,3,or 4 for player 1 player 2 player3 and player 4 respectively:'))
while b not in ('1','2','3','4'):
    print'INVALID input'
    b=raw_input('type the right input:')
b=int(b)    
an_no=('a',str(x+1))
an_no=eval(''.join(an_no))
print an_no
 

if b==1:
  print g1n2,'type the appropriate answer'  
  s1=raw_input()
  if s1 in an_no :
      print 'Team',g1,'get on to the play station'
      print 'Lets review the subjects'
      blank()
      asdf1('g1')
      blank()
      asew=g2
  else:
      print 'Sorry wrong answer'
      print 'Team',g2,'get on to the play station'
      print 'Lets review the subjects'
      blank()
      asdf1('g2')
      blank()
      asew=g1
      
elif b==2:
    print g1n1,'type the appropriate answer'
    s2=raw_input()

    if s2 in an_no :
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1')
        blank()
        asew=g2
    else:
        print 'Sorry wrong answer'
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2')
        blank()
        asew=g1


        
  
elif b==3:
    print g2n2,'type the appropriate answer'
    u1=raw_input()
    if u1 in an_no :
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2')
        blank()
        asew=g1
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1')
        blank()
        asew=g2
elif b==4:
    print g2n1,'type the appropriate answer'
    u2=raw_input(g2n1,'type the appropriate answer')
    if u2  in an_no :
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2')
        blank()
        asew=g1
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1')
        blank()
        asew=g2




     
      



print asew,'get on to the play station'
print 'Lets review the subjects'
   
sub1=sub1.remove(zz2)  
blank()
sub1(str(asew))
blank()     

print 'So by the end of round 1 lets see the scores'
print 'Team',g1,g1score
print 'Team',g2,g2score

qw=max(g1score,g2score)
wq=min(g1score,g2score)

print qw,'you are leading!!! Keep playing!!!'
print wq,'don`t worry.One more round left.Keep playing!!!'
      
       
