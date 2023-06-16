from django.shortcuts import render
from .utils.calma_model import CalmaModel
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .apps import DetectEmotionConfig
import json
import random
import pathlib
from django.conf import settings
import os
# Create your views here.


class CurhatAPI(APIView):
    parser_classes = (MultiPartParser,)
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        wav_file = request.FILES['audio'].file
        emotion = DetectEmotionConfig.detect_model.predict_long_audio(wav_file)
        with open(pathlib.Path("detect_emotion/response.json")) as file:
            responses = json.load(file)
            response = {}
            video_list = responses['video'][emotion]
            text_list = responses['text'][emotion]
            response['emotion'] = emotion
            if len(video_list) != 0:
                response['type'] = 'video'
                response['data'] = random.choice(video_list)
            elif len(text_list) != 0:
                response['type'] = 'text'
                response['data'] = random.choice(text_list) 
            else:
                response['type'] = 'text'
                response['data'] = f"You are feeling {emotion} right now"
            # response = json.dumps(response)
            return Response(response)

