import json
import Epic

def OpenFile():
    ClassList = ""
    OpenFile = open('ShelbyClassList.json')
    for line in OpenFile:
        line = line.strip()
        ClassList = ClassList + line
    ShelbyClasses= json.loads(ClassList)
    return ShelbyClasses
    
def Search(ProfessorName):
    Classes = OpenFile()
    for Class in Classes:
        if Class["ProfessorName"] == ProfessorName:
            print "%s" % Class["ProfessorName"]
            print "%s" % Class["Location"]
            print "%s" % Class["Time"]
                
            
def main():
    ProfessorName = Epic.userString("Enter Professor Name:")
    Search(ProfessorName)
    
main()