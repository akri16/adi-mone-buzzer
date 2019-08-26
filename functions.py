def blank() :
    print''
    o5=raw_input()
    if o5 == 'q' or o5=='quit':
                      confirm=raw_input( 'do you really want to quit the game?(y/n)')
                      if confirm=='yes'or confirm=='y':quit()
                      elif confirm == 'no' or confirm=='n' : print 'ok'
                      else :print 'INVALID INPUT'
    while o5 !='':
           o5=raw_input()
           continue

        

