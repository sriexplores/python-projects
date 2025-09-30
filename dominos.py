
#Dominos clone
import random
class Dominos:
    menu={"veg":{"margerita":129,"cheese_and_corn":169,"peppi_paneer":269,"veg_loaded":210,"tomato_tangi":170},
                 "non_veg":{"pepper_barbeque":199,"non_veg_loaded":169,"chicken_sausage":200},
                 "snacks":{"garlic_bread":120,"zingy":59,"chicken_cheese_balls":170},
                 "desserts":{"choco_lava":100,"mousse_cake":169},
                 "drinks":{"coke":90,"pepsi":78,"sprite":50}
        }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #to validate login state
        self.cart={} #to store orders

        #MAIN PROGRAM

        while True:
            if not self.login_status:
                print("----------WELCOME TO DOMINOS🍕🍕🍕  APP----------")
                print("Login")
                ch=input("Do you want to login? (y/n):").lower()
                if ch=='y':
                    self.login()
            if self.login_status:
                print("-------------------------------------------------------")
                print("User👤:",self.name)
                print("Enter 1:order")
                print("Enter 2:show cart")
                print("Enter 3:logout")
                choice=int(input("Enter choice:"))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice")
    
    @staticmethod
    def validate_otp(value):
        while True:
            og_otp=random.randint(1000,9999) 
            print(f"An otp has been sent to {value}")
            print(f"your dominos otp is:{og_otp}")
            otp=int(input("Enter otp:"))
            if otp==og_otp:
                print("login successful✔")
                return True
            print("Incorrect otp enter correct otp")

    def login(self):
        print("Enter 1: login with phone")
        print("Enter 2:login with email")
        ch=int(input("Enter your choice:"))
        if ch==1:
            #phone no. validation
            phno=int(input("Enter phno:"))
            if phno==self.phno:
                state=self.validate_otp(phno) #True
                self.login_status=state
            else:
                print("Incorrect phno")
        elif ch==2:
            #email validation
            email=input("Enter your email:")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:
                print("Incorrect email")
            
        else:
            print("Invalid choice")

    def order(self):
        print("-------DOMINOS MENU----------")
        for category in Dominos.menu: #display categories
            print(category)
        cat=input("Enter category:")
        if cat in Dominos.menu:
            d=Dominos.menu[cat]
            for item in d: #Display items of respective category
                print(item,'           Rs.',d[item])
            item=input("Enter item:")
            if item in d:
                q= int(input("enter quantity:"))
                if item in self.cart:    
                    self.cart[item]+=d[item]*q#var[key]=new val
                else:
                    self.cart[item]=d[item]*q                
                print(f"{item} added to cart🛒")
            else:
                print(f"{cat} is not available❌")
        else:
            print(f'{cat} is not available❌')

    def show_cart(self):
        if self.cart!={}:
            print("--------------Dominos cart 🛒-------------")
            total=0
            for item in self.cart:
                print(item,"------------- Rs",self.cart[item])
                total+=self.cart[item]
            print("total bill: Rs",total)  
        else:
            print("cart is empty please order")
        if self.cart!={}:
            ch=input("Do you want place order? (y/n):").lower()
            if ch=='y':
                print("Thank you for placing the order..")
                print("Your order is on the way🏍")
                self.cart={}

    def logout(self):
        ch=input("Do you want to logout? (y/n):").lower()
        if ch=='y':
            self.login_status=False
            print("logged out!✔")


ob=Dominos("Thaniya","sri@gmail.com",9876543211)









































