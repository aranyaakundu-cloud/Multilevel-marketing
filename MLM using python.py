import pickle


#save records
def saveRecords(reclist):
    f = open("mlm.dat", "wb")
    for r in reclist:
        pickle.dump(r, f)
    f.close()

#insert member
def insertMember():
    mid=input("enter member id:")
    name=input("enter member name")
    sponsor_id=input("enter sponsor Id(leave blank if none):")
    phone_no=input("enter phone number")
    password=input("enter 4 digit password")

    rec={
        'MemberID':mid,
        'Name':name,
        'SponsorID':sponsor_id,
        'PhoneNo':phone_no,
        'Password':password
    }
    f=open('mlm.dat','ab')
    pickle.dump(rec,f)
    f.close()
    print("member added successfully")

#display member
def displayMembers():
    f=open('mlm.dat','rb')
    while True:
        try:
            rec=pickle.load(f)
            print("Member ID:",rec['MemberID'])
            print("Name:",rec['Name'])
            print("Sponsor ID:",rec['SponsorID'])
            print("Phone no:",rec['PhoneNo'])
            print("Password:",rec['Password'])
            
        except EOFError:
            break
    f.close()

#search member
def searchMembers():
    mid=input("enter MemberID to search:")
    f=open('mlm.dat','rb')
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec['MemberID']== mid:
                print("Member ID:",rec['MemberID'])
                print("Name:",rec['Name'])
                print("Sponsor ID",rec['SponsorID'])
                print("Phone no:",rec['PhoneNo'])
                print("Password:",rec['Password'])
                flag=True
        except EOFError:
            break
    if flag == False:
        print('No records Found')
    f.close()

#update sponsor
def updateSponsor():
    mid=input("enter MemberID to update")
    new_sponsor = input("Enter new Sponsor ID: ")

    f = open('mlm.dat', 'rb')
    reclst = []

    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()

    for r in reclst:
        if r['MemberID'] == mid:
            r['SponsorID'] = new_sponsor

    f = open('mlm.dat', 'wb')
    for r in reclst:
        pickle.dump(r, f)
    f.close()
    print("sponsor updated successfully")
    
#delete Members
def deleteMember():
    mid =input("enter the MemberID to delete:")

    f=open('mlm.dat','rb')
    rec1st=[]
    while True:
        try:
            rec=pickle.load(f)
            rec1st.append(rec)
        except EOFError:
            break
    f.close()
    f=open('mlm.dat','wb')
    for r in rec1st:
        if r['MemberID']!=mid:
            pickle.dump(r,f)
    f.close()
    
#add new member under existing member
def addMemberUnderSponsor(sponsor_id):
    mid = input("Enter New Member ID: ")

    f = open('mlm.dat', 'rb')
    rec1st = []
    flag = False

    while True:
        try:
            rec = pickle.load(f)
            if rec['MemberID'] == mid:
                flag = True
            rec1st.append(rec)
        except EOFError:
            break
    f.close()

    if flag:
        print("Member already exists")
        return

    name = input("Enter New Member Name: ")
    phone_no = input("PhoneNo: ")
    password = input("Password: ")

    new_rec = {
        'MemberID': mid,
        'Name': name,
        'SponsorID': sponsor_id,
        'PhoneNo': phone_no,
        'Password': password
    }

    rec1st.append(new_rec)

    f = open('mlm.dat', 'wb')
    for r in rec1st:
        pickle.dump(r, f)
    f.close()

    print("New member added under you successfully")

#update member under existing member
def updateMemberUnderSponsor(sponsor_id):
    target_id= input("enter Member ID to update under you")
    f=open('mlm.dat','rb')
    rec1st=[]
    flag = False
    
    while True:
        try:
            rec1st.append(pickle.load(f))
        except EOFError:
            break
    f.close()

    for r in rec1st:
        if r['MemberID']== target_id and r['SponsorID'] == sponsor_id:
            r['Name']= input("enter new name")
            r['PhoneNo']= input("enter new phone no")
            flag= True

    if flag:
        f = open('mlm.dat','wb')
        for r in rec1st:
            pickle.dump(r,f)
        f.close()
        print("member updated successfully")
    else:
        print("you cannot update")
    
    
#delete member under existing member
def deleteMemberUnderSponsor(sponsor_id):
    target_id =input("enter the MemberID to delete:")
    f=open('mlm.dat','rb')
    rec1st=[]
    while True:
        try:
            rec=pickle.load(f)
            rec1st.append(rec)
        except EOFError:
            break
    f.close()
    flag= False
    f=open('mlm.dat','wb')
    for r in rec1st:
        if r['MemberID']== target_id and r['SponsorID'] == sponsor_id:
            flag=True
        else:
            pickle.dump(r,f)
    f.close()

    if flag:
        print("Downline member deleted successfully")
    else:
        print("You can delete only your own downline")

#display member under existing member
def displayMemberUnderMe(sponsor_id):
    f=open('mlm.dat','rb')
    print("\n--- MEMBERS UNDER YOU ---")
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['SponsorID'] == sponsor_id:
                print("\nMember ID:", rec['MemberID'])
                print("Name:", rec['Name'])
                print("Phone no:",rec['PhoneNo'])
                print("Password:",rec['Password'])
                flag = True
        except EOFError:
            break
    f.close()

    if flag:
        print("Members displayed")
    else:
        print("No members under you")

#member login
def memberLogin():
    mid=input("enter your Member ID")
    phone=input("Enter phone number: ")
    password = input("Enter password: ")
    f=open('mlm.dat','rb')
    flag =False

    while True:
        try:
            rec=pickle.load(f)
            if rec['MemberID']== mid and rec['PhoneNo']==phone and rec['Password']==password:
                flag= True
                print("\nLogin Successful")
                print("Welcome,",rec['Name'])

                while True:
                    print("\nMEMBER MENU")
                    print("1. View My Details")
                    print("2. View My Sponsor")
                    print("3. Add New Member Under Me")
                    print("4.Update  Member under me")
                    print("5.Delete Member under me")
                    print("6.Display Member under me")
                    print("7. Logout")

                    ch = int(input("Enter choice: "))

                    if ch == 1:
                        print("\nMember ID:", rec['MemberID'])
                        print("Name:", rec['Name'])
                        print("Sponsor ID:", rec['SponsorID'])
                    
                    elif ch == 2:
                        print("Your Sponsor ID:", rec['SponsorID'])

                    elif ch == 3:
                        addMemberUnderSponsor(rec['MemberID'])

                    elif ch == 4:
                        updateMemberUnderSponsor(rec['MemberID'])

                    elif ch == 5:
                        deleteMemberUnderSponsor(rec['MemberID'])

                    elif ch == 6:
                        displayMemberUnderMe(rec['MemberID'])

                    elif ch == 7:
                        f.close()
                        print("Logged out successfully")
                        return

        except EOFError:
            break

    f.close()
    print("Invalid Login Credentials")

#main menu                   

while True:
    
    print("\n MLM MANAGEMENT SYSTEM:")
    print("1.Add member")
    print("2.Display Members")
    print("3.Search Members")
    print("4.Update Sponsor")
    print("5.Delete Members")
    print("6.Member Login")
    print("10. Exit")

    ch =int(input("enter choice"))
    
    if ch == 1:
        insertMember()
    elif ch == 2:
        displayMembers()
    elif ch == 3:
        searchMembers()
    elif ch == 4:
        updateSponsor()
    elif ch ==5:
        deleteMember()
    elif ch ==6:
        memberLogin()
    elif ch ==10:
        break
    else:
        print("Invalid choice.")
