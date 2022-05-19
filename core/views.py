from django.shortcuts import render

def index(request):
  print(dir(request.user))
  print(f"User: {request.user}")

  if str(request.user) == 'AnonymousUser':
    teste = 'Usuário não logado'
  else:
    teste = 'Usuário logado'

  context = {
    'curso': 'Programação Web com Django Framework',
    'outro': 'Django é Show!!',
    'logado': teste
  }

  return render(request, 'index.html', context)


def contato(request):
  return render(request, 'contato.html')