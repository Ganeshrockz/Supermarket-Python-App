import csv
import os
def addItem():
    prodict={}
    print "\nAdd Item\n"
    itemid=input("Enter Item Id : ")
    fp=open('products.csv','r')
    a=csv.reader(fp)
    for product in a:
        val=int(product[0])
        if val==itemid:
            print "ItemId Already Exists!!!"
            return
    fp.close()
    itemName=raw_input("Enter Item Name : ")
    itemRate=input("Enter Rate :")
    fp=open('products.csv','a')
    prodict['ino']=itemid
    prodict['iname']=itemName
    prodict['irate']=itemRate
    a = csv.DictWriter(fp, prodict.keys())
    a.writerow(prodict)
    fp.close()



def searchItem():
    print "1.Search based on itemid"
    print "2.Search based on itemName"
    option=input("Enter option : ")
    fp=open('products.csv','r')
    a=csv.reader(fp)
    if option==1:
        itemId=input("Enter itemid : ")
        for product in a:
            val=int(product[0])
            if val==itemId:
                print "\n"
                print "ItemNo\tItemName\tItemrate\n"
                print product[0],"\t",product[1],"\t\t",product[2]
                fp.close()
                return
    elif option==2:
        itemName=raw_input("ENter ItemName : ")
        for product in a:
            val=product[1]
            itemName=itemName.lower()
            val=val.lower()
            if val==itemName:
                print "\n"
                print "ItemNo\tItemName\tItemrate\n"
                print product[0],"\t",product[1],"\t\t",product[2]
                fp.close()
                return
    print "\n"
    print "Item Not Found"
    fp.close()



def displayItem():
    print "\nItemsList\n"
    fp=open('products.csv','r')
    a=csv.reader(fp)
    print "ItemNo\tItemName\tItemrate\n"
    for product in a:
        print product[0],"\t",product[1],"\t\t",product[2]
    fp.close()



def removeItem():
    present=0
    print "\nItem List\n"
    displayItem()
    print "\n"
    print "1.Delete based on ItemNo"
    print "2.Delete based on ItemName"
    option=input("Enter an option : ")
    fp=open('products.csv','r')
    a=csv.reader(fp)
    fp2=open('dummy.csv','w')
    b=csv.writer(fp2)
    if option==1:
        print "\n"
        itemId=input("Enter Item Id : ")
        confirm=raw_input("Are you sure to delete(Y/N): ")
        confirm=confirm.lower()
        if confirm=='y':
            for product in a:
                val=int(product[0])
                if val!=itemId:
                    b.writerow(product)
                else:
                    present=1
        else:
            return
    elif option==2:
        print "\n"
        itemName=raw_input("Enter Item Name : ")
        confirm=raw_input("Are you sure to delete(Y/N): ")
        confirm=confirm.lower()
        if(confirm=='y'):
            for product in a:
                val=product[1].lower()
                itemName=itemName.lower()
                if itemName!=val:
                    b.writerow(product)
                else:
                    present=1
        else:
            return
    fp.close()
    fp2.close()
    fp=open('products.csv','w')
    a=csv.writer(fp)
    fp2=open('dummy.csv','r')
    b=csv.reader(fp2)
    for product in b:
        a.writerow(product)
    fp.close()
    fp2.close()
    if present==0:
        print "Item Not Found"
        return
    print "\n Item removed Successfully\n"



def updateItem():
    present=0
    displayItem()
    print "\n"
    print "1.Update the itemId"
    print "2.Update the itemName"
    print "3.Update the itemRate"
    print "\n"
    option=input("Enter Option : ")
    fp=open('products.csv','r')
    fp2=open('dummy.csv','w')
    a=csv.reader(fp)
    b=csv.writer(fp2)
    if option==1:
        oldId=input("Enter the old itemId : ")
        newId=input("Enter the new itemId : ")
        for product in a:
            val=int(product[0])
            if val==oldId:
                product[0]=newId
                present=1
            b.writerow(product)
    elif option==2:
        oldName=raw_input("Enter the old itemName : ")
        newName=raw_input("Enter the new ItemName : ")
        for product in a:
            val=product[1]
            if val==oldName:
                product[1]=newName
                present=1
            b.writerow(product)
    elif option==3:
        print "\n"
        print "1.Update rate based on itemId"
        print "2.Update rate based on itemName"
        print "\n"
        choice=input("Enter the option : ")
        if choice==1:
            itemId=input("Enter the itemId   : ")
            newRate=input("Enter the newrate : ")
            for product in a:
                val=int(product[0])
                if val==itemId:
                    product[2]=newRate
                    present=1
                b.writerow(product)
        else:
            itemName=raw_input("Enter the itemName : ")
            newRate=input("Enter the newrate : ")
            for product in a:
                val=product[1]
                if val==itemName:
                    product[2]=newRate
                    present=1
                b.writerow(product)
    fp.close()
    fp2.close()
    fp=open('products.csv','w')
    fp2=open('dummy.csv','r')
    a=csv.writer(fp)
    b=csv.reader(fp2)
    for product in b:
        a.writerow(product)
    fp.close()
    fp2.close()
    if present==0:
        print "Item Not Found"
        return



def purchaseItem():
    os.remove('purchaseList.csv')
    total=0
    while(1):
        fp=open('products.csv','r')
        a=csv.reader(fp)
        purchasedlist=[]
        displayItem()
        print "\n"
        purchaseItemNo=input("Enter Item Number(-1 to exit) : ")
        if purchaseItemNo==-1:
            break
        print "\n"
        for product in a:
            val=int(product[0])
            if val==purchaseItemNo:
                print "Item Name : ",product[1]
                print "Item Rate : ",product[2]
                break
        fp.close()
        print "\n"
        itemQuantity=input("Enter Item Quantity : ")
        rate=int(product[2])
        totalrate=rate*itemQuantity
        purchasedlist.append(product[0])
        purchasedlist.append(product[1])
        purchasedlist.append(product[2])
        purchasedlist.append(itemQuantity)
        purchasedlist.append(totalrate)
        fp2=open('purchaseList.csv','a')
        b = csv.writer(fp2)
        b.writerow(purchasedlist)
        fp2.close()
        total=total+totalrate
    print "\nSummary\n"
    print "ItemNo\tItemName\tRate\tQuantity\tTotal\n"
    fp2=open('purchaseList.csv','r')
    a=csv.reader(fp2)
    for product in a:
        print product[0],"\t",product[1],"\t\t",product[2],"\t",product[3],"\t\t",product[4],"\n"
    print "Grand Total : ",total
    print "\n        Thank You Visit Again"

# Main Program Starts here

while(1):
    print "\n"
    print "********************"
    print "* Choose an Option *"
    print "********************"
    print "\n"
    print "1.Add item"
    print "2.Remove item"
    print "3.Update values"
    print "4.Search Item"
    print "5.Display items"
    print "6.Purchase"
    print "7.Exit"
    print "\n"
    choice=input("Enter your option : ")
    if choice==1:
        addItem()
    elif choice==2:
        removeItem()
    elif choice==3:
        updateItem()
    elif choice==4:
        searchItem()
    elif choice==5:
        displayItem()
    elif choice==6:
        purchaseItem()
    elif choice==7:
        exit(0)
