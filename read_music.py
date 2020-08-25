#!/usr/bin/env python3
import threading
import boto3
from boto3.dynamodb.conditions import Key

def query_artist_songs(artist):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('music')
    response = table.query(
        KeyConditionExpression=Key('artist').eq(artist)
    )
    return response['Items']
    
def query_song_info(artist, song):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('music')
    response = table.query(
        KeyConditionExpression=Key('artist').eq(artist) & 
                               Key('song').eq(song)
    )
    return response['Items']
    
# Will not work because album is not a key
def query_album_songs(album):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('music')
    response = table.query(
        KeyConditionExpression=Key('album').eq(album)
    )
    return response['Items']

if __name__ == '__main__':
    print(query_song_info("Taylor Swift", "Cardigan"))
    