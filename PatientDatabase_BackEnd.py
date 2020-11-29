#BackEnd
import sqlite3


def patientData():
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patient(id INTEGER PRIMARY KEY,MRD_no text,Age text,AgeGrp text,Gender text,ClinicalFeatures text,Pneumonia,Sputeum_specimen text,Organism text)")
    con.commit()
    con.close()

def addPatientRec(MRD_no,Age,AgeGrp,Gender,ClinicalFeatures,Pneumonia,Sputeum_specimen,Organism):
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("INSERT INTO patient VALUES(NULL ,?,?,?,?,?,?,?,?)",(MRD_no,Age,AgeGrp,Gender,ClinicalFeatures,Pneumonia,Sputeum_specimen,Organism))
    con.commit()
    con.close()



def viewData():
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM patient")
    rows=cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("DELETE FROM patient WHERE id=?",(id,))
    con.commit()
    con.close()
    
    
    
def search(MRD_no="",Age="",AgeGrp="",Gender="",ClinicalFeatures="",Pneumonia="", Sputeum_specimen="",Organism=""):
    st=""
    if MRD_no!="" :
        st=st+'MRD_no="'+MRD_no+'" AND '
    if Age!="" :
        st=st+'Age="'+Age+'" AND '
    #if AgeGrp!="" :
        #st=st+'AgeGrp="'+AgeGrp+'" AND '
    #if Gender!="" :
        #st=st+'Gender="'+Gender+'" AND '
    #if ClinicalFeatures!="" :
        #st=st+'ClinicalFeatures="'+ClinicalFeatures+'" AND '
    #if Pneumonia!="" :
        #st=st+'Pneumonia="'+Pneumonia+'" AND '
    #if Sputeum_specimen!="" :
        #st=st+'Sputeum_specimen="'+Sputeum_specimen+'" AND '
    if Organism!="" :
        st=st+'Organism="'+Organism+'" AND '    
        
    st=st+"1=1"    
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM patient WHERE "+st)
    rows=cur.fetchall()
    con.close()
    return rows


def dataUpdate(id,MRD_no="",Age="",AgeGrp="",Gender="",ClinicalFeatures="",Pneumonia="",Sputeum_specimen="",Organism=""):
    con=sqlite3.connect("patient.db")
    cur=con.cursor()
    cur.execute("UPDATE  patient SET MRD_no=?,Age,AgeGrp=?,Gender=?,ClinicalFeatures=?,Pneumonia=?,Sputeum_specimen=?,Organism=?,WHERE id=?",(MRD_no,Age,AgeGrp,Gender,ClinicalFeatures,Pneumonia,Sputeum_specimen,Organism))
    con.commit()
    con.close()

    
#def drop():
    #con=sqlite3.connect("patient.db")
    #cur=con.cursor()
    #cur.execute("DROP TABLE patient")
    #con.commit()
    #con.close()    





patientData()
