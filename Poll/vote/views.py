from vote.models import Question,Option,Voter
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')


@login_required()
def addq(request):
    if request.method == 'POST':
        question=request.POST['question']
        questn=Question(question=question,qid=request.user)
        questn.save()
        return redirect('add')
        
            

    return render(request,'addq.html')


@login_required()
def add(request):
    if request.method == 'POST':
        Questn=get_object_or_404(Question,qid=request.user)
        oplinks= request.POST.getlist('link')
        opnames= request.POST.getlist('name')
        for index in range(len(oplinks)):
            opn=Option(link=oplinks[index],name=opnames[index],quest=Questn)
            opn.save()
        return redirect('stats')
            

    return render(request,'add.html')


@login_required()
def stats(request):
    data=get_object_or_404(Question,qid=request.user)
    vote=Voter.objects.all().filter(vote=data)
    context={
        'data':data,
        'vote':vote,
    }
    return render(request,'stats.html',context)


def join(request):
    if request.method == 'POST':
        username=request.POST['Username']
        if  username==None:
            messages.info(request,'Please Fill All the Details')
            return redirect('join')
        else:
            request.session['username']=username
            return redirect('submit')

    return render(request,'join.html')


def submit(request):
    ok=request.session['username']
    u=get_object_or_404(User,username=ok)
    print(u)
    qst=get_object_or_404(Question,qid=u)
    print(qst.question)
    option=Option.objects.all().filter(quest=qst)
    for op in option:
        print(op.name)
        print(op.link)
        
    context = {
        'question': qst,
        'option': option,
    }
    if request.method =='POST':
        opname = request.POST['opt']
        email=request.POST['email']
        name=request.POST['name']

        vote=Voter(opname=opname,email=email,vname=name,vote=qst)
        vote.save()
        return redirect('/')

    return render(request,'submit.html',context)



def create(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('create')
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            user = auth.authenticate(username=username,password=password)
            auth.login(request, user)
            print('user created')
            return redirect('addq')

    return render(request,'create.html')


def manage(request):
    if request.method =='POST':
        username =request.POST['Username']
        password =request.POST['Password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('stats')
        else:
            messages.info(request,'invalid credentials')
            return redirect('manage')
    else:
        return render(request,'manage.html')


              

            
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def delt(request):
    user=User.objects.get(username=request.user)
    user.delete()

    return redirect('/')