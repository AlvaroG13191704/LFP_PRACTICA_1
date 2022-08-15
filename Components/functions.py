from tkinter import messagebox
from tkinter.filedialog import askopenfile
from Components.subject import Subject

def select_file(self):
    # We open the file
    self.open_file = askopenfile(mode='r+')
    # Chekend if there is a file
    if not self.open_file:
        return
    # If the same file has already been opened only return
    if self._var.get() == self.open_file.name:
        return
    # Open the file
    with open(self.open_file.name, 'r+',encoding='utf-8') as file:
        # We read the file
        files = file.read()
        print(files)

        data = []
        nums = []
        new_nums = []
        new = []
        # Split each course, then asign to a void list -> data
        response = files.split('\n')
        #Delete void lines
        for i in response:
            if i == '':
                response.remove(i)
        #Split each value of each array
        for i in response:
            data.append(i.split(','))
        # First fill a list with only the code of the courses
        for i in data:
            nums.append(i[0])
        # If the code is duplicated, only use the first of them
        for i in range(len(nums)):
            if nums[i] not in new_nums:
                new_nums.append(nums[i])
                new.append(data[i])
        print(new)
        # Iterate data to convert each value of each list an object Subject, then asign to self.subjects
        for i in new:
            # print(f' {i[0],i[1],str(i[2]),i[3],i[4],i[5],i[6]} ')
            obj = Subject(i[0], i[1], i[2], i[3],i[4],i[5],i[6])
            self.subjects.append(obj)

        # Change the rute
        self._var.set(file.name)
        messagebox.showinfo(
            'Selección de archivo', 'Se ha cargado y leido correctamente el archivo.')


def add_an_existing_subject(self, code, name, optional, semester, state, pre, credits):
    obligatorio = ''
    estado = ''

    # Transform the values
    if optional.get() == 'Opcional':
        obligatorio = '0' 
    elif optional.get() == 'Obligatorio':
        obligatorio = '1'
    
    if state.get() == 'Aprobado':
        estado = '0'
    elif state.get() == 'Cursando':
        estado = '1'
    elif state.get() == 'Pendiente': 
        estado = '-1'

    if len(self.subjects) > 0:
        for i in self.subjects:
            if i.codigo == code.get():
                messagebox.showerror(
                    'Agregar Curso',
                    f'Curso con código {i.codigo} ya existe. Se Eliminará y Reemplazará '
                )
                self.subjects.remove(i)
                # Add Course
                obj = Subject(code.get(), name.get(), pre.get(), obligatorio, semester.get(), credits.get(), estado)
                self.subjects.append(obj)
                # Restart
                code.set('')
                name.set('')
                pre.set('')
                optional.set('')
                semester.set('')
                credits.set('')
                state.set('')
                obligatorio = ''
                estado = ''
                break
            else:
                # If there not an existing subject, we validate and add to the list
                # Add Course
                obj = Subject(code.get(), name.get(), pre.get(), obligatorio, semester.get(), credits.get(), estado)
                self.subjects.append(obj)
                # Restart
                code.set('')
                name.set('')
                pre.set('')
                optional.set('')
                semester.set('')
                credits.set('')
                state.set('')
                obligatorio = ''
                estado = ''
                messagebox.showinfo(
                    'Agregar Curso',
                    f'Se ha agregado el curso con código{obj.codigo} correctamente!.'
                )
                break
    else:
       # If there not an existing subject, we validate and add to the list
        # Add Course
        obj = Subject(code.get(), name.get(), pre.get(),obligatorio, semester.get(), credits.get(), estado)
        self.subjects.append(obj)
        # Restart
        code.set('')
        name.set('')
        pre.set('')
        optional.set('')
        semester.set('')
        credits.set('')
        state.set('')
        obligatorio = ''
        estado = ''
        messagebox.showinfo(
            'Agregar Curso',
            f'Se ha agregado el curso con código{obj.codigo} correctamente!.'
        )
def select_and_show_course(self, code, name, optional, semester, state, pre, credits,comboget):
    for i in self.subjects:
        if i.nombre == comboget:
            code.set(f'Código: {i.codigo}')
            name.set(f'Nombre: {i.nombre}')
            pre.set(f'Pre requisito: {i.preRequisito}')
            optional.set(f'Opcionalidad: {i.obligatorio}')
            semester.set(f'Semestre: {i.semestre}')
            credits.set(f'Créditos: {i.creditos}')
            state.set(f'Estado: {i.estado}')

def edit_subject(self, code, name, optional, semester, state, pre, credits):
    # Var
    obligatorio = ''
    estado = ''

    # Transform the values
    if optional.get() == 'Opcional':
        obligatorio = '0' 
    elif optional.get() == 'Obligatorio':
        obligatorio = '1'
    
    if state.get() == 'Aprobado':
        estado = '0'
    elif state.get() == 'Cursando':
        estado = '1'
    elif state.get() == 'Pendiente': 
        estado = '-1'
    # Iterate through the subjects, find the course and edit their values
    for i in self.subjects:
        # If the code is equal to the code.get
        if i.codigo == code.get():
            # Edit
            i.codigo = code.get()
            i.nombre = name.get()
            i.preRequisito = pre.get()
            i.obligatorio = obligatorio
            i.semestre = semester.get()
            i.creditos = credits.get()
            i.estado = estado
            messagebox.showinfo('Curso editado',f'Se ha editado correctamente el curso {i.nombre}!')
            # Restar the values
            code.set('')
            name.set('')
            pre.set('')
            optional.set('')
            semester.set('')
            credits.set('')
            state.set('')
            obligatorio = ''
            estado = ''
            break
            
def approved_fun(self,approved_sub,cursing_sub,pending_sub):
    a = 0
    c = 0
    p = 0
    for i in self.subjects:
        if i.estado == 'Aprobado':
            a += int(i.creditos)
        elif i.estado == 'Cursando':
            c  += int(i.creditos)
        elif i.estado == 'Pendiente' and i.obligatorio == 'Obligatorio':
            p  += int(i.creditos)

    approved_sub.set(a)
    cursing_sub.set(c)
    pending_sub.set(p)
