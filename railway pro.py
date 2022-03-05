import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',passwd='vpms123',database='railway')
                        
if mydb.is_connected():
    print('Connection Successful')
    
mycursor=mydb.cursor()
#This method executes the given database operation (query or command). The 
#parameters found in the tuple or dictionary params are bound to the variables 
#in the operation.


mycursor.execute('select pnrno from passengers order by pnrno desc limit 1;')
res=mycursor.fetchall()


#The method fetches all (or all remaining) rows of a query result set and returns
#a  list of tuples. If no more rows are available, it returns an empty list.
pnr=1000
if len(res)>0:
    pnr=int(res[0][0])

def railresmenu():
    print('Railway Reservation')
    print('1.Train Detail')
    print('2.Reservation of ticket')
    print('3.Cancellation of Ticket')
    print('4.Display PNR status')
    print('5.Quit')
    
    n=int(input('Enter your choice:'))
    if(n==1):
        traindetail()
        print()
    elif(n==2):
        reservation()
        print()
    elif(n==3):
        cancel()
        print()
    elif(n==4):
        displayPNR()   
        print()
    elif(n==5):
        print("Thank You For Your Time.")
    else:
        print('ERROR!')
        
        
def traindetail():
    print('Train Details:-')
    ch='y' 
    while (ch=='y'):
        I=[]
        name=input('Enter train name:')
        I.append(name)
        tnum=int(input('Enter train number:'))
        I.append(tnum)
        ac1=int(input('Enter number of AC 1 class seats:'))
        I.append(ac1)
        ac2=int(input('Enter number of AC 2 class seats:'))
        I.append(ac2)
        ac3=int(input('Enter number of AC 3 class seats:'))
        I.append(ac3)
        slp=int(input('Enter number of sleeper class seats:'))
        I.append(slp)
        train=(I)
        sql='insert into traindetail(tname,tnum,ac1,ac2,ac3,sip) values(%s,%s,%s,%s,%s,%s)'
        
        mycursor.execute(sql,train)
        mydb.commit()
        print('Insertion completed')
        print('Do you want to insert more train detail?:')
        ch=input('Enter y/n:')
        print('===============================================================')



def reservation():
    global pnr
    I1=[]
    np=1
    pname=input('Enter passenger names:')
    I1.append(pname)
    age=int(input('Enter age:'))
    if (age<18):
        print('Sorry you are underage')
        return
    else:
        pass  
    I1.append(age)
    trainn=int(input('Enter Train no.:'))
    I1.append(trainn)
    print('Select a class you would like to travel in:')
    print('1.AC First class')
    print('2.AC Second class')
    print('3.AC Third class')
    print('4.Sleeper class')
    cp=int(input('Enter your travelling class choice:'))
    passno=int(input('Enter no. of passengers:'))
    I1.append(passno)
    if(cp==1):
        amount=np*1000*passno
        cls='ac1'
    elif(cp==2):
        amount=np*800*passno
        cls='ac2'
    elif(cp==3):
        amount=np*500*passno
        cls='ac3'
    else:
        amount=np*350*passno
        cls='slp'
    I1.append(cls)
    print("Total amount to be paid:",amount)
    I1.append(amount)
    pnr=pnr+1
    print('PNR Number:',pnr)
    print('Status confirmed')
    sts='Confirm'
    I1.append(sts)
    I1.append(pnr)
    train1=(I1)
    sql="insert into passengers(pname,age,trainno,noofpas,cls,amt,status,pnrno) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        
    mycursor.execute(sql,train1)
    mydb.commit()
    print('insertion completed')
    print('Go back to menu')
    print('===================================================================')

def cancel():

    print("Ticket cancel window")
    pnr=input('Enter PNR for cancellation of Ticket:')
    pn=(pnr,)
    dummy=0
    mycursor.execute('select pnrno from passengers;')
    res=mycursor.fetchall()
    numbers = [ int(x) for x in res ]
    for x in numbers:
        if x==pnr:
            sql="update passengers set status='deleted' where pnrno=%s"
            mycursor.execute(sql,pn)
            mydb.commit()
            print('Deletion completed')
            print('Go Back to menu')
            print('===================================================================')
      
            
            
    
            
    
            
        
        
    
 
def displayPNR():
    print('PNR status windows:-')
    pnr=int(input('Enter PNR NUMBER:'))
    pn=(pnr,)
    sql='select*from passengers where pnrno=%s'
    mycursor.execute(sql,pn)
    res1=mycursor.fetchall()
    mydb.commit()
    print('PNR STATUS are as follows:')
    for x in res1:
        print(x)
    if x not in res1:
        print('Not found')
    print('===================================================================')
        
railresmenu()
