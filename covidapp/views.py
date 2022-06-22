from logging import critical
from multiprocessing import context
from select import select
from django.shortcuts import render
import json
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

# querystring = {"country":"usa","day":"2020-06-02"}

headers = {
	"X-RapidAPI-Key": "10c3ca1159msh2a1a623f389750ep189c3ajsneabf6a98a83f",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry,'mylist': mylist,'new': new, 'active': active, "critical": critical, 'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request, 'helloworld.html', context) 
    
   
    context = {'mylist': mylist}
    return render(request, 'helloworld.html', context) 