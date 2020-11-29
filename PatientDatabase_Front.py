#front
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import PatientDatabase_BackEnd

class Patient:

    def __init__(self, root):
        self.root=root
        self.root.title("Medata")
        self.root.geometry("1060x440+400+300")
        self.root.config(bg="#dcf4fe")

        self.root.resizable(width="False",height="False") 

        MRD_no = StringVar()
        Age = StringVar()
        AgeGrp = StringVar()
        Gender=StringVar()
        ClinicalFeatures =StringVar()
        Pneumonia=StringVar()
        Sputeum_specimen=StringVar()
        Organism=StringVar()

        load=Image.open('a.jpg')
        render=ImageTk.PhotoImage(load)

        
        

        def move_window(event):
            root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    
        
        
        

        AgeNo=[]
        for i in range(101):
            AgeNo.append(i)
            

        OptionsGender= ["","Male","Female"]
        OptionsAgeGrp=["","Pediatrics","Adult","Elderly"]
        OptionsClinicalFeatures=["","Cough","Fever","Breathlessness","Chest Pain","Others"]
        OptionsPneumonia=["","HAP","CAP"]
        

        def organism() :
            if Sputeum_specimen.get()=="Yes" :
                self.txtOrganism.config(state=NORMAL)
            
            else  :
                
                self.txtOrganism.delete(0,'end')
                self.txtOrganism.config(state=DISABLED)




        def sp():
            if pt[7]=="Yes":
                self.txtSputeum.select()
                
                
                

                
            
#===================================================================================================================================================================================================================================                
        def iexit():
            iexit=tkinter.messagebox.askyesno("Medata","Do you want to exit")
            if iexit>0:
                root.destroy()
                return

        def minim():

            root.overrideredirect(0)
            root.iconify()

        def appear(event):
            root.overrideredirect(1)


        def clearData():
            self.txtMRD.delete(0,'end')
            self.txtAge.delete(0,'end')
            Gender.set(OptionsGender[0])
            AgeGrp.set(OptionsAgeGrp[0])
            ClinicalFeatures.set(OptionsClinicalFeatures[0])
            Pneumonia.set(OptionsPneumonia[0])
            self.txtSputeum.deselect()
            organism()



        def addData():
            if (len(MRD_no.get()) !=0):
                PatientDatabase_BackEnd.addPatientRec(MRD_no.get(),Age.get(),AgeGrp.get(),Gender.get(),ClinicalFeatures.get(),Pneumonia.get(),Sputeum_specimen.get(),Organism.get())
                patientlist.delete(0,'end')
                patientlist.insert(END,(MRD_no.get(),Age.get(),AgeGrp.get(),Gender.get(),ClinicalFeatures.get(),Pneumonia.get(),Sputeum_specimen.get(),Organism.get()))
                
                
            
            
        def display():
            patientlist.delete(0,'end')
            for row in PatientDatabase_BackEnd.viewData():
                patientlist.insert(END,row,str(""))

        def PatientRec(event):
            global pt
            searchpt=patientlist.curselection()[0]
            pt= patientlist.get(searchpt)

            self.txtMRD.delete(0,'end')
            self.txtMRD.insert(END,pt[1])
            self.txtAge.delete(0,'end')
            self.txtAge.insert(END,pt[2])                   
            Gender.set(OptionsGender[0])
            Gender.set(pt[3])
            AgeGrp.set(OptionsAgeGrp[0])
            AgeGrp.set(pt[4])
            ClinicalFeatures.set(OptionsClinicalFeatures[0])
            ClinicalFeatures.set(pt[5])
            Pneumonia.set(OptionsPneumonia[0])
            Pneumonia.set(pt[6])
            self.txtSputeum.deselect()
            sp()
            self.txtOrganism.delete(0,'end')
            organism()
            self.txtOrganism.insert(END,pt[8])
            
            
                
                
        def deleteData():
            if (len(MRD_no.get()) !=0):
                PatientDatabase_BackEnd.deleteRec(pt[0])
                clearData()
                display()
                
            
        def searchData():
            patientlist.delete(0,'end')
            for row in PatientDatabase_BackEnd.search(MRD_no.get(),Age.get(),AgeGrp.get(),Gender.get(),ClinicalFeatures.get(),Pneumonia.get(),Sputeum_specimen.get(),Organism.get()):
                patientlist.insert(END,row,str(""))
            count=str(patientlist.size())
            self.lblcount = Label(ButtonFrame ,font=('arial', 8,'bold'),text="Count:"+MRD_no.get(),bg="#535356")
            self.lblcount.grid(row=0, column=7)
            
            
            
        def update():
            if (len(MRD_no.get()) !=0):
                PatientDatabase_BackEnd.deleteRec(pt[0])
            if (len(MRD_no.get()) !=0):
                PatientDatabase_BackEnd.addPatientRec(MRD_no.get(),Age.get(),AgeGrp.get(),Gender.get(),ClinicalFeatures.get(),Pneumonia.get(),Sputeum_specimen.get(),Organism.get())
                patientlist.delete(0,'end')
                patientlist.insert(END,(MRD_no.get(),Age.get(),AgeGrp.get(),Gender.get(),ClinicalFeatures.get(),Pneumonia.get(),Sputeum_specimen.get(),Organism.get()))
            
        

        
        


                       
#===================================================================================================================================================================================================================================


        MainFrame = Frame(self.root, bg="#535356")
        MainFrame.grid()

        TitFrame=Frame(MainFrame, bd=2, padx=54,pady=8, bg="#535356", relief=RIDGE)


        self.lblTit = Label(TitFrame ,font=('arial', 47,'bold'),text="Medata",bg="#535356")
        self.lblTit.grid()

        ButtonFrame =Frame(MainFrame, bd=2, width=1350, height=70, padx=18,pady=10, bg="#535356",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=1, width=1300, height=400, padx=20,pady=20, relief=RIDGE, bg="#535356")
        DataFrame.pack(side=BOTTOM)
        
        DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="#535356",font=('arial', 20,'bold'),text="Patient Info\n",fg="#d7d7d7")
        DataFrameRIGHT.pack(side=RIGHT)

        DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady=3, relief=RIDGE, bg="#535356",font=('arial', 20,'bold'),text="Patient Database\n",fg="#d7d7d7")
        DataFrameLEFT.pack(side=LEFT)



#=============================================================================================================================================================================================================================================
        self.lblMRD = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="MRD_no:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblMRD.grid(row=0, column=0, sticky=W)
        self.txtMRD = Entry(DataFrameRIGHT,font=('arial', 15,'bold'),textvariable=MRD_no,width=39,bg="#535356",fg="#d7d7d7")
        self.txtMRD.grid(row=0, column=1)


        self.lblAge = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="Age:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblAge.grid(row=1, column=0, sticky=W)
        self.txtAge = Entry(DataFrameRIGHT,font=('arial', 15,'bold'),textvariable=Age,width=39,bg="#535356",fg="#d7d7d7")
        self.txtAge.grid(row=1, column=1)

      


        self.lblAgeGrp = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="AgeGrp:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblAgeGrp.grid(row=2, column=0, sticky=W)
        self.txtAgeGrp = OptionMenu(DataFrameRIGHT, AgeGrp, *OptionsAgeGrp)
        self.txtAgeGrp.grid(row=2, column=1)



        self.lblGender = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="Gender:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblGender.grid(row=3, column=0, sticky=W)
        self.txtGender = OptionMenu(DataFrameRIGHT, Gender, *OptionsGender)
        self.txtGender.grid(row=3, column=1)

        

        self.lblClinicalFeatures = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="ClinicalFeatures:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblClinicalFeatures.grid(row=4, column=0, sticky=W)
        self.txtClinicalFeatures = OptionMenu(DataFrameRIGHT, ClinicalFeatures, *OptionsClinicalFeatures)
        self.txtClinicalFeatures.grid(row=4, column=1)


        
        
        self.lblPneumonia = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="Pneumonia:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblPneumonia.grid(row=5, column=0, sticky=W)
        self.txtPneumonia = OptionMenu(DataFrameRIGHT,Pneumonia , *OptionsPneumonia)
        self.txtPneumonia.grid(row=5, column=1)
      

        
        self.lblSputeum = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="Sputeum_specimen:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblSputeum.grid(row=6, column=0, sticky=W)
        self.txtSputeum = Checkbutton(DataFrameRIGHT,variable= Sputeum_specimen,bg="#535356",onvalue="Yes",offvalue="No",command=organism)
        self.txtSputeum.deselect()
        self.txtSputeum.grid(row=6, column=1)
        



        self.lblOrganism = Label(DataFrameRIGHT,font=('arial', 15,'bold'),text="Organism:",padx=2,pady=2,bg="#535356",fg="#d7d7d7")
        self.lblOrganism.grid(row=7, column=0, sticky=W)
        self.txtOrganism = Entry(DataFrameRIGHT,font=('arial', 15,'bold'),textvariable=Organism,width=39,bg="#535356",state=DISABLED,fg="#d7d7d7")
        self.txtOrganism.grid(row=7, column=1)



#=============================================================================================================================================================================================================================================
        scrollbar=Scrollbar(DataFrameLEFT)
        scrollbar.grid(row=0, column=1,sticky='ns')
        patientlist=Listbox(DataFrameLEFT, width=41, height=16,font=('arial', 8,'bold'),bg="#535356",yscrollcommand=scrollbar.set)
        patientlist.bind('<<ListboxSelect>>', PatientRec)
        patientlist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=patientlist.yview)

            

        
#=============================================================================================================================================================================================================================================

        self.buttonAddData=Button(ButtonFrame,text="Add",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=addData)
        self.buttonAddData.grid(row=0, column=0)

        
        self.buttonShow=Button(ButtonFrame,text="Show",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=display)
        self.buttonShow.grid(row=0, column=1)


        self.buttonClear=Button(ButtonFrame,text="Clear",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=clearData)
        self.buttonClear.grid(row=0, column=2)


        self.buttonDelete=Button(ButtonFrame,text="Delete",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=deleteData)
        self.buttonDelete.grid(row=0, column=3)


        self.buttonSearch=Button(ButtonFrame,text="Search",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=searchData)
        self.buttonSearch.grid(row=0, column=4)

        self.buttonUpdate=Button(ButtonFrame,text="Update",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,fg="#d7d7d7",command=update)
        self.buttonUpdate.grid(row=0, column=5)

        self.buttonExit=Button(ButtonFrame,text="Exit",font=('arial', 8,'bold'),bg="#535356",width=10, height=1,bd=4,command=iexit,fg="#d7d7d7")
        self.buttonExit.grid(row=0, column=6)


#=============================================================================================================================================================================================================================================
        root.overrideredirect(True)
        self.title_bar = Frame(MainFrame, bg="#535356", relief='raised', bd=2)
        self.title_bar.pack(expand=1, fill=BOTH)

        
        self.close_button = Button(self.title_bar, text='X',bg="#535356",fg="#d7d7d7", command=iexit)
        self.close_button.pack(side=RIGHT)


        self.minimize_button = Button(self.title_bar, text='_',bg="#535356",fg="#d7d7d7", command=minim)
        self.minimize_button.pack(side=RIGHT)
        

        self.title = Label(self.title_bar, text='Medata',font=('MV Boli', 8,'bold'),bg="#535356",fg='white')
        self.title.pack(side=LEFT)
        

        self.title_bar.bind('<B1-Motion>', move_window)
        self.title_bar.bind('<Map>',appear)
        
        

        

        






      


if __name__=='__main__':
    root =Tk()
    application = Patient(root)
    root.mainloop  
