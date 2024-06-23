import os
from django.shortcuts import render
from dotenv import load_dotenv
from googleapiclient.discovery import build
from django.http import JsonResponse
# Create your views here.

load_dotenv()
API_KEY = os.getenv('YOUTUBE_API')

youtube = build('youtube', 'v3', developerKey=API_KEY)


def respond_json(request):
    playlist_id = "PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU"

    # To fetch details of a playlist we need to use PlaylistItems
    # https://developers.google.com/youtube/v3/docs/playlistItems
    total_duration = 0  # total duration of playlist initialized to 0
    nextPageToken = None
    json_obj = {"items": []}
    while True:
        pl_query = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        )
        pl_response = pl_query.execute()
        # print(json.dumps(pl_response, indent=2))
        # break
        # pl_response contains a list of videos which matches the criteria of pl_query

        # print(json.dumps(pl_response['items'], indent=2))

        # storing all videoIds in this list
        video_ids = [id['contentDetails']['videoId'] for id in pl_response['items']]
        # print(video_ids)
        # print(len(video_ids))
        video_query = youtube.videos().list(
            part="contentDetails, snippet",
            id=",".join(video_ids),
            # maxResults=5
        )
        video_resp = video_query.execute()
        # print(json.dumps(video_resp, indent=2))
        # break
        json_obj['items'].extend(video_resp['items'])
        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break
    return JsonResponse(json_obj, safe=False)
# respond_json(request)