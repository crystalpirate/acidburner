
# coding: utf-8

# In[1]:

#Version 0.1-5
#Written by Acidhttp://localhost:8889/notebooks/Python%20Scripts/AcidBurner.ipynb#
#Cannot calculate passwords above 4 places currently
#Will add multithreading and more password places
#Will also add different dictionaries to test.

import sys
import math
import string
import array
import timeit
from itertools import product
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        
        
        self.b = QtWidgets.QPushButton('Test Password', self)
        self.l1 = QtWidgets.QLabel(self)
        self.l = QtWidgets.QLabel(self)
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.b)
        h_box.addStretch()
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        self.setWindowTitle('ふぬしき---ふぬしき')
        self.setGeometry(500, 500, 300, 300)
        self.setFixedSize(300, 300)
        
        self.l.move(150, 200)
        self.l1.move(50, 200)
        
        self.btn = QtWidgets.QPushButton('Range', self)
        self.btn.move(10, 60)
        self.btn.clicked.connect(self.showDialog)
        
        self.btn1 = QtWidgets.QPushButton('Password', self)
        self.btn1.move(10, 20)
        self.btn1.clicked.connect(self.showPDialog)
        
        
        self.le2 = QtWidgets.QLineEdit(self)
        self.le2.move(10, 100)
        text = self.le2
        
        self.le = QtWidgets.QLineEdit(self)
        self.le.move(10, 100)
        text = self.le
        
        self.b.clicked.connect(self.btn_click)
        self.show()
     
    def showDialog(self):
        
        
        text, ok = QtWidgets.QInputDialog.getText(self, 'Max Characters to test? ', 'Enter Character Limit: ')
        
        if ok:
            self.le.setText(str(text))
     
    def showPDialog(self):
        
        text, ok = QtWidgets.QInputDialog.getText(self, 'Password', 'Please Enter Password: ')
        
        if ok:
            self.le2.setText(str(text))
        
        
        
    def btn_click(self):
        x = len(string.printable)
        i = 1;
        j = 1;
        
        test = int(self.le.text())
        
        password_length = test #int(input('Max Characters to check for: '))#check max password length to test for
        
        password = self.le2.text()#input('What is your password? ')#get input for password
        evilbook = []
        permutations = math.pow(x,password_length)
        print(permutations)

        start = timeit.default_timer()


        while(i <= password_length): #Use i to create all permutations
            if (permutations < 536870912): #permutations is less than max memory 
                evilbook = [''.join(i) for i in product(string.printable, repeat = i)] #evilbook list is filled with permutations of value i
    
    
            #if (permutations > 536870911): # if greater than max memory
                #j = permutations / 536870912 #find # of list needed
                #j = math.ceil(j) #round number of list needed up to whole number
                #while(j >= 0): #create each list
                #evilbook(j) = [''.join(i) for i in product(string.printable, repeat = i)]
         
            y = (len(evilbook) - 1) #since indexed at 0 subtract by 1
            while(y >= 0):
                p_test = evilbook[y]
                if (p_test == password): #if password == bruteforce then success!
                    self.l1.setText('Password Cracked: ') #print password cracked:
                    self.l.setText(p_test) #print password
                    y = -5; # end second while loop for checking each combination in current array
                    i = 10; #end first while loop for password size
                y -= 1;
            i += 1;
        if (i != 11):
            self.l1.setText('Could not Crack Password :( ')
        stop = timeit.default_timer()

        print('Run Time:')
        print(stop - start)
        
        
        

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



