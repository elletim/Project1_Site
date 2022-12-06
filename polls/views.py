from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pandas as pd 
import requests as req
from io import StringIO
from .models import Choice, Question
from django.urls import reverse
import json
import statistics 


#page that displays question text for poll
def detail(request, question_id): 
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.save()
    urlname = selected_choice.choice_url
    page = req.get(urlname)
    page_df= pd.read_csv(StringIO(page.text),skiprows=10,sep='\t')
    page_df.columns= ['Year','Month','Day', 'UTC Hour','PM2.5','PM10_mask','Retrospective']     
    page_df = page_df[["Year","Month","PM2.5"]]
    page_df = page_df[(page_df["Year"].isin([2018,2019,2020,2021,2022])) & (page_df["Month"].isin([3,4,5,6]))]
    page_df = page_df.groupby(["Year","Month"])
    page_df = page_df["PM2.5"].mean()
    df = pd.DataFrame(data=page_df)
    y = df["PM2.5"].to_list()
    y = [round(i,2) for i in y]
    avg = statistics.mean(y)
    avg = [avg] * len(y)
    x = df.index.values
    x = list(x)
    x = [str(i) for i in x]
    x = [i.replace(',','/').replace(' ','') for i in x]
    context= { 'y' : y, 'x': json.dumps(x), 'question' : question, 'city': selected_choice,'avg': avg }
    return render(request, 'polls/vote.html', context)

