#!/usr/bin/env python3
import boto3

if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb')
    
    music_table = dynamodb.Table('music')
    
    songs = [ {
        'artist' : 'Taylor Swift',
        'song'   : 'Cardigan',
        'album'  : 'Folklore',
        'year'   : 2020
        },
        {
        'artist' : 'Taylor Swift',
        'song'   : 'The 1',
        'album'  : 'Folklore',
        'year'   : 2020
        },
        {
        'artist' : 'Taylor Swift',
        'song'   : 'Exile',
        'album'  : 'Folklore',
        'feat'   : ['Bon Iver'],
        'year'   : 2020
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Stupid Love',
        'album'  : 'Chromatica',
        'feat'   : ['지수', '제니', '로제', '리사'],
        'year'   : 2020
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Sour Candy',
        'album'  : 'Chromatica',
        'feat'   : ['지수', '제니', '로제', '리사'],
        'year'   : 2020
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Stupid Love',
        'album'  : 'Chromatica',
        'year'   : 2020
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Rain on Me',
        'album'  : 'Chromatica',
        'feat'   : ['Ariana Grande'],
        'year'   : 2020
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Perfect Illusion',
        'album'  : 'Joane',
        'year'   : 2016
        },
        {
        'artist' : 'Lady Gaga',
        'song'   : 'Million Reasons',
        'album'  : 'Joane',
        'year'   : 2016
        }
    ]
    
    for song in songs:
        music_table.put_item(Item = song)