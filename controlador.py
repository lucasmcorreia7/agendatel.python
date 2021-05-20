'''
Agenda simples
'''
__author__ - 'Lucas Correia'
__license__= 'UNP'
__version__= '0.0.1'
__status__ ='Development'

from telefone import Telefone

class Controller():
   def inserir (nome, telefone):
    return Telefone (nome, telefone)
def listarAll(listaTelefone):
     for tel in listaTelefone:
   print('{} | {}'.format(tel.getNome(), tel.getTelefone()))
  
   def listarNome(listaTelefone, nome):
       cont =0
       for tel in listaTelefone:
      if tel.getNome() == nome:
          print('{} | {} '). '.format(tel.getNome(), tel.getTelefone()))
         break
        cont += 1

  def listarNome (listaTelefone, nome):
         if len(ListaTelefone) != 0:
             listaTelefone.clear()
             return ' Todos os contatos foram removidos!'
         else:
             return 'A lista telefonica está vazia!'

  def deletarNome(selflistaTelefone, nome):
      if len(ListaTelefone) != 0:
          cont= 0
          for tel in listaTelefone:
         if tel.getNome() ==nome:
             listaTelefone.pop(cont)
             return 'Contado {} removido com sucesso!'.format(nome)
         else:
             return 'Nome não encontrado!'
      else:
      return 'Lista está vazia!'
                    ''