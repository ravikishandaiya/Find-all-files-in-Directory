import os
import time
def get_all_files(a,d,t):
    try:
        if t!=0:
            os.chdir(d)
    
        path=os.getcwd()
        x=os.listdir()
    except:
        print('--------Access Denied-------- for :',d)
        input()
        return
    t+=1
    for file in x:
        while os.getcwd()!=path:
            os.chdir('..')
        try:
            b = os.stat(file).st_size    ## returns size in bytes so b bytes
        except:
            print('--------Access Denied-------- for file/folder :',file)
            input()
            return

        if os.path.isdir(file):
            print(a*t+"Dir :",file )
            get_all_files(a,file,t)
    for file in  x:
        if os.path.isfile(file):
            print(a*t+"File :",file + ', size =',b,"Bytes")
              
def get_empty_files(a,d,t):
    print("    ...--...Empty Files...--...")
    try:
        if t!=0:
            os.chdir(d)
    
        path=os.getcwd()
        x=os.listdir()
    except:
        print('--------Access Denied-------- for :',d)
        input()
        return
    t+=1
    for file in x:
        while os.getcwd()!=path:
            os.chdir('..')
        try:
            b = os.stat(file).st_size    ## returns size in bytes so b bytes
        except:
            print('--------Access Denied-------- for file/folder :',file)
            input()
            return

        if os.path.isdir(file) and int(b)==0:
            print(a*t+"Dir :",file )
            get_empty_files(a,file,t)
    for file in  x:
        if os.path.isfile(file) and int(b)==0:
            print(a*t+"File :",file + ', size =',b,"Bytes")

                
## Main function
while True:
    os.system('cls')
    print("..-.. Q/q for Quit..-..")
    dir=input("Please Enter a valid directory:")
    if dir=="q" or dir=="Q":
        break
    '''while os.getcwd()!=dir:
        os.chdir('..')
        '''
    try:    
        os.chdir(dir)
        print("1. Find all File/Folder within the  directory.")
        print("2. Find only Empty files in the directory.")
        option=input()
        if option=="q" or option=="Q":
            break
        print("Main Dir :",os.getcwd())
        a='    '
        if  option=="1":
            get_all_files(a,os.getcwd(),0)
        elif option=="2":
            get_empty_files(a,os.getcwd(),0)
        else:
            print("Sorry!, Wrong Input.")
    except:
        print("Opps! Something went wrong, please check your entered Directory.")
    
    input("Press any key to continue.")