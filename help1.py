sub=input('Enter Subject: ')
if(sub == "Science" or sub == "science"):
    sci_the, sci_pra =input('Enter Science Theory and Practical Marks : ').split()
    sci_the = int(sci_the)
    sci_pra = int(sci_pra)
    if(sci_the > 50):
        print("Please Check input score for Science Thoery")
    elif(sci_pra > 50):
        print("Please check input score for Science Practical")
    else: print("Your Science Total is: ", (60/100)*sci_the + (40/100)*sci_pra)
elif(sub == "English" or sub == "english" ):
    eng_the, eng_pra = input('Enter English Theory and Practical Marks : ').split() 
    eng_the, eng_pra =input('Enter English Thoery and Practical Marks : ').split()
    eng_the = int(eng_the)
    eng_pra = int(eng_pra)
    if(eng_the > 60):
        print("Please check input score for English Thoery")
    elif(eng_pra > 40):
        print("Please check input score for English Practical")
    else:
        print("Your English Total is: ", (60/100)*eng_the + (40/100)*eng_pra)
else: print("Subject not recognised ")


   

