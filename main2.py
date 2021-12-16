import pickle
import os

open('contactdairy.dat','ab+').close() #creats file if doesnt exist in system

with open('contactdairy.dat','rb') as datafile:
    if(os.path.getsize('contactdairy.dat')==0):
        contact = dict()
    else:
        contact = pickle.load(datafile)

    while True:
        try:
            choice = int(input('''
                                1.Add Contact
                                2.Search Contact
                                3.Display all Contact
                                4.Modify Contact
                                5.Delete Contact
                                6.Exit : '''))
        except:
            print('----------------------------------')
            print('Warning : Enter Valid Input')
            print('----------------------------------')
            # choice = ''

        if choice == 1:
            name = input('Enter Name : ').upper()
            while True:
                if name == '':
                    print('----------------------------------')
                    print('Warning : Name Field Cannot be empty!')
                    print('----------------------------------')
                    name = input('Enter Name : ').upper()
                else:
                    break
                if name in contact:
                    print('----------------------------------')
                    print('Alert : Contact Name Already Exists!\n')
                    print('----------------------------------')
                    continue
            address = input('Enter Address : ').strip()
            while True:
                if address == '':
                    print('----------------------------------')
                    print('Warning : Address Field Cannot be empty!')
                    print('----------------------------------')
                    address = input('Enter Address : ').upper()
                else:
                    break
            phone_no = input('Enter Contact Number : ').strip()
            while True:
                if not phone_no.isdecimal():
                    print('----------------------------------')
                    print('Warning : Phone Number should only contain digits!')
                    print('----------------------------------')
                    phone_no = input('Enter COntact Number : ').strip()
                    continue
                if phone_no[0] != '8' and phone_no[0] != '9':
                    print('----------------------------------')
                    print('Warning : Phone Number should begin with 8 or 9!')
                    print('----------------------------------')
                    phone_no = input('Enter Contact Number : ').strip()
                    continue
                if len(phone_no) != 10:
                    print('----------------------------------')
                    print('Warning : Phone Number Should be of 10 Digits!')
                    print('----------------------------------')
                    phone_no = input('Enter Contact Number : ').strip()
                    continue
                break
            contact[name] = {'Phone': phone_no, 'Address': address}
            with open('contactdairy.dat','wb') as f:
                pickle.dump(contact,f)
            print('----------------------------------')
            print('Note: Contact Added Succesfully.')
            print('----------------------------------')

        elif choice == 2:
            name = input('Enter Name : ').upper()
            if name in contact:
                print(name,':\nContact Number : ',contact[name]['Phone'],'\nAddress : ',contact[name]['Address'])
            else:
                print('----------------------------------')
                print("Friend Doesn't Exist!\n")
                print('----------------------------------')

        elif choice == 3:
            print('-----------------------------------------------')
            print("{:10} {:15} {:20}".format("Name","Contact No","Address"))            #String Format Method
            print('-----------------------------------------------')
            for key,item in contact.items():
                # print(key,item['Phone'],item['Address'])
                print("{:<10} {:<10} {:>10}".format(key,item['Phone'],item['Address']))
            print('-----------------------------------------------')

        elif choice == 4:
            name = input('Enter Name : ').upper()
            while True:
                if name == '':
                    print('----------------------------------')
                    print("Warning : Name cannot be empty!")
                    print('----------------------------------')
                    name = input('Enter Name : ').upper()
                else:
                    break
                if name not in contact:
                    print('----------------------------------')
                    print('Alert : Contact Doent Exist!')
                    print('----------------------------------')
                    continue
            new_contact = input('Enter New Contact to Update : ').strip()
            while True:
                if not new_contact.isdecimal():
                    print('----------------------------------')
                    print('Warning : Phone Number should only contain digits!')
                    print('----------------------------------')
                    new_contact = input('Enter Contact Number : ').strip()
                    continue
                if new_contact[0] != '8' and new_contact[0] != '9':
                    print('----------------------------------')
                    print('Warning : Phone Number should begin with 8 or 9!')
                    print('----------------------------------')
                    new_contact = input('Enter Contact Number : ').strip()
                    continue
                if len(new_contact) != 10:
                    print('----------------------------------')
                    print('Warning : Phone Number Should be of 10 Digits!')
                    print('----------------------------------')
                    new_contact = input('Enter Contact Number : ').strip()
                    continue
                break
            contact[name]['Phone'] = new_contact
            with open('contactdairy.dat','wb') as f:
                pickle.dump(contact,f)
            print('----------------------------------')
            print('Note: Contact Updated Succesfully.')
            print('----------------------------------')

        elif choice == 5:
            name = input('Enter Name to Delete Contact : ').upper()
            if name in contact:
                print('Deleted:- ',name,contact.pop(name))
                with open('contactdairy.dat','wb') as f:
                    pickle.dump(contact,f)
            else:
                print("Friend Doesn't Exist!")

        elif choice == 6:
            print('----------------------------------')
            print('Thanks For Using CONTACT BOOK')
            print('----------------------------------')
            break
        else:
            print('Invalid Choice!')
