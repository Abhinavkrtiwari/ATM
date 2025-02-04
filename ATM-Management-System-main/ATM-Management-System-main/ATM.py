import datetime
import sys
import time as t
import random
user_balance = 0
user_name="Avinash Dhanuka"
user_pin="7319"
print("\n\n\n\n -------- \033[1m\033[93m WELCOME    TO    PUNJAB    NATIONAL    BANK  \033[0m\033[0m  --------")
print("\nPress \033[91m 1 \033[0m for NEXT Option.")
list=[]
n=int(input())
if(n==1):
    print("Please SELECT Langauge:","\033[95m 1.\033[0m ENGLISH",sep="\n")
    x=int(input())
    if(x==1):
        num_of_tries = 3
        while (num_of_tries!=0):
            check_pin=int(input("Please Enter Your \033[93m 4 Digit PIN\033[0m :  "))
            check_pin=str(check_pin)
            user_pin=str(user_pin)
            if(check_pin==user_pin):
                print("Please Wait...\n")
                t.sleep(1)
                print("ACCOUNT AUTHORISED!!\n")
                t.sleep(1)
                while True:
                    t.sleep(0.25)
                    print("\n\t\t  You Have Selected English Langauge.")
                    print("\n\t\t  \033[91m 1.\033[0m BALANCE ENQUIRY","                            \033[91m 2.\033[0m CASH WITHDRAWAL")
                    print("\t\t  \033[91m 3.\033[0m DEPOSIT","                                    \033[91m 4.\033[0m TRANSFER")
                    print("\t\t  \033[91m 5.\033[0m PIN CHANGE","                                 \033[91m 6.\033[0m MINI STATEMENT")
                    print("\t\t                                  \033[91m 0.\033[0m EXIT")
                    Facility=int(input("\tPlease SELECT ANY Above Facility to Avail:"))
                    if(Facility==1):
                        print("You Have Choosen to "  '\033[94m''\033[4m''\033[1m' + 'CHECK BALANCE' + '\033[0m''\033[0m''\033[0m',"of Your ACCOUNT")
                        t.sleep(0.25)
                        print("Fetching Details!  Please Wait....")
                        t.sleep(1)
                        print("Your \033[96m CURRENT   ACCOUNT   BALANCE \033[0m is", user_balance)
                        t.sleep(1)
                        continue
                    elif(Facility==2):
                        t.sleep(0.5)
                        print("You Have Choosen ", '\033[94m''\033[4m''\033[1m' + 'CASH WIITHDRAWAL' + '\033[0m''\033[0m''\033[0m',"from Your ACCOUNT",end="\n\n")
                        print("\t\t\tOR","\n\tPress \033[91m 0 \033[0m to CANCEL CASH WITHDRAWAL\n\n",sep="\n")
                        t.sleep(0.5)
                        print("---   AVAILABLE CASH DENOMINATIONS AVAILABLE   ---")
                        print("\033[91m 1.\033[0m  100","                                \033[91m 2.\033[0m  500")
                        print("\033[91m 3.\033[0m  2000","                               \033[91m 0.\033[0m  CANCEL CASH WITHDRAWAL")
                        denominations=int(input("  Please SELECT the DENOMINATIONS required:  "))
                        if(denominations==1):
                            withdrawl_amount=int(input("  Enter a AMOUNT TO WITHDRWAW :  "))
                            if(withdrawl_amount%100==0 and withdrawl_amount<=user_balance):
                                a=random.randint(1,100)
                                b=random.randint(1,100)
                                print("--- Enter a Number Between",a,"and",b,"---")
                                print("Press \033[91m 0 \033[0m to Cancel CASH WITHDRAWL Transfer")
                                Authentication=int(input("Please Enter a Number Between the Given Range: "))
                                if(a<b):
                                    if(Authentication>a and Authentication<b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        t.sleep(1)
                                        print("\tYou Are Not Authorized !!")
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(a>b):
                                    if(Authentication<a and Authentication>b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        print("  Please wait a while !!  ")
                                        t.sleep(0.5)
                                        print("\tYou Are Not Authorized !!")
                                        t.sleep(0.5)
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(Authentication==0):
                                    print("Cancelling IMT Transfer !!")
                                    t.sleep(1)
                                    print("---  You have Been Exited Successfully  ---")
                                    t.sleep(0.5)
                                    continue
                            elif(withdrawl_amount%100!=0):
                                print("  Processing the request !! Please Wait ....")
                                t.sleep(0.5)
                                print("...  Please Entered Amount in Hundreds  ....")
                                t.sleep(0.5)
                                continue
                            elif(withdrawl_amount>user_balance):
                                print(" \t\t... Please Wait ...")
                                t.sleep(0.5)
                                print("  \t\tYour Account Doesn't Have Sufficient Cash  !!!")
                                t.sleep(0.5)
                                continue
                        elif(denominations==2):
                            withdrawl_amount=int(input("  Enter a AMOUNT TO WITHDRWAW :  "))
                            if(withdrawl_amount%500==0 and withdrawl_amount<=user_balance):
                                a=random.randint(1,100)
                                b=random.randint(1,100)
                                print("--- Enter a Number Between",a,"and",b,"---")
                                print("Press \033[91m 0 \033[0m to Cancel CASH WITHDRAWL Transfer")
                                Authentication=int(input("Please Enter a Number Between the Given Range: "))
                                if(a<b):
                                    if(Authentication>a and Authentication<b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        t.sleep(0.5)
                                        print("\tYou Are Not Authorized !!")
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(a>b):
                                    if(Authentication<a and Authentication>b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        t.sleep(0.5)
                                        print("\tYou Are Not Authorized !!")
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(Authentication==0):
                                    print("Cancelling IMT Transfer !!")
                                    t.sleep(0.5)
                                    print("---  You have Been Exited Successfully  ---")
                                    t.sleep(0.5)
                                    continue
                            elif(withdrawl_amount%500!=0):
                                print("... Please Wait !!!")
                                t.sleep(0.5)
                                print("... Please Entered Amount in Hundreds ....")
                                t.sleep(0.5)
                                continue
                            elif(withdrawl_amount>user_balance):
                                print("  \t\tProcessing Your Wait  !!!      Please Wait ...")
                                t.sleep(1)
                                print("  \t\tYour Account Doesn't Have Sufficient Cash  !!!")
                                t.sleep(0.5)
                                continue
                        elif(denominations==3):
                            withdrawl_amount=int(input("  Enter a AMOUNT TO WITHDRWAW :  "))
                            if(withdrawl_amount%2000==0 and withdrawl_amount<=user_balance):
                                a=random.randint(1,100)
                                b=random.randint(1,100)
                                print("--- Enter a Number Between",a,"and",b,"---")
                                print("Press \033[91m 0 \033[0m to Cancel CASH WITHDRAWL Transfer")
                                Authentication=int(input("Please Enter a Number Between the Given Range: "))
                                if(a<b):
                                    if(Authentication>a and Authentication<b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        t.sleep(0.5)
                                        print("\tYou Are Not Authorized !!")
                                        t.sleep(0.25)
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(a>b):
                                    if(Authentication<a and Authentication>b):
                                        t.sleep(0.5)
                                        print("\tPlease Wait....")
                                        user_balance-=withdrawl_amount
                                        now = datetime.datetime.now()
                                        today = datetime.date.today()
                                        current_day = today.strftime("%d/%m/%Y")
                                        current_time = now.strftime("%H:%M:%S")
                                        CashWithDrawl_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Withdrawn: ", withdrawl_amount,"Current Balance: ",user_balance]
                                        list.append(CashWithDrawl_Statement)
                                        t.sleep(0.5)
                                        print("---   Your ACCOUNT is DEBITED By",withdrawl_amount," ---")
                                        t.sleep(0.5)
                                        print("---   Your CURRENT BALANCE is",user_balance," ---")
                                        t.sleep(0.5)
                                        continue
                                    else:
                                        t.sleep(0.5)
                                        print("\tYou Are Not Authorized !!")
                                        t.sleep(0.25)
                                        print("---   Exiting From Cash WithDrawal   ----")
                                        t.sleep(0.5)
                                elif(Authentication==0):
                                    print("Cancelling IMT Transfer !!")
                                    t.sleep(0.5)
                                    print("---  You have Been Exited Successfully  ---")
                                    t.sleep(0.5)
                                    continue
                            elif(withdrawl_amount%100!=0):
                                print("    Please   wait   a   while !!!  ")
                                t.sleep(0.5)
                                print("... Please Entered Amount in Hundreds ....")
                                t.sleep(0.5)
                                continue
                            elif(withdrawl_amount>user_balance):
                                print(" \t\t... Please Wait ...")
                                t.sleep(1)
                                print("  \t\tYour Account Doesn't Have Sufficient Cash  !!!")
                                t.sleep(0.5)
                                continue
                        elif(denominations==0):
                            t.sleep(0.5)
                            print("   Please wait a While  ...")
                            print("--- Exited from Cash WithDrawl  ----")
                            t.sleep(0.5)
                            continue
                        else:
                            print("Please Wait ........")
                            t.sleep(0.5)
                            print("You Haven't Selected Valid Denominations !!")
                            t.sleep(1)
                            print("---  Exiting From CashWithDrawl  ---")
                            t.sleep(0.5)
                            continue
                    elif(Facility==3):
                        print("------   You Have Choosen to "  '\033[94m''\033[4m''\033[1m' + 'DEPOSIT' + '\033[0m''\033[0m''\033[0m  -----------')
                        print("OR Press \033[91m 0 \033[0m to CANCEL")
                        t.sleep(0.5)
                        amount=int(input("Please Enter the" '\033[94m' + ' AMOUNT ' + '\033[0m' "to" '\033[94m' + ' DEPOSIT ' + '\033[0m' "in the"'\033[94m' + ' ACCOUNT' + '\033[0m' ":"))
                        if(amount==0):
                            print("Exiting !!!    Please  Wait ......")
                            t.sleep(1.25)
                            print("---You HAVE " '\033[94m''\033[4m''\033[1m' + 'EXITED from DEPOSIT' + '\033[0m''\033[0m''\033[0m' "---")
                            t.sleep(0.5)
                            continue
                        else:
                            t.sleep(1)
                            user_balance+=amount
                            now = datetime.datetime.now()
                            today = datetime.date.today()
                            current_day = today.strftime("%d/%m/%Y")
                            current_time = now.strftime("%H:%M:%S")
                            Deposit_Statement=["Date: ",current_day,"Time: ",current_time, "Amount Deposite: ", amount,"Current Balance: ",user_balance]
                            list.append(Deposit_Statement)
                            t.sleep(0.5)
                            print("Please Wait !!! Processing Your Request ----")
                            t.sleep(0.5)
                            print(amount," is",'\033[94m' + ' successfully ' + '\033[0m',"added in your account")
                            t.sleep(0.5)
                            print("Your \033[93m CURRENT ACCOUNT BALANCE \033[0m is",user_balance)
                            t.sleep(0.5)
                            continue
                    elif(Facility==4):
                        print("You Have Choosen to "  '\033[94m''\033[4m''\033[1m' + 'TRANSFER' + '\033[0m''\033[0m''\033[0m')
                        print("Please SELECT the Required Transfer Option:  ")
                        print("\033[91m 1.\033[0m ACCOUNT BASED TRANSFER","                     \033[91m 2.\033[0m IMT")
                        print("\033[91m 3.\033[0m CARD TO CARD FUND TRANSFER","                 \033[91m 0.\033[0m CANCEL TRANSFER")
                        transfer_option=int(input("SELECT THE REQUIRED TRANSFER OPTION: "))
                        if(transfer_option==1):
                            t.sleep(0.25)
                            print("-------You Have Selected ACCOUNT BASED TRANSFER-------")
                            transfer_amount=int(input("Please ENTER the AMOUNT which is to be TRANSFERRED: "))
                            if(transfer_amount>user_balance):
                                print("Please Wait !!!")
                                t.sleep(0.5)
                                print("Your ACCOUNT haven't SUFFICIENT BALANCE to Transfer.")
                                t.sleep(0.5)
                                continue
                            elif(transfer_amount==0):
                                print("-- Prcessing Your Request !!  Please  Wait .....")
                                t.sleep(0.5)
                                print("-- You Have EXITED from  ACCOUNT BASED TRANSFER --")
                                t.sleep(0.5)
                                continue
                            else:
                                t.sleep(0.25)
                                transfer_acc=int(input("Please ENTER the \033[93m 12-DIGIT ACCOUNT NUMBER \033[0m of Reciever: "))
                                user_balance=user_balance-transfer_amount
                                now = datetime.datetime.now()
                                today = datetime.date.today()
                                current_day = today.strftime("%d/%m/%Y")
                                current_time = now.strftime("%H:%M:%S")
                                Account_Transfer_Statement=["Date: ",current_day,"Time: ",current_time, "ACCOUNT Transfer Amount : ", transfer_amount,"Current Balance: ",user_balance]
                                list.append(Account_Transfer_Statement)
                                t.sleep(0.3)
                                print("----  Please  Wait   !!!\n")
                                t.sleep(0.5)
                                print(transfer_amount," \033[96m is Sucessfuully Transferred to the Account \033[0m --",transfer_acc)
                                t.sleep(1)
                                print("The \033[96m REMAINING BALANCE \033[0m of your ACCOUNT is ",user_balance)
                                t.sleep(0.5)
                                continue
                        elif(transfer_option==2):
                            print("--- You Have Selected IMT Transfer Option ---")
                            print("\033[91m 1.\033[0m INITIATE IMT","                          \033[91m 0.\033[0m EXIT IMT TRANSFER")
                            IMT_option=int(input("Please Select the Desired Option: "))
                            if(IMT_option==1):
                                print("-- You Have Selected INITIATE IMT Option --")
                                Benificiary_number=str(input("---  Enter BENIFICIARY Mobile Number  ---"))
                                First_Benificiary_number=Benificiary_number[0]
                                check_number=["0","1","2","3","4","5"]
                                if(len(Benificiary_number)==10 and First_Benificiary_number not in check_number):
                                    Mobile_number=str(input("---  Enter Your Mobile Number  ---"))
                                    First_Mobile_number=Mobile_number[0]
                                    if(len(Mobile_number)==10 and First_Mobile_number not in check_number):
                                        IMT_Pin=str(input("---  Create Your IMT PIN  ---"))
                                        if(len(IMT_Pin)==4):
                                            check_IMT_Pin=str(input("---  Re-Enter Your IMT PIN  ---"))
                                            if(check_IMT_Pin==IMT_Pin):
                                                IMT_Amount=int(input("---  Enter Amount to Transfer through IMT  ---"))
                                                if(IMT_Amount>=100 and IMT_Amount<=10000 and IMT_Amount<=(user_balance-25)):
                                                    t.sleep(0.5)
                                                    print("---   Please Confirm Your IMT Details   ---")
                                                    print("Benificiary Number:  ",Benificiary_number)
                                                    print("Mobile Number     :  ",Mobile_number)
                                                    print("IMT PIN           :  ",IMT_Pin)
                                                    print("IMT AMOUNT        :  ","Rs",IMT_Amount)
                                                    print("Commission Fees   :  ","Rs 25")
                                                    print("----------------------------------------")
                                                    a=random.randint(1,100)
                                                    b=random.randint(1,100)
                                                    print("--- Enter a Number Between",a,"and",b,"---")
                                                    print("Press \033[91m 0 \033[0m to Cancel IMT Transfer")
                                                    Authentication=int(input("Please Enter a Number Between the Given Range: "))
                                                    if(a<b):
                                                        if(Authentication>a and Authentication<b):
                                                            t.sleep(0.5)
                                                            print("Your IMT have been Created Successfully !!!")
                                                            user_balance=user_balance-(IMT_Amount+25)
                                                            now = datetime.datetime.now()
                                                            today = datetime.date.today()
                                                            current_day = today.strftime("%d/%m/%Y")
                                                            current_time = now.strftime("%H:%M:%S")
                                                            IMT_Statement=["Date: ",current_day,"Time: ",current_time, "IMT Amount Transfered: ", IMT_Amount,"Current Balance: ",user_balance]
                                                            list.append(IMT_Statement)
                                                            IMT_valid_day=today + datetime.timedelta(days=2)
                                                            IMT_ID=random.randint(1000,9999)
                                                            IMT_ID=str(IMT_ID)
                                                            IMT_ID = "00100100000"+IMT_ID
                                                            t.sleep(0.25)
                                                            print("\t\t..................Please Wait..............")
                                                            print("\t\t..............Generating Your IMT..........\n")
                                                            t.sleep(1)
                                                            print("----------------------------------------------------------------------------------------------------------------------------------------")
                                                            print("\nYou have sent an IMT of",IMT_Amount,"to beneficiary",Benificiary_number,"Valid upto",IMT_valid_day,". IMT ID",IMT_ID,", Withdrawable at any State Bank ATM.")
                                                            print("\n--------------------------------------------------------------------------------------------------------------------------------------")
                                                            continue
                                                        else:
                                                            t.sleep(0.5)
                                                            print("\tYou Are Not Authorized !!")
                                                            t.sleep(0.25)
                                                            print("---   Exiting From IMT   ----")
                                                            t.sleep(0.5)
                                                            continue
                                                    elif(a>b):
                                                        if(Authentication<a and Authentication>b):
                                                            t.sleep(0.5)
                                                            print("Your IMT have been Created Successfully !!!")
                                                            user_balance=user_balance-(IMT_Amount+25)
                                                            now = datetime.datetime.now()
                                                            today = datetime.date.today()
                                                            current_day = today.strftime("%d/%m/%Y")
                                                            current_time = now.strftime("%H:%M:%S")
                                                            IMT_Statement=["Date: ",current_day,"Time: ",current_time, "IMT Amount Transfered: ", IMT_Amount,"Current Balance: ",user_balance]
                                                            list.append(IMT_Statement)
                                                            IMT_valid_day=today + datetime.timedelta(days=2)
                                                            IMT_ID=random.randint(1000,9999)
                                                            IMT_ID=str(IMT_ID)
                                                            IMT_ID = "00100100000"+IMT_ID
                                                            t.sleep(0.25)
                                                            print("\t\t..................Please Wait..............")
                                                            print("\t\t..............Generating Your IMT..........\n")
                                                            t.sleep(1)
                                                            print("----------------------------------------------------------------------------------------------------------------------------------------")
                                                            print("\nYou have sent an IMT of",IMT_Amount,"to beneficiary",Benificiary_number,"Valid upto",IMT_valid_day,". IMT ID",IMT_ID,", Withdrawable at any State Bank ATM.")
                                                            print("\n--------------------------------------------------------------------------------------------------------------------------------------")
                                                            continue
                                                        else:
                                                            t.sleep(0.5)
                                                            print("\tYou Are Not Authorized !!")
                                                            t.sleep(0.25)
                                                            print("---   Exiting From IMT   ----")
                                                            t.sleep(0.5)
                                                            continue
                                                    elif(Authentication==0):
                                                        print("Cancelling IMT Transfer !!")
                                                        t.sleep(0.5)
                                                        print("---  You have Been Exited Successfully  ---")
                                                        t.sleep(0.5)
                                                        continue
                                                elif(IMT_Amount>=100 and IMT_Amount<=10000 and IMT_Amount>(user_balance-25)):
                                                    print("--  Please wait a While  --")
                                                    t.sleep(0.5)
                                                    print("Your Account Doesn,t Have Appropriate Balance !!")
                                                    t.sleep(0.5)
                                                    print("Exiting from IMT Transfer !!!")
                                                    t.sleep(1)
                                                    print("---  You have Been Exited Successfully  ---")
                                                    t.sleep(0.5)
                                                    continue
                                                else:
                                                    print("You Haven,t Correct Range of AMOUNT")
                                                    t.sleep(0.5)
                                            else:
                                                print("You IMT PIN Re-Entered Doesn't Matched !!")  
                                                t.sleep(0.5)  
                                        else:
                                            print("Emter a Valid IMT PIN")
                                            t.sleep(0.5)
                                    else:
                                         print("Please Enter your Valid Mobile Number !!")
                                         t.sleep(0.5)
                                else:
                                    print("Please Enter a valid Benificiary Number !!")
                                    t.sleep(0.5)
                            elif(IMT_option==0):
                                print("\tPlease Wait a While ....")
                                t.sleep(0.5)
                                print("---  Exiting from IMT Services  ---")
                                t.sleep(0.5)
                                continue
                            else:
                                print("---  You Haven't Enter Any Valid Option  ---")
                                t.sleep(0.5)
                                continue
                        elif(transfer_option==3):
                            print("--- You Have Selected CARD to CARD FUND Transfer Option ---")
                            Card_Reciever=str(input("  Enter \033[93m 16-Digit Card Number \033[0m of Reciever:   "))
                            if(len(Card_Reciever)==16):
                                Check_Card_Reciever=str(input(" Please Re-Enter 16-Digit Card Number of Reciever:  "))    
                                if(Check_Card_Reciever==Card_Reciever):
                                    Card_Amount_Transfer=int(input("Enter the AMOUNT to Transfer:  "))
                                    if(Card_Amount_Transfer<user_balance):
                                        a=random.randint(1,100)
                                        b=random.randint(1,100)
                                        print("--- Enter a Number Between",a,"and",b,"---")
                                        print("Press \033[91m 0 \033[0m to Cancel CARD to CARD Fund Transfer")
                                        Authentication=int(input("Please Enter a Number Between the Given Range: "))
                                        if(a<b):
                                            if(Authentication>a and Authentication<b):
                                                t.sleep(0.5)
                                                print("....... Please Wait .......")
                                                t.sleep(1.5)
                                                print("Your CARD to CARD Fund have been \033[91m Transfered Sucessfully \033[0m !!!")
                                                user_balance=user_balance-(Card_Amount_Transfer)
                                                now = datetime.datetime.now()
                                                today = datetime.date.today()
                                                current_day = today.strftime("%d/%m/%Y")
                                                current_time = now.strftime("%H:%M:%S")
                                                CARD_Statement=["Date: ",current_day,"Time: ",current_time, "CARD to CARD Fund Transfered: ", Card_Amount_Transfer,"Current Balance: ",user_balance]
                                                list.append(CARD_Statement)
                                                continue
                                            else:
                                                t.sleep(0.5)
                                                print("\tYou are UnAuthorized !!!")
                                                t.sleep(0.25)
                                                print("---  Exiting From CARD to CARD Fund Transfer  ---")
                                                t.sleep(0.5)
                                                continue
                                        elif(a>b):
                                            if(Authentication<a and Authentication>b):
                                                t.sleep(0.5)
                                                print("....... Please Wait .......")
                                                t.sleep(1)
                                                print("Your \033[96m CARD TO CARD FUND \033[0m have been \033[96m Transfered Sucessfully \033[0m !!!")
                                                user_balance=user_balance-(Card_Amount_Transfer)
                                                now = datetime.datetime.now()
                                                today = datetime.date.today()
                                                current_day = today.strftime("%d/%m/%Y")
                                                current_time = now.strftime("%H:%M:%S")
                                                CARD_Statement=["Date: ",current_day,"Time: ",current_time, "CARD to CARD Fund Transfered: ", Card_Amount_Transfer,"Current Balance: ",user_balance]
                                                list.append(CARD_Statement)
                                                continue
                                            else:
                                                t.sleep(0.5)
                                                print("\tYou are UnAuthorized !!!")
                                                t.sleep(0.25)
                                                print("---  Exiting From CARD to CARD Fund Transfer  ---")
                                                t.sleep(0.5)
                                                continue
                                        elif(Authentication==0):
                                            print("Cancelling \033[91m  IMT  Transfer  \033[0m !!")
                                            t.sleep(0.5)
                                            print("---  You have Been Exited Successfully  ---")
                                            t.sleep(0.5)
                                            continue
                                    else:
                                        print("You Haven't Authenticate Your Self Correctly !!")
                                        t.sleep(0.5)
                                        print("---  You are Denied from CARD to CARD Fund Transfer  ---")
                                        t.sleep(1)
                                        continue 
                                else:
                                    print("Please Wait.......")
                                    t.sleep(0.5)
                                    print("---  Card Number Doesn't Match  ---")
                                    t.sleep(1)
                                    print("---  Exiting from CARD to CARD Fund Transfer  ---")
                                    continue 
                            else:
                                print("Please Wait.......")
                                t.sleep(0.5)
                                print("You Haven't Enter Valid Card Number !!")
                                t.sleep(0.25)
                                print("---  Exiting from CARD to CARD Fund Transfer  ---")
                                t.sleep(0.5)
                                continue
                        elif(transfer_option==0):
                            print("Processing Your Request !!  Please Wait....")
                            t.sleep(0.5)
                            print("---------- You HAVE EXITED FROM TRANSFER FACILITY ----------")
                            continue
                    elif(Facility==5):
                        print("You Have Choosen to "  '\033[94m''\033[4m''\033[1m' + 'CHANGE YOUR PIN' + '\033[0m''\033[0m''\033[0m')
                        confirm_pin=str(input("Please ENTER " '\033[94m''\033[4m''\033[1m' + 'OLD PIN: ' + '\033[0m''\033[0m''\033[0m'))
                        if(confirm_pin==user_pin):
                            t.sleep(0.5)
                            print("--- YOU ARE AUTHORISED TO CHANGE PIN ---")
                            new_pin=input("Please ENTER the \033[93m NEW 4-Digit PIN \033[0m : ")
                            if new_pin.isnumeric()==True and len(new_pin)==4:
                                user_pin=new_pin
                                t.sleep(0.5)
                                print("---YOUR \033[96m NEW 4-Digit PIN \033[0m is ",user_pin,"---")
                                t.sleep(0.5)
                                continue
                            else:
                                t.sleep(1)
                                print("You Haven't Enter Valid PIN to CHANGE",end="\n\n")
                                break
                        else:
                            t.sleep(0.5)
                            print("--- The OLD PIN Entered is InCorrect ---","--- ACCESS TO CHANGE PIN IS DENIED BY THE BANK ---",sep="\n",end="\n\n")
                            t.sleep(0.5)
                            break
                    elif(Facility==6):
                        t.sleep(0.25)
                        print("--- You Have Choose to Show "  '\033[94m''\033[4m''\033[1m' + 'MINI STATEMENT' + '\033[0m''\033[0m''\033[0m' "of your ACCOUNT ---")
                        t.sleep(0.25)
                        print("---- Generating Your MINI Statement !!   Please Wait ----")
                        t.sleep(1)
                        print('\n'.join(map(str, list)))
                        t.sleep(0.5)

                    elif(Facility==0):
                        t.sleep(1)
                        print("\t---------- You HAVE EXITED ----------","\t--- THANK YOU FOR USING PNB BANK ---",sep="\n")
                        sys.exit(Facility==0)
                    else:
                        t.sleep(0.5)
                        print("\t---  You Haven't Selected ANY Facility ---")
                        t.sleep(0.75)
                        print("\t---   Please Select Mentioned Facility  ---")
                        t.sleep(1)
                        continue
            else:
                num_of_tries-=1 
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n\n")
                if(num_of_tries==0):
                    print("! ! !     \033[94m ACCESS   DENIED \033[0m     ! ! !",sep="\n")   
                    print("----  Exiting  from  PNB  ATM  ----")
                    t.sleep(2)
                    print("\033[91m -------   YOU   ARE   UNAUTHORISED    ------- \033[0m")
    else:
        t.sleep(0.25)
        print("You Haven't Selected ANY Language.")
else:
    t.sleep(0.25)
    print("You Have Not Selected a Valid Option.")