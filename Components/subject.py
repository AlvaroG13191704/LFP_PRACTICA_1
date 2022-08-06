

#Create a class who represent the a course of the career

class Subject():
    #Constructor
    def __init__(self,codigo,nombre,preRequisito,obligatorio,semestre,creditos,estado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__preRequisito = preRequisito
        self.__obligatorio = obligatorio
        self.__semestre = semestre
        self.__creditos = creditos 
        self.__estado = estado
    #Getters and Setters
    #Code
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo

    #name
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    #Prerequisito
    @property
    def preRequisito(self):
        return self.__preRequisito
        
    @preRequisito.setter
    def preRequisito(self,pre):
        self.__preRequisito = pre

    #Obligatorio
    @property
    def obligatorio(self):
        if self.__obligatorio == '1':
            return 'Obligatorio'
        elif self.__obligatorio == '0':
            return 'Opcional'

    @obligatorio.setter
    def obligatorio(self,obligatorio):
        self.__obligatorio = obligatorio

    #Semestre
    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self,semestre):
        self.__semestre = semestre
    
    #Creditos
    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self,creditos):
        self.__creditos = creditos
    
    #Estado
    @property
    def estado(self):
        if self.__estado == '0':
            return 'Aprobado'
        elif self.__estado == '1':
            return 'Cursando'
        elif self.__estado == '-1':
            return 'Pendiente'

    @estado.setter
    def estado(self,estado):
        self.__estado = estado

