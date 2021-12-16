import pickle
contact = dict()
def add_contact_fun():
    file = open('contactbook.txt', 'wb+')
    name = input("Enter Name : ").strip().upper()
    while True:
        if name == '':
            print("WARNING :Name Field Cannot be Empty.")
            print('-------------------------------------------------')
            name = input("Enter Name : ").strip().upper()
        else:
            break
    phn = input("Enter Phone Number : ")
    while True:
        if not phn.isdecimal():
            print('WARNING : Phone Number should contain only digit.')
            print('-------------------------------------------------')
            phn = input("Enter Phone Number : ")
            continue
        if phn[0] != '8' and phn[0] != '9':
            print('WARNING : Phone Number should begin with 8 or 9.')
            print('-------------------------------------------------')
            phn = input("Enter Phone Number : ")
            continue
        if len(phn) != 10:
            print('WARNING : Phone should contain of 10 Number.')
            print('-------------------------------------------------')
            phn = input("Enter Phone Number : ")
            continue
        else:
            break

    add = input('Enter Address : ')
    while True:
        if add == '':
            print("WARNING : Address Field Cannot be Empty.")
            print('-------------------------------------------------')
            add = input("Enter Address : ")
        else:
            break
    contact[name]={'phone':phn,'address':add}
    pickle.dump(contact, file)
    print('Note:- Contact Added Succesfully')
    file.close()

def search_contact_fun():
    with open('contactbook.txt','rb') as file:
        data = pickle.load(file)
        search = input('Enter Name for Searching:').strip().upper()
        if search in data:
            print('-------------------------------------------------')
            print(f'Phone No of {search} is :- ',end='')
            for k in data[search]['phone']:
                 print(k,end='')
            print('\t')
            print('And Address is :- ',end='')
            for v in data[search]['address']:
                 print(v,end='')
            print('\n')
            print('-------------------------------------------------')

        else:
            print('---------------------------------------')
            print(f'Sorry their no contact name {search}')
            print('---------------------------------------')

def display_contact_fun():
    with open('contactbook.txt','rb') as file:
        try:
            while True:
                d = []
                record = pickle.load(file)
                # for x,y in record.items():
                #     print(x,y)
                # for x in record.keys():
                #     print(x)

                for key,value in record.items():
                    temp = [key,value]
                    d.append(temp)
                print('-------------------------------------------------------------')
                print("{:<20} {:<20} {:<20}".format("Name","Phone Number","Address"))
                print('-------------------------------------------------------------')

                for i in range(len(d)):
                    print("{:<20} {:<20} {:<20}".format(d[i][0],d[i][1]['phone'],d[i][1]['address']))
                    print('_____________________________________________________________')
        except EOFError:
            print('All Contacts Displayed.')
    # file.close()


def modify_contact_fun():
    file1 = open('contactbook.txt','rb')
    file2 = open('temp.txt','wb')
    name_mod = input('Enter Name to Modify Number : ').strip().upper()
    try:
        while True:
            rec = pickle.load(file1)
            if name_mod in rec:
                print(f'Phone No of {name_mod} is :- ', end='')
                for k in rec[name_mod]['phone']:
                    print(k, end='')
                print('\n')
                mod_number = input('Enter Number to Modify : ')
                while True:
                    if not mod_number.isdecimal():
                        print('WARNING : Phone Number should contain only digit.')
                        print('-------------------------------------------------')
                        mod_number = input("Enter Phone Number : ")
                        continue
                    if mod_number[0] != '8' and mod_number[0] != '9':
                        print('WARNING : Phone Number should begin with 8 or 9.')
                        print('-------------------------------------------------')
                        mod_number = input("Enter Phone Number : ")
                        continue
                    if len(mod_number) != 10:
                        print('WARNING : Phone should contain of 10 Number.')
                        print('-------------------------------------------------')
                        mod_number = input("Enter Phone Number : ")
                        continue
                    else:
                        break
                rec[name_mod]['phone'] = mod_number
                print('Note:- Modified Successfully')
                pickle.dump(rec,file2)
            else:
                print('Note:- Contact not found')
    except:
        pass
    file1.close()
    file2.close()
    file1 = open('contactbook.txt','wb')
    file2 = open('temp.txt','rb')
    try:
        while True:
            rec = pickle.load(file2)
            pickle.dump(rec,file1)
    except:
        pass
    file1.close()
    file2.close()

def delete_contact_fun():
    file1 = open('contactbook.txt', 'rb')
    file2 = open('tempdel.txt', 'wb')
    name_del = input('Enter Name to Delete Records : ').strip().upper()
    try:
        while True:
            rec = pickle.load(file1)
            if name_del in rec:
                print('Phone No :- ', end='')
                for k in rec[name_del]['phone']:
                    print(k, end='')
                print('\t')
                print('And Address is :- ', end='')
                for v in rec[name_del]['address']:
                    print(v, end='')
                print('\n')
                print('Contact To Be Deleted')
                print('-------------------------------------------------')
                del rec[name_del]
                print('Deleted Successfully')
                print('-------------------------------------------------')

                pickle.dump(rec, file2)
            else:
                continue
    except:
        print('Record Not Found')
    file1.close()
    file2.close()



    file1 = open('contactbook.txt', 'wb')
    file2 = open('tempdel.txt', 'rb')
    try:
        while True:
            rec = pickle.load(file2)
            pickle.dump(rec, file1)
    except:
        pass
    file1.close()
    file2.close()







while True:
    choice=int(input('''\t\tContact Book
        --------------
        1.Add Contact
        2.Search Contact
        3.Display all Contact
        4.Modify Contact
        5.Delete Contact
        6.Exit :- '''))
    if choice == 1 :
        add_contact_fun()
    elif choice == 2:
        search_contact_fun()
    elif choice == 3:
        display_contact_fun()
    elif choice == 4:
        modify_contact_fun()
    elif choice == 5:
        delete_contact_fun()
    elif choice == 6:
        print('--------------------------------------------------')
        print("Thank You For Using Contact Book ~omkar barge")
        print('--------------------------------------------------')
        break
    else:
        print('--------------------------------------------------')
        print("Please choose valid Number.")
        print('--------------------------------------------------')

