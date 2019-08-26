import os
os.startfile('p.mp3')
from random import *
from qa import *
from intro import *
from functions import blank
from RULES import*
def asdf1 (t,h):
   
  t1=eval(''.join((t,'n1')))
  t2=eval(''.join((t,'n2')))
  s=0 
  
  
  
  if h==1: 
   print '(1)',k1
   print '(2)',k2
   print '(3)',k3
   print '(4)',k4
   pas=[k1,k2,k3,k4] 
   global pas
  else:
    pas.remove(zz2)
    lok=0 
    for lkj in pas:
      
     
      lok=lok+1
      print lok,lkj
      

   
  

  if h==1:
   user_in=raw_input('Select the desired subject')
  
   while user_in not in ('1','2','3','4'):
    print 'INVALID input'
                          
    user_in=raw_input('Select the desired subject')

   
   zz=pas
   zz1=int(user_in)-1
   zz2=zz[zz1]
   print 'Guruji question please'
   print 'Which of the following are',zz2,'?'
   zz3=sub1.index(zz2)
   zz4=zz3+1
   zz5=eval(''.join(('n',str(zz4))))
   print zz5
   global zz2

  else :
    user_in=raw_input('Select the desired subject')
  
    while user_in not in ('1','2','3'):
     print 'INVALID input'
                          
     user_in=raw_input('Select the desired subject')
    
     
    zz1=int(user_in)-1
    print pas
    zz2=pas[zz1]
    print zz2 
    print 'Guruji question please'
    print 'Which of the following are',zz2,'?'
    zz3=sub1.index(zz2)
    zz4=zz3+1
    zz5=eval(''.join(('n',str(zz4))))
    print zz5
    global zz2
  hyt=['1','2','3','4','5','6','7','8','9','10']
  print t1,'it is your turn now' 
  print 'Type the correct answer:'
  sln1=raw_input('sol1:')
  while sln1 not in hyt:
          print 'INVALID input'
          sln1=raw_input('sol1:')
  hyt.remove(sln1)        
          
  sln2=raw_input('sol2:')
  while sln2 not in hyt:
          print 'INVALID input'
          sln2=raw_input('sol2:')
  hyt.remove(sln2)         
  sln3=raw_input('sol3:')
  while sln3 not in hyt:
          print 'INVALID input'
          sln3=raw_input('sol3:')
  hyt.remove(sln3)         
  sln4=raw_input('sol4:')
  while sln4 not in hyt:
          print 'INVALID input'
          sln4=raw_input('sol4:')
  hyt.remove(sln4)         
  sln5=raw_input('sol5:')
   
  while sln5 not in hyt:
          print 'INVALID input'
          sln5=raw_input('sol5:')

           
  
   
  print t1,'type "change" to change the solutions else proceed' 
  cnf=raw_input()
  while (cnf !='change') and (cnf !=''):
      print 'INVALID input'
      print t1,'type "change" to change the solutions else proceed'
      cnf=raw_input()
  hyt=['1','2','3','4','5','6','7','8','9','10']   
  if cnf=='change':    
      print 'retype the correct answers'
      sln1=raw_input('sol1:')
      while  sln1 not in hyt:
          print 'INVALID input'
          sln1=raw_input('sol1:')
      hyt.remove(sln1)    
      sln2=raw_input('sol2:')
      while  sln2 not in hyt:
          print 'INVALID input'
          sln2=raw_input('sol1:')
      hyt.remove(sln2)     
      sln3=raw_input('sol3:')
      while  sln3 not in hyt:
          print 'INVALID input'
          sln3=raw_input('sol1:')
      hyt.remove(sln3)     
      sln4=raw_input('sol4:')
      while  sln4 not in hyt:
          print 'INVALID input'
          sln4=raw_input('sol1:')
      hyt.remove(sln4)     
      sln5=raw_input('sol5:')
       
      while  sln5 not in hyt:
          print 'INVALID input'
          sln5=raw_input('sol1:')
           
          
  
          
          
  if cnf=='' or cnf=='change':   

      blank()

      print t2,'its your turn.....'
  
      print t2,'type "change" to change the solutions else proceed'
      cnf1=raw_input()
      while (cnf1 !='change')and (cnf1 !=''):
       print 'INVALID input'
       print t2,'type "change" to change the solutions else proceed'
       cnf1=raw_input()

       
      
      if cnf1=='change':
        s=0
        hyt=['1','2','3','4','5','6','7','8','9','10']
        print 'retype the correct answers'
        sLn1=raw_input('sol1:')
        while sLn1 not in hyt:
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        hyt.remove(sLn1)  
        sLn2=raw_input('sol2:')
        while sLn2 not in hyt :
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        hyt.remove(sLn2)  
        sLn3=raw_input('sol3:')
        while sLn3 not in hyt:
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        hyt.remove(sLn3)  
        sLn4=raw_input('sol4:')
        while sLn4 not in hyt:
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        hyt.remove(sLn4)  
        sLn5=raw_input('sol5:')

         
        while sLn5 not in hyt:
          print 'INVALID input'
          sLn1=raw_input('sol1:')
          
           
        
      if cnf1=='' or cnf1=='change':
          blank()
          print 'Now lets see to the answers','Dont be afraid!!!'
          xcv=[sln1,sln2,sln3,sln4,sln5]
          
          if cnf1=='':
            for afgh in xcv:
              if int(afgh)in (eval(''.join(('Ans',str(zz4))))):
               ast=zz5[(int(afgh))-1]
               print ast,'--> double correct-->2000 points'
               s=s+2000
              else:
                ast=zz5[(int(afgh))-1]
                print ast,'-->Sorry,wrong answer'
             
            
          elif cnf1=='change':
            mnb=[sLn1,sLn2,sLn3,sLn4,sLn5]
             
            

            for y in xcv :
             
              if (y in mnb) and (int(y) in(eval(''.join(('Ans',str(zz4)))))):
                s=s+2000
                mnb.remove(y)
                mnj=zz5[(int(y))-1]
                print mnj,'--> double correct-->2000 points'
                 
            for pl in mnb:
             if int(pl) in (eval(''.join(('Ans',str(zz4))))):
              s=s+1000
              act=zz5[(int(pl))-1]
              print act,'--> correct-->1000 points'
             else:
              act=zz5[(int(pl))-1]

              print act,'-->Sorry,wrong answer'
          print 'Now lets see which all are right answers'
          print 'So the correct answers are--->'

          for asw in (eval(''.join(('Ans',str(zz4))))):
             
              print zz5[asw-1]
              
             


          blank()

          if s==10000:
              print 'ya!hoo!,you`ve got a bonus!!!'
              s=s+5000
           
           
          if t=='g1':
            score1=s

            global score1
          elif t=='g2':
            score2=s
            
          global score2
              
          t=eval(t)     
          print 'team', t,'your team score is',s
  



def osub1 (R):
  
   
   
  x1=randint(0,13)
  if R=='r1':
   k1=sub1[x1]
  else :k1=sub3[x1] 
  print '(1)',k1

  x2=randint(0,13)
  while x2==x1:
    x2=randint(0,13)
  if R=='r1':
   k2=sub1[x2]
  else :k2=sub3[x2]
   
  print '(2)',k2
 
  x3=randint(0,13)
  while (x3==x1) or (x3==x2):
    x3=randint(0,13)
  if R=='r1':
   k3=sub1[x3]
  else :k3=sub3[x3]  
   
  print '(3)',k3

  x4=randint(0,13)                 
  while (x4==x1)or (x4==x2)or(x4==x3):
    x4=randint(0,13)
  if R=='r1':
   k4=sub1[x4]
  else :k4=sub3[x4]  
   
  print '(4)',k4

  global k1
  global k2
  global k3
  global k4
#------------------------------

    
def main ():
  
  
  
 print'ADI MONA BUZZER FOR ROUND-1-->TYPE IT RIGHT'
 rul1()
 print ('guruji subjects please')
 osub1 ('r1')
 
 blank() 
 
 print 'So your buzzer question is........'
      
 x=randint(0,5)
 print bq[x]
 b=(raw_input('type 1,2,3,or 4 for player 1 player 2 player3 and player 4 respectively:'))
 while (b not in ('1','2','3','4'))or b=='' :
    print'INVALID input'
    b=raw_input('type the right input:')
 b=int(b)    
 an_no=('a',str(x+1))
 an_no=eval(''.join(an_no))
  

 if b==1:
  print g1n2,'type the appropriate answer:'  
  s1=raw_input()
  while len(s1)==0 or len(s1)>25:
    print 'INVALID Input'
    print g1n2,'type the appropriate answer:'  
    s1=raw_input()
    
   
  if an_no in s1 :
      print 'Right Answer'
      print 'Team',g1,'get on to the play station'
      print 'Lets review the subjects'
      blank()
      asdf1('g1',1)
      blank()
      asew='g2'
      pm=g1
  else:
      print 'Sorry wrong answer'
      print 'Team',g2,'get on to the play station'
      print 'Lets review the subjects'
      blank()
      asdf1('g2',1)
      blank()
      asew='g1'
      pm=g1
 elif b==2:
    print g1n1,'type the appropriate answer:'
    s2=raw_input()
    while len(s2)==0 or len(s2)>25:
     print 'INVALID Input'
     print g1n1,'type the appropriate answer:'  
     s2=raw_input()

    if  an_no in s2  :
        print 'Right Answer'
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1',1)
        blank()
        asew='g2'
    else:
        print 'Sorry wrong answer'
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2',1)
        blank()
        asew='g1'
        pm=g1


        
  
 elif b==3:
    print g2n2,'type the appropriate answer:'
    u1=raw_input()
    while len(u1)==0 or len(u1)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u1=raw_input()
     
    if  an_no in u1 :
        print 'Right Answer'
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2',1)
        blank()
        asew='g1'
        pm=g1
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1',1)
        blank()
        asew='g2'
        pm=g2
 elif b==4:
    print g2n1,'type the appropriate answer:'
    u2=raw_input()
    while len(u2)==0 or len(u2)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u2=raw_input()
    if  an_no  in u2 :
        print 'Right Answer'
        print 'Team',g2,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g2',1)
        blank()
        asew='g1'
        pm=g1
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        print 'Lets review the subjects'
        blank()
        asdf1('g1',1)
        blank()
        asew='g2'
        pm=g2




     
 print 'So the right answer is-->'
 print an_no     
 if asew ==g1:
   print 'Team',g2,',you can get back to your team station'
   print 'Team',g1,'get on to the play station'    
 else:
   print 'Team',g1,',you can get back to your team station'
   print 'Team',g2,'get on to the play station'

 
 
 print 'Lets review the subjects'
 asdf1(asew,2)
 
 print 'So by the end of round 1 lets see the scores'
 print 'Team',g1,'-->',score1
 print 'Team',g2,'-->',score2

 if score1!=score2:
  qw=max( score1,score2)
  wq=min(score1,score2)
  if qw==score1:
    mnk=g1
    mpk=g2
  else :
    mnk=g2
    mpk=g1
  
  print mnk,'you are leading with',qw, 'Keep playing!!! ' 
  print mpk,'don`t worry,you have earned',wq,'.One more round left.Keep playing!!!'
 
 else:print 'Team',g1,'and Team',g2,'you have earned a tie of', score1
 blank()


 
 print 'Now lets play ROUND-2 --> KNOCK OUT ROUND'
 blank()
 print 'ADI MONA BUZZER for ROUND-2 --> KNOCK OUT ROUND'
 
 blank()
 rul2()

 print 'Best of luck!!!!'
 blank()
 print 'Guruji Question Please'
 print 'So your first question is.....'
 just=range(0,21)
 global just
 asdf2()
 blank()
 print 'Now your second question .....'
 asdf2()
 blank()
 print 'Here goes your third question.....'
 asdf2()
 blank()
 print 'Now your fourth question...'
 asdf2()
 blank()
 print 'And the final question of this round....'
 print 'Here goes it'
 asdf2()
 blank()

 print 'So by the end of Round 2, lets see your team scores'
 print 'Team',g1,'-->',score1,'Points'
 print 'Team',g2,'-->',score2,'Points'
 
 if score1!=score2:
  qw=max( score1,score2)
  wq=min(score1,score2)
  if qw==score1:
    mnk=g1
    mpk=g2
  else :
    mnk=g2
    mpk=g1
  
  print mnk,'you are leading with',qw, 'Keep playing!!! '
  print 'So Team',mnk,'You are qualified for JACKPOT ROUND'
  print mpk,'don`t worry,you have earned',wq,'you have done your best!!!'
 
 else:
   print 'Team',g1,'and Team',g2,'you have earned a tie of', score1
   print 'So lets have a TIE BREAK question for JACKPOT qualification'
   
 
 print 'So now lets play ROUND-3 JACKPOT ROUND'
 print 'ADI MONA BUZZER for ROUND-3 -->JACKPOT ROUND'
 blank()
 rul3()
 print 'Team',mnk,'get on to the play station'
 blank()
 asdf3()
 print 'So by the end of JACKPOT ROUND ,lets view the scores'
 print 'Team',g1,'--->',score1,'Points'
 print 'Team',g2,'--->',score2,'Points'
 if score1!=score2:
  qw=max( score1,score2)
  wq=min(score1,score2)
  if qw==score1:
    mnk=g1
    mpk=g2
  else :
    mnk=g2
    mpk=g1
  
  print 'Team',mnk,'you are leading with',qw
  
  print mpk,'don`t worry,you have earned',wq,'you have done your best!!!'
 

 blank()

 print'So today we had tough contestents'
 blank()
 print'They have cooperated with us well to provide the global a fruitful and enjoyable game'
 print 'Thank you all my contestents'
 blank()
 print 'Now I thank the holy GURUJI who have spreaded knowledge to us'
 blank()
 print'Last but not the least, I thank all the global malayalees'
 blank()

 print'My buddies sweet hearts ,love sky high and keep falling in love again and again and again'


 blank()
 print 'SO THERE COME TO END THIS ADI MONA BUZZER PROGRAM!!!'
 blank()
 print 'Thank you for your kind cooperation'
 blank()
 dfrew=raw_input('Would you like to drop a feedback to us?(y/n)')
 while dfrew!='y'and dfrew!='n':
   print 'INVALID input'
   dfrew=raw_input('Would you like to drop a feedback to us?(y/n)')
 if dfrew=='y':  
  feedback=raw_input('Enter your feedback and name')
  target=open('feedback.txt',"w")
  target.write(feedback+"\n")
  print 'Thank you for your kind feedback'
 else:print 'Ok Thank You' 
 blank()
 
 print 'I Amit signing off',',good bye'
 os.system("TASKKILL /F /IM wmplayer.exe")
 global mnk
 print '----------------------THE END--------------------------'
 asde=raw_input('Do you want to run the programme again?(y/n):')
 while asde!='y' and asde!='n':
   print'INVALID INPUT'
   asde=raw_input('Do you want to run the programme again?(y/n):')

 if asde=='y':
   from intro import* 
   main()
 else:
   print 'Ok,Thank you'
   quit()
 
 
 


                 
                 
                


def asdf2():
 global score1
 global score2
 
 ran=choice(just)
 _just= sub2[ran]
 print _just
 just.remove(ran)
 bp=(raw_input('type 1,2,3,or 4 for player 1 player 2 player3 and player 4 respectively:'))
 while (bp not in ('1','2','3','4'))  :
    print'INVALID input'
    bp=raw_input('type the right input:')
 bp=int(bp)    
 an_n=('p',str(ran+1))
 an_n=eval(''.join(an_n))
  

 if bp==1:
  print g1n2,'type the appropriate answer:'  
  s1=raw_input()
  while len(s1)==0 or len(s1)>25:
    print 'INVALID Input'
    print g1n2,'type the appropriate answer:'  
    s1=raw_input()
    
   
  if an_n in s1 :
      print 'Right Answer'
        
      blank()
      score1=score1+4000
      print 'Team',g1 ,'You get 4000 points'
  else:
      print 'Sorry wrong answer'
        
      blank()
      score1=score1-3000 
      blank()
      print 'Team',g1,'I am sorry,you get -3000 points'
  print 'Team',g1,'your current score is',score1    
 elif bp==2:
    print g1n1,'type the appropriate answer:'
    s2=raw_input()
    while len(s2)==0 or len(s2)>25:
     print 'INVALID Input'
     print g1n1,'type the appropriate answer:'  
     s2=raw_input()

    if  an_n in s2  :
        print 'Right Answer'
         
        blank()
        print 'Team',g1 ,'You get 4000 points'
        s1=score1+4000 
    else:
        print 'Sorry wrong answer'
        blank()
        score1=score1-3000
        print 'Team',g1,'I am sorry,you get -3000 points'
    print 'Team',g1,'your current score is',score1    
 

        
  
 elif bp==3:
    print g2n2,'type the appropriate answer:'
    u1=raw_input()
    while len(u1)==0 or len(u1)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u1=raw_input()
     
    if  an_n in u1 :
        print 'Right Answer'
        blank()
        score2=score2+4000
        print 'Team',g2 ,'You get 4000 points'
    else:
        print 'Sorry wrong answer'
        blank()
        score2=score2-3000
        print 'Team',g2,'I am sorry,you get -3000 points'
    print 'Team',g2,'your current score is',score2    
 elif bp==4:
    print g2n1,'type the appropriate answer:'
    u2=raw_input()
    while len(u2)==0 or len(u2)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u2=raw_input()
    if  an_n  in u2 :
        print 'Right Answer'
        blank()
        score2=score2+4000
        print 'Team',g2 ,'You get 4000 points'
    else:
        print 'Sorry wrong answer'
        
         
        blank()
        score2=score2-3000
        print 'Team',g2,'I am sorry,you get -3000 points' 
    print 'Team',g2,'your current score is',score2
 print 'So the right answer is-->'
 print an_n
 global sub2  
  


  
def tb():
 ran=choice(just) 
 _just= sub2[ran]
 print _just
 sub2.remove(_just)
 bp=(raw_input('type 1,2,3,or 4 for player 1 player 2 player3 and player 4 respectively:'))
 while (bp not in ('1','2','3','4'))  :
    print'INVALID input'
    bp=raw_input('type the right input:')
 bp=int(bp)    
 an_n=('p',str(just+1))
 an_n=eval(''.join(an_n))

 if b==1:
  print g1n2,'type the appropriate answer:'  
  s1=raw_input()
  while len(s1)==0 or len(s1)>25:
    print 'INVALID Input'
    print g1n2,'type the appropriate answer:'  
    s1=raw_input()
    
   
  if an_no in s1 :
      print 'Right Answer'
      print 'Team',g1,'you are qualified for JACKPOT ROUND'
      print 'Team',g1,'get on to the play station'
      mnk=g1 
       
  else:
      print 'Sorry wrong answer'
      print 'Now,Team',g2,'you are qualified for JACKPOT ROUND'
      print 'Team',g2,'get on to the play station'
      mnk=g2 
       
 elif b==2:
    print g1n1,'type the appropriate answer:'
    s2=raw_input()
    while len(s2)==0 or len(s2)>25:
     print 'INVALID Input'
     print g1n1,'type the appropriate answer:'  
     s2=raw_input()

    if  an_no in s2  :
        print 'Right Answer'
        print 'Team',g1,'you are qualified for JACKPOT ROUND'

        print 'Team',g1,'get on to the play station'
        mnk=g1  
    else:
        print 'Sorry wrong answer'
        print 'Team',g2,'get on to the play station'
        mnk=g2 

        
  
 elif b==3:
    print g2n2,'type the appropriate answer:'
    u1=raw_input()
    while len(u1)==0 or len(u1)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u1=raw_input()
     
    if  an_no in u1 :
        print 'Right Answer'
        print 'Team',g2,'you are qualified for JACKPOT ROUND'

        print 'Team',g2,'get on to the play station'
        mnk=g2
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        mnk=g1 
 elif b==4:
    print g2n1,'type the appropriate answer:'
    u2=raw_input()
    while len(u2)==0 or len(u2)>25:
     print 'INVALID Input'
     print g2n2,'type the appropriate answer:'  
     u2=raw_input()
    if  an_no  in u2 :
        print 'Right Answer'
        print 'Team',g2,'you are qualified for JACKPOT ROUND'

        print 'Team',g2,'get on to the play station'
        mnk=g2 
    else:
        print 'Sorry wrong answer'
        print 'Team',g1,'get on to the play station'
        mnk=g1 
 global mnk
 print 'So the right answer is-->'
 print an_n

def asdf3():
   print 'So lets see today`s subjects'
   blank()
   osub1('r3')
   blank()
   if mnk==g1:
    pl1=g1n1
    pl2=g2n2
   elif mnk==g2:
    pl1=g2n1
    pl2=g2n2

   cmos=[pl1,pl2]
   pq=choice(cmos)
   cmos.remove(pq)
   print pq,'Its your turn now'
   user_in=raw_input('Select the desired subject')
  
   while user_in not in ('1','2','3','4'):
    print 'INVALID input'
                          
    user_in=raw_input('Select the desired subject')
   pas=(k1,k2,k3,k4)
   zz=pas
   zz1=int(user_in)-1
   zz2=zz[zz1]
   print 'Guruji question please'
   print 'Which of the following are',zz2,'?'
   zz3=sub3.index(zz2)
   zz4=zz3+1
   zz5=eval(''.join(('m',str(zz4))))
   print zz5
   global zz2
   
   print 'Type the correct answer:'
   sln1=raw_input('sol1:')
   while sln1 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln1=raw_input('sol1:') 
          
   sln2=raw_input('sol2:')
   while sln2 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln2=raw_input('sol2:')
   sln3=raw_input('sol3:')
   while sln3 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln3=raw_input('sol3:')
   sln4=raw_input('sol4:')
   while sln4 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln4=raw_input('sol4:')
   sln5=raw_input('sol5:')
   
   while sln5 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln5=raw_input('sol5:')

           
  
   
   print pq,'type "change" to change the solutions else proceed' 
   cnf=raw_input()
   while (cnf !='change') and (cnf !=''):
      print 'INVALID input'
      print t1,'type "change" to change the solutions else proceed'
      cnf=raw_input()
      
   if cnf=='change':    
      print 'retype the correct answers'
      sln1=raw_input('sol1:')
      while  sln1 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln1=raw_input('sol1:')
      sln2=raw_input('sol2:')
      while  sln2 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln2=raw_input('sol1:')
      sln3=raw_input('sol3:')
      while  sln3 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln3=raw_input('sol1:')
      sln4=raw_input('sol4:')
      while  sln4 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln4=raw_input('sol1:')
      sln5=raw_input('sol5:')
       
      while  sln5 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sln5=raw_input('sol1:')
           
          
  
          
   lk=cmos[0]        
   if cnf=='' or cnf=='change':   

      blank()

      print lk,'its your turn.....'
  
      print lk,'type "change" to change the solutions else proceed'
      cnf1=raw_input()
      while (cnf1 !='change')and (cnf1 !=''):
       print 'INVALID input'
       print t2,'type "change" to change the solutions else proceed'
       cnf1=raw_input()

       
      
      if cnf1=='change':
        s=0
        print 'retype the correct answers'
        sln1=raw_input('sol1:')
        while sLn1 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        sln2=raw_input('sol2:')
        while sLn2 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        sln3=raw_input('sol3:')
        while sLn3 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        sln4=raw_input('sol4:')
        while sLn4 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sLn1=raw_input('sol1:')
        sln5=raw_input('sol5:')

         
        while sln5 not in ('1','2','3','4','5','6','7','8','9','10'):
          print 'INVALID input'
          sLn1=raw_input('sol1:')

      if cnf1=='' or cnf1=='change':
          blank()
          print 'Now lets see to the answers','Dont be afraid!!!'
          xcv=[sln1,sln2,sln3,sln4,sln5]
          
          if cnf1=='' or cnf1=='change':
            for afgh in xcv:
              ast=zz5[(int(afgh))-1]
              if int(afgh)in (eval(''.join(('sol',str(zz4))))):
                print ast,'You have got it right'
              else:print 'I am Sorry',ast,'is wrong answer'
          kljh=(eval(''.join(('sol',str(zz4)))))
          print 'So the correct answers are--->'

          for asw in kljh:
             
              print zz5[asw-1]
              
          if sln1  in kljh and sln2 in kljh and sln3 in kljh and sln4 in kljh :
            print 'Team',mnk,'You have won a JACKPOT!!!!!!!!!!!!!!!!!'
            if mnk==g1:
              
             score1='JACKPOT +',score1
            elif mnk==g2:
             score2='JACKPOT +',score2 
            print'-----------YA!HOOO!!!,YOU HAVE WON JACKPOT!,JACKPOT!!,JACKPOT!!!-----------'
          else:print 'I am sorry you have lost the JACKPOT ROUND'
          
main()

          
                

              
           
          


  
   
   
 
    
