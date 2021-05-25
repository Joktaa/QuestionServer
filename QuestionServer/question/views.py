from rest_framework.decorators import api_view
import json
import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
import random


# The function that get the questions
@api_view(['GET'])
def getQuestions(request):
    allQuestions = []
    finalQuestions = []
    try:
        # Opening JSON file
        f = open(os.path.join(settings.BASE_DIR, 'question/questions.json'))
        data = json.load(f)

        for key, value in data.items():
            allQuestions.append(value)
            # print ("Key == "+key+"  Value == "+ value)
        
        # Closing file
        f.close()

        while len(finalQuestions) < 1:
            ran = random.randint(0, 9)
            if(not questionExist(finalQuestions, allQuestions[ran])):
                finalQuestions.append(allQuestions[ran])
        
        return JsonResponse({
                'status': "success",
                'message': "Data found",
                'result': finalQuestions,
            }, status=status.HTTP_200_OK)

    except:
        return JsonResponse({
                'status': "error",
                'message': "Error occured while processing",
                'result': [],
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# check the question already exist in the final question list
def questionExist(finalQuestions, question):
    status = False
    for fq in finalQuestions:
        if(question == fq):
            status = True
            break
    return status



