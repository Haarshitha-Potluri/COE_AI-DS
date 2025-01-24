import streamlit as st


class Bank:
    balance = 50000

    def deposit(self):

        amount = st.number_input("Enter amount to deposit:", key="deposit_amount", min_value=0)

        if amount < 100 or amount > 50000:

            st.title("Minimum deposit is 100 and Maximum deposit is 50000")

        elif amount % 100 == 0:

            self.balance += amount

            st.title(f"{amount} is deposited")

            obj.bal_enquiry()

            st.title("************Transaction successful*********")

        else:

            st.title("Amount should be in multiples of 100")

    def withdraw(self):

        amount = st.number_input("Enter amount to withdraw:", key="withdraw_amount", min_value=0)

        min_bal = 500

        minacc = self.balance - min_bal

        if amount < 100 or amount > minacc:

            st.title(

                f"Minimum withdrawal is 100 and Maximum withdrawal is {minacc} as there should be a minimum balance "

                f"of 500 in your account")

        elif amount % 100 == 0:

            self.balance -= amount

            st.title(f"{amount} is withdrawn")

            obj.bal_enquiry()

            st.title("************Transaction successful*********")

        else:

            st.title("Amount should be in multiples of 100")

    def bal_enquiry(self):

        st.title(f"Balance: {self.balance}")

    def viewoptions(self):

        transac = 3

        while transac > 0:

            st.title("----------------Transaction---------------------")

            st.title("1. Deposit:")

            st.title("2. Withdraw:")

            st.title("3. Balance Enquiry:")

            st.title("4. Exit")

            op = st.number_input("Choose option", key=f"transaction_option_{transac}", min_value=0)

            if op == 1:

                obj.deposit()

            elif op == 2:

                obj.withdraw()

            elif op == 3:

                obj.bal_enquiry()

            elif op == 4:

                exit()

            else:

                st.title("Invalid option .....")

            transac -= 1

    def validate(self):

        chance = 1

        while chance > 0:

            pin = st.number_input("Enter your pin:", key=f"pin_input_{chance}", min_value=0)

            actual_pin = 1234

            if pin == actual_pin:

                obj.viewoptions()

                break

            else:

                if chance == 1:

                    st.title("Your card is blocked...")

                else:

                    st.title("Incorrect pin, try again...")

            chance -= 1


obj = Bank()

obj.validate()
