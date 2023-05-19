from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from learning_logs.models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from .forms import TopicForm, EntryForm

def index(request): # página inicial
    return render(request, 'learning_logs/index.html')

@login_required(login_url='users:login')
def topics(request): # mostra todos os assuntos
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    
    return render(request, 'learning_logs/topics.html', context) 

@login_required(login_url='users:login')   
def topic(request, topic_id): #um único assunto e suas entradas
    topic = Topic.objects.get(id=topic_id) 
    check_topic_owner(request,topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'learning_logs/topic.html', context)

@login_required(login_url='users:login')     
def new_topic(request): # adiciona um novo assunto
    if request.method != 'POST': #nenhum dado submetido
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
    
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        
        return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required(login_url='users:login') 
def new_entry(request, topic_id):
    # Verifica se o tópico com o ID fornecido existe
    topic = get_object_or_404(Topic, id=topic_id)

    if request.method != 'POST':
        # Requisição GET - Cria um novo formulário de entrada.
        form = EntryForm()
    else:
        # Dados POST submetidos; processa os dados.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Cria um objeto Entry, mas não o salva no banco de dados.
            new_entry = form.save(commit=False)
            # Atribui o tópico ao qual a entrada se relaciona.
            new_entry.topic = topic
            # Salva o objeto Entry no banco de dados.
            new_entry.save()
            # Redireciona para a página do tópico relacionado.
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    # Exibe um formulário em branco ou inválido.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required(login_url='users:login') 
def edit_entry(request, entry_id): # edita uma entrada já existente
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
  
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
        
        
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404 
    