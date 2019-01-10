
import sqlite3 as sql
from string import punctuation as specialChar
import datetime

DATATYPE = ["BOOLEAN","VARCHAR","CHAR","INTEGER","FLOAT","TIME","DATE"]
connected = False

def joinDatabase(arg):
    global connected
    validDb = False
    if arg == "database":
        userIn = input("\nWhat is the name of the database that you want to connect to?\n>>> ").strip()
    if " " in userIn:
        return "\nYou can't use that as a name!\nHint you can't use spaces."
    elif userIn == "":
        return "\nYou can't use that as a name!\nHint you can't leave it blank"
    elif any(i in userIn for i in specialChar):
        return "\nYou can't use that as a name!\nHint there is punctuation."
    else:
        validDb = True
    if arg == "database" and validDb is True:
        userIn = "{}.db".format(userIn)
        return userIn

def validInput(type):
    if type == "tableName":
        while True:
            try:
                tblName = input("What is the table name?\n>>> ").strip()
                if " " in tblName or tblName == "":
                    print("Sorry that is not a valid [Space in name]")
                elif any(i in tblName for i in specialChar):
                    print("Sorry that is not valid [Punctuation Used]")
                else:
                    return tblName
            except Exception as e:
                print(f"Error \"{e}\" when creating table name [See validInput tableName]")

    elif type == "primary key":
        while True:
            try:
                keyName = input(f"What is the name of the {type.upper()}?\n>>> ").strip()
                if " " in keyName or keyName == "":
                    print("Sorry that is not a valid name try again [Space in name]")
                elif any(i in keyName for i in specialChar):
                    print("Sorry that is not valid try again [Punctuation used]")
                else:
                    return keyName
            except Exception as e:
                print(f"Error \"{e}\" when adding primary key [See validInput Primary Key]")

    elif type in ["varchar","char","date","time","float","integer","boolean"]:
        while True:
            try:
                rowName = input(f"What is the name of the {type.upper()}?\n>>> ").strip()
                if " " in rowName or rowName == "":
                    print("Sorry that is not a valid name try again [Space in name]")
                elif any(i in rowName for i in specialChar):
                    print("Sorry that is  not try again [Punctuation used]")
                else:
                    return rowName
            except Exception as e:
                print(f"Error \"{e}\" when adding varchar / char key [See validInput Varchar / Char]")

    elif type == "number":
        while True:
            try:
                number = int(input(f"What is the number of characters:\n>>> "))
                if number < 1:
                    print("Sorry that number is not greater than 0")
                else:
                    return number
            except Exception as e:
                print(f"Error \"{e}\" when adding number [See validInput Number]")

def validData(attribute, datatype, nullValue,isPKey):
    types = {"VARCHAR":str,"CHAR":str,"INTEGER":int,"FLOAT":float,"BOOLEAN":bool,"DATE":type(datetime.datetime.now().date()),"TIME":type(datetime.datetime.now().time())}
    if datatype[:7] == "VARCHAR":
        datatype = "VARCHAR"
    elif datatype[:4] == "CHAR":
        datatype = "CHAR"
    while True:
        uInput = input(f"What is the data for {datatype} {attribute}: ").strip()
        if " " in uInput or uInput == "":
            print("Sorry you can't use spaces")
            continue
        if datatype not in ["VARCHAR","CHAR"]:
            try:
                if uInput.isdigit():
                    uInput = int(uInput)
                elif uInput.lower() in ["true","false"]:
                    uInput = bool(uInput)
                    print(type(uInput))
                elif type(float(uInput)) == float:
                    uInput = float(uInput)
            except:
                pass
        print(type(uInput))
        print(types[f"{datatype}"])
        if type(uInput) == types[f"{datatype}"]:
            print("passed")
            break
        else:
            print("Sorry that is not a valid data type")
    return uInput

def findIndex(array, argument):
    index = None
    try:
        for i in array:
            if i[0] == argument:
                index = i.index(argument)
                return index
    except Exception as e:
        print(f"Error {e} when finding index. See findIndex")

def addID(array, argument, whatToAdd):
    try:
        for x in array:
            if x[0] == argument:
                for ids in x:
                    if ids != argument:
                        ids.append(whatToAdd)
        return array
    except Exception as e:
        print(f"Error {e} when adding element. See addID")

def createTable(tblName):
    table = []
    values = {"A": "varchar","B":"char","C":"integer","D":"float","E":"date","F":"time","G":"boolean"}
    pKey = input("Would you like a primary key? [Yes,Y]\n>>> ").upper()
    if pKey in ["YES","Y"]:
        pKey = validInput("primary key")
        dataType = input("What is the datatype?\n>>> ").strip().upper()
        while dataType not in DATATYPE:
            print("Sorry that is not valid")
            dataType = input("What is the datatype?\n>>> ").strip().upper()
        if dataType in ["VARCHAR","CHAR"]:
            chars = validInput("number")
            dataType = f"{dataType}({chars})"
        table.append([f"{dataType} PRIMARY KEY",[pKey]])
    else:
        print("Not adding a primary key!")
    carryOn = True
    while carryOn is True:
        withChar = False
        additional = input("\nWhat else would you like in the table?\nA| Varchar\nB| Char\nC| Integer\nD| Float\nE| Date\nF| Time\nG| Boolean\nX| Exit\n\n>>> ").strip().upper()
        if additional == "X":
            string = f"CREATE TABLE IF NOT EXISTS {tblName}(\n"
            for x in table:
                for y in x[1]:
                    notNull = input(f"Would you like {y} to be not null?\n>> ").strip().upper()
                    if notNull in ["Y", "YES"]:
                        string += f"{y} {x[0].upper()} NOT NULL,\n"
                    else:
                        string += f"{y} {x[0].upper()},\n"
            string = f"{string[:-2]});"
            cursor.execute(string)
            break
        try:
            whatVariable = values[additional]
            if whatVariable in ["varchar", "char"]:
                withChar = True
        except:
            withChar = None
        if withChar is True:
            variable = validInput(whatVariable)
            chars = validInput("number")
            index = findIndex(table, f"{whatVariable}({chars})")
            if index is None:
                table.append([f"{whatVariable}({chars})", [variable]])
            else:
                table = addID(table, f"{whatVariable}({chars})", variable)
        elif withChar is None:
            pass
        else:
            variable = validInput(whatVariable)
            index = findIndex(table, whatVariable)
            if index is None:
                table.append([whatVariable, [variable]])
            else:
                table = addID(table, whatVariable, variable)

if __name__ == "__main__":
    while True:
        menuIn = input("\nWhat do you want to do?\nA| Create database\nB| Create table\nC| Show tables\nD| Enter Data\nX| Exit\n\n>>> ").lower()
        if menuIn == "a":
            dbName = joinDatabase("database")
            try:
                connection = sql.connect(dbName)
                cursor = connection.cursor()
                connected = True
                print(f"Connected to {dbName}")
            except Exception as e:
                print(str(e))
        elif menuIn == "b":
            if connected is False:
                print("Please connect to a database first")
            else:
                createTable(validInput("tableName"))
        elif menuIn == "c":
            if connected is False:
                print("Please connect to a database first")
            else:
                data = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
                for i in data.fetchall():
                    tables = cursor.execute(f"PRAGMA table_info({i[0]})").fetchall()
                    print(i[0])
                    null = {0: "Null", 1: "Not Null"}
                    isPKey = {0: "", 1: "Primary Key"}
                    for x in tables:
                        print(f" |{x[0]}| {x[1]} {x[2]} {isPKey[x[5]]} {null[x[3]]}")
        elif menuIn == "d":
            if connected is False:
                print("Please connect to a database first")
            else:
                finalString = ""
                whatTable = input("What table do you want to enter data for?\n>>> ").strip()
                inserting = f"INSERT INTO {whatTable}("
                values = "VALUES ("
                data = []
                for i in cursor.execute(f"PRAGMA table_info({whatTable})").fetchall():
                    inserting += f"{i[1]},"
                    values += "?,"
                    uInput = validData(i[1],i[2],i[3],i[4])
                    data.append(uInput)
                cursor.execute(f"{inserting[:-1]}) {values[:-1]})",(data))
                connection.commit()

        elif menuIn == "x":
            print("Thanks for using my software")
            connection.close()
            break
        else:
            print("Sory that is not a valid option\n")
