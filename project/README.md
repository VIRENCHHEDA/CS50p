# ATM SYSTEM
#### Video Demo: (https://youtu.be/jpjYiWtCjAY)
#### Description:
This is a project for CS50's Introduction to programming with Python in this project i have made a **ATM SYSTEM** it has a different **csv** file which contains a database including _username,Account Number,Pin,Balance_ which ideally a bank owns this data is then read by the **atm system** and the following functions are executed after the user authorization.The project has five different files in it the first one is named **project.py**

The file **project.py** contains the main code for the ATM SYSTEM it starts with importing **pandas** library to handle the data present in the **csv** file, the code first prompts the user to __Enter your account number__ if the account number does not match with the dataset present in the csv file the it prompts the user about the __wrong AC number__ and asks the user to __enter valid AC number__. If valid AC number is entered it passes to next function for __PIN AUTHORIZATION__. This **pin** function uses _while loop_ and _count_ is set to **3** for the number of incorrect attempts. After 3 incorrect attempts it exits the code. If the user enters the correct **PIN** the user is authorized to use all the other functions of the **ATM SYSTEM**. I have also used the __TRY EXCEPT__ to avoid the breaking of code if user enters alphabets for PIN number.

After the authorization takes place the user can access the all the other function in the __ATM SYSTEM__.

 "**choice**" function  is used so that the user can choose between different functionalities of the ATM system

- USER INPUTS '_1_' TO : CHECK BALANCE
- USER INPUTS '_2_' TO : DEPOSIT MONEY IN THE ACCOUNT
- USER INPUTS '_3_' TO : WITHDRAW MONEY FROM THE ACCOUNT
- USER INPUTS '_4_' TO : CHANGE THE CURRENT PIN OF THE ACCOUNT
- USER INPUTS '_5_' TO : EXIT FROM THE SYSTEM

__display_balance__ function is used to display the current balance of the authorized user this balance is fetched from the CSV file. '_balance:.2f_' is used so that it displays the balance upto 2 decimals.

__deposit__ function prompts the user for amount to be deposited and the amount is added to the current balance for the user and the user is prompted **DEPOSIT SUCCESFULL!** and the account balance after the deposited amount is shown

__withdraw__ function prompts the user for amount to be withdrawn from the user, it checks whether the amount is _greater than_ or _less than_ the current balance. If the requested withdrawal amount is less than the current balance than the amount is subtracted from the users current balance and than the new current balance is displayed to the user along with a "**WITHDRAWAL SUCCESFULL!**" message, If the requested amount is greater than the users current balance than it shows the message of "**Insufficient funds**" to the user

__change_pin__ function  prompts the user for _new pin_ once the user inputs a 4 digit pin the pin is changed and message of "**PIN CHANGED SUCCESSFULLY**" is shown on the screen.

This was the main code of the project the project contains some other files as well, one of which is "**atm.csv**" file it is basically a file containing the data for _username, Account Number, Pin, Balance_. It is the file which contains the database such file is usually a backend file present with the bank wherin they can access, edit, add any details from the file. Data from this file is used for all the functions in the code.

"**requirements.txt**" is also a file which contains the name of  python libraries used for wriring the program in __project.py__.


As testing is a crucial part of the project it helps to check all the functionalities of the functions and any errors or bugs  in the program can be easily recognized and corrected by writing unit tests. It also sets a bar for any changes made in the function should pass the tests for the changes to be approved and hence reduces the continous testing of the program


"__test_project.py__" is the final file for the ATM SYSTEM project it is used to write tests for the functions written in __project.py__,  facing lots of challenges to import complete database file "atm.csv" for testing the functions and failing to do so with many errors i settled here  by using "unittest.mock"  library in python  so that the functions can be tested using mock data, i was sucessful in testing for mock data(limited data), wherein testing of all the functions have been done on this mock data. In this mock data information regarding two individuals was tested

This being a simple project does not contain security features like a ideal bank would have but i would definately like to make the program better and add more functionalities making it more secure and more user friendly as i learn through new stuff in PYTHON





