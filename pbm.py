#This is a python program to implement phone book using file management system
#It will store the name and phone number of the person in a file
#The program will have the following functionalities
#1. Add a new contact
#2. Delete a contact
#3. Search a contact
#4. Display all contacts
#5. Exit the program
#6. Delete all contacts.
#Project 1 (IST SEM)

def search(x):
    file=open("file.txt",'r')
    results=[]
    for i in file:
        if i.strip().split()[0]==x or i.strip().split()[1]==x:
            results.append(i.strip())
    return results
                
def addNumbers():
    name=input("Enter the name of the person: ")
    phone_number=input("Enter the phone number of the person: ")
    file=open("file.txt",'r')
    if file.read()!='':
        check1=search(name)
        check2=search(phone_number)
        if len(check1)>0 or len(check2)>0:
            print("Error! Contacts already exists")
            return "TASK INCOMPLETED"
        else:
            file.close()
            file=open("file.txt",'a')
            file.write('\n'+name+" "+phone_number)
    else:
        file=open("file.txt",'w')
        file.write(name+" "+phone_number)
    file.close()
    print("Contact Saved")
    return "TASK COMPLETED"


def delNumbers():
    newcontact=''
    x=input("Enter The Name or Number ")
    check=search(x)
    if len(check)>1:
        print("Multiple Contacts Exists with the same name")
        for i in check:
            print(i)
        return "TASK INCOMPLETED"
    elif len(check)==0:
        print("Contact does not exist as per given information")
        return "TASK INCOMPLETED"
    file=open("file.txt",'r')
    for i in file:
        if i.strip()==check[0]:
            print(i,"DELETED")
            continue
        else:
            newcontact+=i
    print("New",newcontact)
    file.close()
    file=open("file.txt",'w')
    file.write("NEW CONTACTS ARE:\n",newcontact)
    file.close()
    return "TASK COMPLETED"

def delallContacts():
    if not input("Press 0 to confirm or else cancel request"):
        return "TASK INCOMPLETED"
    file=open("file.txt",'w')
    file.write("")
    return "TASK COMPLETED"

def display():
    file=open("file.txt",'r')
    count=1
    for i in file:
        print(count,". ",i, sep='')
        count+=1
    return "TASK COMPLETED"
while(True):
    try:
        file=open("file.txt",'r')
    except Exception:
        file=open("file.txt",'w')
        file.close()
        file=open("file.txt",'r')
    print("Press 0 to DISPLAY CONTACTS")
    print("Press 1 for ADD CONTATCTS")
    print("Press 2 to DELETE CONTACTS")
    print("Press 3 to SEARCH CONTACTS")
    print("Press 4 to DELETE ALLCONTATCTS")
    print("Press 5 to EXIT")
    try:
        x=int(input())
    except Exception:
        print("Invalid Input")
    flag=True
    if file.read()=='':
        flag=False
    file.close()
    if x==0:
       if flag==False:
           print("NO CONTACTS AVAILABLE")
       else:
           print(display())
    elif x==1:
        print(addNumbers())
    elif x==2:
        if flag==False:
            print("NO CONTACT AVAILABLE")
        else:
            print(delNumbers())
    elif x==3:
        if flag==False:
            print("NO CONTACT AVAILABLE")
        else:
            results=search(input("Enter Name or Number"))
            for i in range(len(results)):
                print((i+1),". ",results[i],sep='')
            if len(results==0):
                print("NO CONTACT FOUND")
    elif x==4:
        if flag==False:
            print("NO CONTACT AVAILABLE")
        else:
            print(delallContacts())
    elif x==5:
        print("TASK COMPLETED")
        exit(0)
    else:
        print("Invalid Input")
    x=input("press any number to continue")






    
        

