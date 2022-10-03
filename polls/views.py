from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd 
import requests as req
from io import StringIO
from .models import Choice, Question
from django.template import loader
from django.urls import reverse



def getdata(request):
    #page = req.get(url)
    #page_df= pd.read_csv(StringIO(page.text),skiprows=10,sep='\t')
    #page_df.columns= ['Year','Month','Day', 'UTC Hour','PM2.5','PM10_mask','Retrospective']     
    #page_df = page_df[["Year","Month","PM2.5"]]
    #page_df = page_df[(page_df["Year"].isin([2018,2019,2020,2021,2022])) & (page_df["Month"].isin([3,4,5]))]
    #page_df = page_df.groupby(["Year","Month"])
    #page_df = page_df["PM2.5"].mean()
    #df = pd.DataFrame(data=page_df)
    #pivot = df.pivot_table(columns="Year",index="Month",values="PM2.5")
    #global data 
    #data = pivot.to_html()
    #return HttpResponse(data)
    #return render(request, 'polls/getdata.html', context)
    url_list = Choice.objects.all()
    context= {
        "url_list" : url_list,
    }
    return render(request, 'polls/getdata.html', context)

#page that displays question text for poll
def detail(request, question_id): 
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.save()
    context = { 'selected_choice': selected_choice,}
    return HttpResponseRedirect(reverse('results', args=(question.id,)),context)

def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

