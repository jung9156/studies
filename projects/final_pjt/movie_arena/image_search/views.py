from django.shortcuts import render, redirect
import requests
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



# Create your views here.
def how(request):
    if request.method == 'POST':

        authenticator = IAMAuthenticator('RP9pUsl_Z-uZd4fTxaa78wlivZ1rQhpL_XZOekDD1mjn')
        assistant = AssistantV2(
            version='2020-04-01',
            authenticator = authenticator
        )
        assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/6d8c3435-9650-4202-af84-07fc845a4f34')
        response = assistant.message_stateless(
            assistant_id='c65c3c89-ac53-4651-be25-b7bb35015fb4',
            input={
                'message_type': 'text',
                'text': request.POST['msg'],
            }
        ).get_result()

        context = {
            'response': response,
        }
        return render(request, 'image_search/index.html', context)
        
    return render(request, 'image_search/index.html')