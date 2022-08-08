
from curses import window
import tkinter as tk
from tkinter import messagebox,ttk
from tkinter.filedialog import askopenfile
from tkinter.font import BOLD


from Components.functions import add_an_existing_subject, approved_fun, edit_subject, select_file
#Import the subject class
#from Components.subject import Subject


class MainPage(tk.Tk):

    def __init__(self):
        super().__init__()
        #Title
        self.title('PRACTICA 1')
        #Dimension
        self.geometry('600x400+700+200')
        self['background']='#dbdbdb'
        #Grid
        self.columnconfigure(0,weight=1)

        #Variables
        self._var = tk.StringVar(value='Ruta del archivo...')
        #Containt the file 
        self.file = None
        #To verified the actual file
        self.open_file = False
        #list of subject objects
        self.subjects = []
        #Components
        self._create_components()
    

    def _create_components(self):
        #Labels
        #usando el sticky N(arriba), E(derecha), S(abajo), W(izquierda) 
        tk.Label(self,text='Lenguajes Formales y de Programación',font=("Verdana",14)).grid(row=0,column=0,sticky='WE',padx=10,pady=10)
        tk.Label(self,text='Alvaro Norberto García Meza',font=("Verdana",14)).grid(row=1,column=0,sticky='WE',padx=10,pady=10)
        tk.Label(self,text='Carnet: 202109567',font=("Verdana",14)).grid(row=2,column=0,sticky='WE',padx=10,pady=10)

        #Buttons of the main page
        #file upload
        btn_upload = tk.Button(self,text='Cargar Archivo',command=self._file_upload,height=2,width=15)
        btn_upload.grid(row=3,column=0,pady=10)
        #Manage
        btn_manage = tk.Button(self,text='Gestionar Curso',command=self._manage_subjects,height=2,width=15)
        btn_manage.grid(row=4,column=0,pady=10)
        #Count Credits
        btn_countC = tk.Button(self,text='Conteo de Créditos',command=self._count_credits,height=2,width=15)
        btn_countC.grid(row=5,column=0,pady=10)
        #quit
        btn_quit = tk.Button(self,text='Salir',command=lambda: self.quit(),height=2,width=15)
        btn_quit.grid(row=6,column=0,pady=10)

    #First button command -> File Upload
    def _file_upload(self):
        window = tk.Toplevel(self)
        window.geometry('600x200+700+200')
        window.title('Seleccionar Archivo')
        window.rowconfigure(0,weight=4)
        window.rowconfigure(1,weight=2)
        self.withdraw()
        #Functions
        def back():
            self.deiconify()
            window.destroy()
        #Label
        tk.Label(window,text='Ruta',font=("Verdana",12)).grid(row=0,column=0,sticky='WE',padx=8,pady=5)
        #Entry
        file_name = tk.Entry(window,textvariable=self._var,width=89)
        file_name.grid(row=0,column=1,sticky='WE',columnspan=2)
        #Buttons
        btn_select = tk.Button(window,text='Seleccionar archivo',command=lambda: select_file(self),height=2,width=15)
        btn_select.grid(row=1,column=1,pady=2)
        btn_back = tk.Button(window,text='Regresar',command=back,height=2,width=15)
        btn_back.grid(row=1,column=2)

    #Second button command -> Manage subjects
    def _manage_subjects(self):
        #Create buttons
        window = tk.Toplevel(self)
        window.geometry('600x400+700+200')
        window.title('Gestionar Cursos')
        window.columnconfigure(0,weight=1)
        self.withdraw()
        
        #List Window
        def list_courses():
            list_window = tk.Toplevel(window)
            list_window.geometry('1560x300+200+200')
            list_window.title('Listado de Cursos')
            window.withdraw()
            #Table
            columns = ('codigo','nombre','pre_requisito','opcionalidad','semestre','creditos','estado')
            tree = ttk.Treeview(list_window,columns=columns,show='headings')
            #Define headings
            tree.heading('codigo', text='Código')
            tree.heading('nombre', text='Nombre')
            tree.heading('pre_requisito', text='Pre requisito')
            tree.heading('opcionalidad', text='Opcionalidad')
            tree.heading('semestre', text='Semestre')
            tree.heading('creditos', text='Créditos')
            tree.heading('estado', text='Estado')
            #Contact the values
            courses = []
            for i in self.subjects:
                courses.append((
                    f' {i.codigo} ',
                    f' {i.nombre} ',
                    f' {i.preRequisito} ',
                    f' {i.obligatorio} ',
                    f' {i.semestre} ',
                    f' {i.creditos} ',
                    f' {i.estado} '
                ))
            #add data to the treeview
            for c in courses:
                tree.insert('',tk.END,values=c)
            
            tree.grid(row=0, column=0, sticky='nsew',padx=5,pady=5)
            #button
            def back():
                window.deiconify()
                list_window.destroy()
            btn_back = tk.Button(list_window,text='Regresar',command=back,height=2,width=15)
            btn_back.grid(row=10,column=5,padx=6)

        #Add course
        def add_course():
            #Variables
            code = tk.StringVar(value='')
            name = tk.StringVar(value='')
            pre = tk.StringVar(value='')
            semester = tk.StringVar(value='')
            optional = tk.StringVar(value='')
            credits = tk.StringVar(value='')
            state = tk.StringVar(value='')
            
            add_window = tk.Toplevel(window)
            add_window.geometry('600x500+700+200')
            add_window.title('Agregar Curso')
            add_window.columnconfigure(0,weight=2)
            add_window.columnconfigure(1,weight=5)
            window.withdraw()

            #Labels
            tk.Label(add_window,text='Código:',font=('Arial',12,BOLD)).grid(row=0,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Nombre:',font=('Arial',12,BOLD)).grid(row=1,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Pre Requisito:',font=('Arial',12,BOLD)).grid(row=2,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Semestre:',font=('Arial',12,BOLD)).grid(row=3,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Opcional:',font=('Arial',12,BOLD)).grid(row=4,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Créditos:',font=('Arial',12,BOLD)).grid(row=5,column=0,padx=5,pady=10)
            tk.Label(add_window,text='Estado:',font=('Arial',12,BOLD)).grid(row=6,column=0,padx=5,pady=10)

            #Entries
            code_entry = tk.Entry(add_window,textvariable=code,width=3,font=('Arial',12,BOLD))
            code_entry.grid(row=0,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            name_entry = tk.Entry(add_window,textvariable=name,width=15,font=('Arial',12,BOLD))
            name_entry.grid(row=1,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            pre_entry = tk.Entry(add_window,textvariable=pre,width=10,font=('Arial',12,BOLD))
            pre_entry.grid(row=2,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            semester_entry = tk.Entry(add_window,textvariable=semester,width=10,font=('Arial',12,BOLD))
            semester_entry.grid(row=3,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            optinal_entry = tk.Entry(add_window,textvariable=optional,width=10,font=('Arial',12,BOLD))
            optinal_entry.grid(row=4,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            credits_entry = tk.Entry(add_window,textvariable=credits,width=10,font=('Arial',12,BOLD))
            credits_entry.grid(row=5,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            state_entry = tk.Entry(add_window,textvariable=state,width=10,font=('Arial',12,BOLD))
            state_entry.grid(row=6,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)
            #Functions
            def add():
                #This function add a course
                if code.get() and name.get() and optional.get() and semester.get() and state.get() and credits.get():
                    add_an_existing_subject(self,code,name,optional,semester,state,pre,credits)
                else:
                    messagebox.showerror('Error!','Debes ingresar todos los campos a expeción de Pre requisitos!')
                
            btn_add = tk.Button(add_window,text='Agregar',command=add,height=2,width=15)
            btn_add.grid(row=7,column=0,padx=10,pady=10)

            def back():
                window.deiconify()
                add_window.destroy()
                
            btn_back = tk.Button(add_window,text='Regresar',command=back,height=2,width=15)
            btn_back.grid(row=7,column=1,padx=10,pady=10)

        def edit_course():
            #Variables
            code = tk.StringVar(value='')
            name = tk.StringVar(value='')
            pre = tk.StringVar(value='')
            semester = tk.StringVar(value='')
            optional = tk.StringVar(value='')
            credits = tk.StringVar(value='')
            state = tk.StringVar(value='')
            
            edit_window = tk.Toplevel(window)
            edit_window.geometry('600x550+700+200')
            edit_window.title('Editar Curso')
            edit_window.columnconfigure(0,weight=2)
            edit_window.columnconfigure(1,weight=5)
            window.withdraw()
            #
            def selection_changed(event):
                selection = combo.get()
                for i in self.subjects:
                    if i.nombre == selection:
                        code.set(f'{i.codigo}')
                        name.set(f'{i.nombre}')
                        pre.set(f'{i.preRequisito}')
                        optional.set(f'{i.obligatorio}')
                        semester.set(f'{i.semestre}')
                        credits.set(f'{i.creditos}')
                        state.set(f'{i.estado}')
                print(selection)
            list_combo = []
            for i in self.subjects:
                list_combo.append(i.nombre)
            combo = ttk.Combobox(
                edit_window,
                values= list_combo,
                state='readonly'
            )
            combo.bind("<<ComboboxSelected>>",selection_changed)
            combo.grid(row=0,column=0,padx=5,pady=10,columnspan=2,ipadx=30,ipady=8)
            #Labels
            tk.Label(edit_window,text='Código:',font=('Arial',12,BOLD)).grid(row=1,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Nombre:',font=('Arial',12,BOLD)).grid(row=2,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Pre Requisito:',font=('Arial',12,BOLD)).grid(row=3,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Semestre:',font=('Arial',12,BOLD)).grid(row=4,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Opcional:',font=('Arial',12,BOLD)).grid(row=5,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Créditos:',font=('Arial',12,BOLD)).grid(row=6,column=0,padx=5,pady=10)
            tk.Label(edit_window,text='Estado:',font=('Arial',12,BOLD)).grid(row=7,column=0,padx=5,pady=10)

            #Entries
            code_entry = tk.Entry(edit_window,textvariable=code,width=3,font=('Arial',12,BOLD))
            code_entry.grid(row=1,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            name_entry = tk.Entry(edit_window,textvariable=name,width=15,font=('Arial',12,BOLD))
            name_entry.grid(row=2,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            pre_entry = tk.Entry(edit_window,textvariable=pre,width=10,font=('Arial',12,BOLD))
            pre_entry.grid(row=3,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            semester_entry = tk.Entry(edit_window,textvariable=semester,width=10,font=('Arial',12,BOLD))
            semester_entry.grid(row=4,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            optinal_entry = tk.Entry(edit_window,textvariable=optional,width=10,font=('Arial',12,BOLD))
            optinal_entry.grid(row=5,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            credits_entry = tk.Entry(edit_window,textvariable=credits,width=10,font=('Arial',12,BOLD))
            credits_entry.grid(row=6,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            state_entry = tk.Entry(edit_window,textvariable=state,width=10,font=('Arial',12,BOLD))
            state_entry.grid(row=7,column=1,sticky='WE',ipadx=8,ipady=8,padx=5,pady=10)

            #Functions
            def edit():
                #This function add a course
                if code.get() and name.get() and optional.get() and semester.get() and state.get() and credits.get():
                    edit_subject(self,code,name,optional,semester,state,pre,credits)
                else:
                    messagebox.showerror('Error!','Debes ingresar todos los campos a expeción de Pre requisitos!')

            btn_edit = tk.Button(edit_window,text='Editar',command=edit,height=2,width=15)
            btn_edit.grid(row=8,column=0,padx=10,pady=10)

            def back():
                window.deiconify()
                edit_window.destroy()
            btn_back = tk.Button(edit_window,text='Regresar',command=back,height=2,width=15)
            btn_back.grid(row=8,column=1,padx=10,pady=10)
            
        
        #Delete course
        def delete_course():
            delete_window = tk.Toplevel(window)
            delete_window.geometry('280x300+700+200')
            delete_window.title('Editar Curso')
            delete_window.rowconfigure(0,weight=3)
            delete_window.rowconfigure(1,weight=2)
            window.withdraw()
            #
            def selection_changed(event):
                pass
            list_combo = []
            for i in self.subjects:
                list_combo.append(i.nombre)

            combo = ttk.Combobox(
                delete_window,
                values= list_combo,
                state='readonly'
            )
            combo.bind("<<ComboboxSelected>>",selection_changed)
            combo.grid(row=0,column=0,padx=5,pady=10,columnspan=2,ipadx=30,ipady=8)
            #Butons
            #Functions
            def delete():
                select = combo.get()
                for i in self.subjects:
                    if i.nombre == select:
                        self.subjects.remove(i)
                        messagebox.showwarning('Eliminar Curso',f'Se ha eliminado el curso {i.nombre} correctamente!')

            btn_delete = tk.Button(delete_window,text='Eliminar',command=delete,height=2,width=15)
            btn_delete.grid(row=1,column=0,padx=10,pady=10)

            def back():
                window.deiconify()
                delete_window.destroy()
            btn_back = tk.Button(delete_window,text='Regresar',command=back,height=2,width=15)
            btn_back.grid(row=1,column=1,padx=10,pady=10)
                
        #Create the buttons
        #List courses
        btn_list_subjects = tk.Button(window,text='Listar Cursos',command=list_courses,height=2,width=15)
        btn_list_subjects.grid(row=0,column=0,pady=20)
        #Add Subject
        btn_add_subject = tk.Button(window,text='Agregar Curso',command=add_course,height=2,width=15)
        btn_add_subject.grid(row=1,column=0,pady=15)
        #Edit Subject
        btn_edit_subject = tk.Button(window,text='Editar Curso',command=edit_course,height=2,width=15)
        btn_edit_subject.grid(row=2,column=0,pady=15)
        #Delete subject
        btn_delete_subject = tk.Button(window,text='Eliminar Curso',command=delete_course,height=2,width=15)
        btn_delete_subject.grid(row=3,column=0,pady=15)
        #Quit
        def back():
            self.deiconify()
            window.destroy()
        btn_back = tk.Button(window,text='Regresar',command=back,height=2,width=15)
        btn_back.grid(row=4,column=0,pady=15)

    #Third buttom command -> Count the credtis
    def _count_credits(self):

        count_window = tk.Toplevel(self)
        count_window.geometry('700x700+700+100')
        count_window.title('Contare Creditos')
        
        self.withdraw()

        #Variable
        approved_sub = tk.StringVar(value='')
        cursing_sub = tk.StringVar(value='')
        pending_sub = tk.StringVar(value='')
        required_credtis = tk.StringVar(value='Créditos Obligatorios hasta el semestre:')

        #Fun
        approved_fun(self,approved_sub,cursing_sub,pending_sub)
        def selection_changed(event):
            total_credits = 0
            n_semester = combo.get()
            #Calculated the credits of the semester 1 to N, only the required courses
            for i in self.subjects:
                if int(i.semestre) <= int(n_semester) and i.obligatorio == 'Obligatorio':
                    total_credits += int(i.creditos)

            required_credtis.set(f'Créditos Obligatorios hasta el semestre {n_semester}: {total_credits} créditos ')

            print(f'Creditos totales = {total_credits} ')
        
        def count_credits_per_semester():
            #semester 
            semester = spin.get()
            c_a = 0
            c_c = 0
            c_p = 0
            #Filter by semester
            for i in self.subjects:
                if int(i.semestre) == int(semester):
                    if i.estado == 'Aprobado':
                        c_a += int(i.creditos)
                    elif i.estado == 'Cursando':
                        c_c += int(i.creditos)
                    elif i.estado == 'Pendiente':
                        c_p += int(i.creditos)
            print(semester)
            messagebox.showinfo(f'Creditos del semestre {semester}', f'Creditos de cursos aprobados {c_a} \n Créditos de cursos asignados {c_c} \n Créditos de cursos pendientes {c_p} ')
             
        #labels
        tk.Label(count_window,text=f'Créditos Aprobados: {approved_sub.get()} ',font=('Arial',12,BOLD)).grid(row=0,column=0,padx=5,pady=15)
        tk.Label(count_window,text=f'Créditos Cursando: {cursing_sub.get()} ',font=('Arial',12,BOLD)).grid(row=1,column=0,padx=5,pady=15)
        tk.Label(count_window,text=f'Créditos Pendientes: {pending_sub.get()} ',font=('Arial',12,BOLD)).grid(row=2,column=0,padx=5,pady=15)
        tk.Label(count_window,textvariable=required_credtis,font=('Arial',12,BOLD)).grid(row=3,column=0,padx=5,pady=15)
        tk.Label(count_window,text='Semestre:',font=('Arial',12,BOLD)).grid(row=4,column=0,padx=5,pady=15)
        
        #Numeric selection
        list_combo = [x for x in range(1,11)]
        
        combo = ttk.Combobox(
            count_window,
            values= list_combo,
            state='readonly'
        )
        combo.bind("<<ComboboxSelected>>",selection_changed)
        combo.grid(row=4,column=1,padx=5,pady=10,columnspan=2,ipadx=30,ipady=8)

        #Spin
        spin = ttk.Spinbox(count_window,from_=1,to=10,font=('Arial',14,BOLD))
        spin.grid(row=5,column=0,padx=2,pady=10,columnspan=2,ipadx=5,ipady=5)
        #Button
        btn_filter = tk.Button(count_window,text='Contar',command=count_credits_per_semester,height=2,width=15)
        btn_filter.grid(row=5,column=1,padx=2,pady=10,columnspan=2,ipadx=5,ipady=5)

        #Quit
        def back():
            self.deiconify()
            count_window.destroy()
        btn_back = tk.Button(count_window,text='Regresar',command=back,height=2,width=15)
        btn_back.grid(row=6,column=0,rowspan=2)

    

if __name__ == '__main__':
    main_page = MainPage()
    main_page.mainloop()





