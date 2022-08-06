
import re


from tkinter import messagebox
from Components.subject import Subject


def add_an_existing_subject(self, code, name, optional, semester, state, pre, credits):
    if len(self.subjects) > 0:
        for i in self.subjects:
            if i.codigo == code.get():
                messagebox.showerror(
                    'Agregar Curso',
                    f'Curso con código {i.codigo} ya existe. Se Eliminará y Reemplazará '
                )
                self.subjects.remove(i)
                # Add Course
                obj = Subject(code.get(), name.get(), pre.get(), optional.get(), semester.get(), credits.get(), state.get())
                self.subjects.append(obj)
                # Restart
                code.set('')
                name.set('')
                pre.set('')
                optional.set('')
                semester.set('')
                credits.set('')
                state.set('')
                break
            else:
                # If there not an existing subject, we validate and add to the list
                # Add Course
                obj = Subject(code.get(), name.get(), pre.get(), optional.get(), semester.get(), credits.get(), state.get())
                self.subjects.append(obj)
                # Restart
                code.set('')
                name.set('')
                pre.set('')
                optional.set('')
                semester.set('')
                credits.set('')
                state.set('')
                messagebox.showinfo(
                    'Agregar Curso',
                    f'Se ha agregado el curso con código{obj.codigo} correctamente!.'
                )
                break
    else:
       # If there not an existing subject, we validate and add to the list
        # Add Course
        obj = Subject(code.get(), name.get(), pre.get(),optional.get(), semester.get(), credits.get(), state.get())
        self.subjects.append(obj)
        # Restart
        code.set('')
        name.set('')
        pre.set('')
        optional.set('')
        semester.set('')
        credits.set('')
        state.set('')
        messagebox.showinfo(
            'Agregar Curso',
            f'Se ha agregado el curso con código{obj.codigo} correctamente!.'
        )
        
def edit_subject(self, code, name, optional, semester, state, pre, credits):
    #Var
    obligatorio = ''
    estado = ''

    #Transform the values
    if optional.get() == 'Opcional':
        obligatorio = '1' 
    else:
        obligatorio = '0'
    
    if state.get() == 'Aprobado':
        estado = '0'
    elif state.get() == 'Cursando':
        estado = '1'
    else: 
        estado = '-1'
    #Iterate through the subjects, find the course and edit their values
    for i in self.subjects:
        #If the code is equal to the code.get
        if i.codigo == code.get():
            #Edit
            i.codigo = code.get()
            i.nombre = name.get()
            i.preRequisito = pre.get()
            i.obligatorio = obligatorio
            i.semestre = semester.get()
            i.creditos = credits.get()
            i.estado = estado
            messagebox.showinfo('Curso editado',f'Se ha editado correctamente el curso {i.nombre}!')
            #Restar the values
            code.set('')
            name.set('')
            pre.set('')
            optional.set('')
            semester.set('')
            credits.set('')
            state.set('')
            break
            
