import sqlite3 as sql
from string import punctuation as pun
from time import sleep
from sys import exit as ex

dataType = ["BOOLEAN"," VARCHAR","CHAR","INTEGER","FLOAT","TIME","DATE"]
         
def joinDatabase(temp):
    while True:
        if temp == "create":
            userIn = input("Enter a name of the database: ").strip()
        elif temp == "table":
            userIn = input("Enter a name of the table: ").strip()
        if " " in list(userIn):
            print("You cannot use spaces")
        elif userIn in [""," "]:
            print("Sorry that is not a valid name for the database")
        elif not any(i in userIn for i in pun):
            break
        else:
            print("Sorry you cant use punctuation")
    if temp == "create":
        userIn = "{dbName}.db".format(dbName = userIn)
    return userIn


def booleanRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        isNull = True
        while isNull:
            notNull = input("Would you like the row to be \"Not Null\"? (Y/N): ").upper()
            if notNull == "Y":
                formatCommand ='''{iden} BOOLEAN NOT NULL,
'''.format(iden= rowName)
                isNull = False
            elif notNull == "N":
                formatCommand = '''{iden} BOOLEAN,
'''.format(iden= rowName)
                isNull = False
            else:
                print("Sorry Y/N only!")
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def integerRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        formatCommand = '''{iden} INTEGER,
'''.format(iden= rowName)
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def dateTimeRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        formatCommand = '''{iden} DATETIME,
'''.format(iden= rowName)
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def charRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        validAmount = False
        while validAmount == False:
            try:
                charAmount = int(input("How many characters: "))
                if charAmount > 0:
                    validAmount = True
                else:
                    print("Sorry the amount of characters is not valid, try again")
            except Exception as e:
                print("Sorry that is not a valid number, try again.")
        formatCommand = '''{iden} CHAR({charAm}),
'''.format(iden = rowName, charAm= charAmount)
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand
        
def varCharRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        validAmount = False
        while validAmount == False:
            try:
                charAmount = int(input("How many characters: "))
                if charAmount > 0:
                    validAmount = True
                else:
                    print("Sorry the amount of characters is not valid, try again")
            except Exception as e:
                print("Sorry that is not a valid number, try again.")
        formatCommand = '''{iden} VARCHAR({charAm}),
'''.format(iden = rowName, charAm= charAmount)
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def floatRow():
    finalCommand = ""
    validHowMany = False
    while validHowMany == False:
        try:
            howMany = int(input("How many rows: "))
            if howMany > 0:
                validHowMany = True
            else:
                print("Sorry that is not valid, try again.")
        except:
            print("Sorry that is not valid, try again.")
    finalFormatCommand = ""
    for i in range(howMany):
        rowName = input("What is the name of the row: ")
        formatCommand = '''{iden} FLOAT,
'''.format(iden= rowName)
        finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def foreignKeyRow():
    finalCommand = ""
    finalFormatCommand = ""
    validKeyName = False
    while validKeyName == False:
        try:
            foreignKeyName = input("What would would you like the name of the foreign key to be: ")
            if foreignKeyName == "" or foreignKeyName == " ":
                print("Sorry that is not valid, try again")
            else:
                validKeyName = True
        except:
            print("Sorry that it not valid, try again")
    validRefTable = False
    while validRefTable == False:
        try:
            referenceTable = input("What would would you like the name of the reference table to be: ")
            if referenceTable == "" or referenceTable == " ":
                print("Sorry that is not valid, try again")
            else:
                validRefTable = True
        except:
            print("Sorry that it not valid, try again")
    validRefTableKey = False
    while validRefTableKey == False:
        try:
            refTablePrimaryKey = input("What is the primary key of {refTable}: ".format(refTable = referenceTable))
            if refTablePrimaryKey == "" or refTablePrimaryKey == " ":
                print("Sorry that is not valid, try again")
            else:
                validRefTableKey = True
        except:
            print("Sorry that it not valid, try again")
    formatCommand = '''FOREIGN KEY({iden}) REFERENCES {refTable}({refTablePrimary}),
'''.format(iden = foreignKeyName, refTable= referenceTable, refTablePrimary = refTablePrimaryKey)
    finalFormatCommand = finalFormatCommand + formatCommand
    finalCommand = "{cmd}".format(cmd = finalCommand + finalFormatCommand)
    return finalCommand

def createTable():
    validTableName = False
    while validTableName == False:
        try:
            tableName = input("What would would you like the name of the table to be: ")
            if tableName == "" or tableName == " ":
                print("Sorry that is not valid, try again")
            else:
                validTableName = True
        except:
            print("Sorry that it not valid, try again")
    command = '''CREATE TABLE IF NOT EXISTS {tableName}(
'''.format(tableName = tableName)
    userPKey = input("Would you like a primary key in the table? (Y/N)\n>>> ").upper().strip()
    if userPKey == "Y":
        validName = False
        while validName == False:
            try:
                keyName = input("What would would you like the name of the primary key to be: ")
                if keyName == "" or keyName == " ":
                    print("Sorry that is not valid, try again")
                else:
                    validName = True
            except:
                print("Sorry that it not valid, try again")
        validType = False
        while validType == False:
            try:
                keyType = input("What would you like the data type of the key to be: ").upper()
                if keyType[0:7] == "VARCHAR":
                    varAmount = int(keyType[8:-1])
                    if varAmount > 0:
                        validType = True
                    else:
                        print("Sorry the amount of characters is not valid, try again")
                elif keyType[0:4] == "CHAR":
                    varAmount = int(keyType[5:-1])
                    if varAmount > 0:
                        validType = 1
                    else:
                        print("Sorry the amount of characters is not valid, try again")
                elif keyType not in dataType:
                    print("Sorry that is not a valid data type, try again.")
                else:
                    validType = 1
            except Exception as e:
                print("Sorry that is not valid, try again")
        formatCommand = '''{iden} {dType} PRIMARY KEY UNIQUE,
'''.format(iden = keyName, dType = keyType)
        command = "{cmd}".format(cmd = command+formatCommand)
        finalCommand = command
    else:
        finalCommand = command
    carryOn = True
    while carryOn is True:
        userChoice = input('''What else would you like in the database?\n
[A] Var Char
[B] Char
[C] Integer
[D] Boolean
[E] DateTime
[F] Foreign Key
[G] Float
[X] Exit
        
>>> ''').upper()
        if userChoice == "A":
            varCharCommand = varCharRow()
            finalCommand += varCharCommand
        elif userChoice == "B":
            charCommand = charRow()
            finalCommand += charCommand
        elif userChoice == "C":
            integerCommand = integerRow()
            finalCommand += integerCommand
        elif userChoice == "D":
            booleanCommand = booleanRow()
            finalCommand += booleanCommand
        elif userChoice == "E":
            dateTimeFormat = dateTimeRow()
            finalCommand += dateTimeFormat
        elif userChoice == "F":
            foreignKeyFormat = foreignKeyRow()
            finalCommand += foreignKeyFormat
        elif userChoice == "G":
            finalCommand += floatRow()
        elif userChoice == "X":
            finalCommand = "{finalC});".format(finalC = finalCommand[:-2])
            if finalCommand == "CREATE TABLE IF NOT EXISTS test);":
                print("Sorry you must at least one attribute in the table")
                carryOn = True
            else:
                break
        else:
            print("Sorry that is not a valid option")
        finalChoice = input("Would you like to carry on? (Y/N)\n>>>  ").upper()
        if finalChoice != "Y":
            carryOn = False
            finalCommand = "{finalC});".format(finalC = finalCommand[:-2])
    return finalCommand



def menu():
    print('''
    +-+------------------------------------------------+-+
    +-+------------------------------------------------+-+
    | |          Semi Customisable SQL creator         | |
    | |              Coded by Adam Edmunds             | |
    +-+------------------------------------------------+-+
    +-+------------------------------------------------+-+


    
    ''')
    contin = True
    joinedDb = False
    while contin:
        userChoice = input('''
[A] Connect to a database
[B] Create table
[C] Show tables
[D] Enter data
[X] Stop

>>> ''').upper()
        if userChoice == "A":
            dB = joinDatabase("create")
            try:
                connection = sql.connect(dB)
                cursor = connection.cursor()
                print("\nConnected!")
                joinedDb = True
            except Exception as e:
                print("{}\n".format(str(e)))
        elif userChoice == "B":
            if joinedDb == True:
                sqlCommand = createTable()
                try:
                    cursor.execute(sqlCommand)
                    print("\nTable created!")
                except Exception as e:
                    print(str(e))
            else:
                print("Sorry you need to connect to a database first!")
        elif userChoice == "C":
            if joinedDb == True:
                sqlCommand = 'SELECT name FROM sqlite_master WHERE type = "table"'
                count = 0
                for i in cursor.execute(sqlCommand):
                    print("Table: {}\n tableName: {}  ".format(count, i[0]))
                    count +=1
            else:
                print("Sorry you need to connect to a database first!")
        elif userChoice == "D":
            if joinedDb == True:
                userIn = joinDatabase("table")
                finalString = ""
                sqlCommand = '''PRAGMA table_info({tName});'''.format(tName = userIn)
                rows= []
                for row in cursor.execute(sqlCommand):
                    isNull = ''.join(str(row[3]))
                    isPrimaryKey = ''.join(str(row[5]))
                    if isPrimaryKey == "0":
                        isPrimaryKey = "False"
                    elif isPrimaryKey == "1":
                        isPrimaryKey = "True"
                    if isNull == "0":
                        isNull = "False"
                    elif isNull == "1":
                        isNull = "True"                                        
                    finalString += "rowName: {rowName}\n dataType: {dType}\n isNotNull: {isNull}\n isPrimaryKey: {pKey}\n".format(rowName = row[1], dType = row[2], isNull = isNull, pKey = isPrimaryKey)
                    rows.append(row[1])
                tempRow = ""
                tempVal = ""
                tempAr = []
                howManyVals = ""
                for i in rows:
                    tempRow += "{}, ".format(i)
                    howManyVals += "?, "
                finalHowMany = howManyVals[:-2]
                finalRows = tempRow[:-2]
                insertInto = """INSERT INTO {tName}({rows})""".format(tName = userIn, rows = finalRows)
                for i in rows:
                    userInputValue = input("What is the data for {}: ".format(i))
                    tempVal += "{}, ".format(userInputValue)
                    tempAr.append(userInputValue)
                finalVal = tempVal[:-2]
                command = """{}
VALUES ({})""".format(insertInto, finalHowMany)
                cursor.execute(command, tuple(tempAr))
                connection.commit()
                    
            else:
                print("Sorry you need to connect to a database first!")
        elif userChoice == "X":
            print("Stopping",end='')
            for i in range(0,3):
                sleep(.1)
                end = "."
                print("{}".format(end),end='')
                
            contin = False
        else:
            print("Sorry that option is not available.\n")






















if __name__ == "__main__":
    menu()
