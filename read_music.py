#!/usr/bin/env python3
"""
DynamoDB Query Operations Example

This module demonstrates different query patterns in DynamoDB:
- Querying by partition key only
- Querying by partition key + sort key (exact match)
- Querying using Local Secondary Index (LSI)

Learning Objectives:
- Understand DynamoDB query vs scan operations
- Learn how to use KeyConditionExpression for efficient queries
- Practice querying with Local Secondary Indexes
- Handle query responses and extract data
"""

import boto3
from boto3.dynamodb.conditions import Key

def query_artist_songs(artist):
    """
    Query all songs by a specific artist using partition key only.
    
    This demonstrates a partition key query - retrieves all items
    that share the same partition key value.
    
    Query Pattern: artist = 'Lady Gaga'
    Returns: All songs by Lady Gaga
    
    Args:
        artist (str): The artist name to search for
        
    Returns:
        list: List of all songs by the specified artist
    """
    # Step 1: Create DynamoDB resource connection
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    # Step 2: Get table reference
    table = dynamodb.Table('music')
    
    # Step 3: Execute query using partition key
    # KeyConditionExpression: Specifies the key condition for the query
    # Key('artist').eq(artist): Matches items where artist equals the provided value
    response = table.query(
        KeyConditionExpression=Key('artist').eq(artist)
    )
    
    # Step 4: Extract and return items from response
    # DynamoDB returns metadata along with items, we only need 'Items'
    return response['Items']
    
def query_song_info(artist, song):
    """
    Query specific song information using both partition key and sort key.
    
    This demonstrates an exact match query - retrieves a specific item
    using both primary key components.
    
    Query Pattern: artist = 'Taylor Swift' AND song = 'Cardigan'
    Returns: Specific song details
    
    Args:
        artist (str): The artist name (partition key)
        song (str): The song name (sort key)
        
    Returns:
        list: List containing the specific song (should be 0 or 1 item)
    """
    # Note: Different region used here - ensure consistency in real applications
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('music')
    
    # Execute query with both partition key and sort key
    # & operator combines multiple key conditions
    response = table.query(
        KeyConditionExpression=Key('artist').eq(artist) & 
                               Key('song').eq(song)
    )
    return response['Items']
    
def query_album_songs(artist, album):
    """
    Query all songs by an artist from a specific album using Local Secondary Index.
    
    This demonstrates LSI usage - queries using the same partition key
    but a different sort key (album instead of song).
    
    Query Pattern: artist = 'Taylor Swift' AND album = 'Folklore'
    Returns: All songs by Taylor Swift from the Folklore album
    
    Args:
        artist (str): The artist name (partition key)
        album (str): The album name (LSI sort key)
        
    Returns:
        list: List of all songs by the artist from the specified album
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('music')
    
    # Execute query using Local Secondary Index
    # IndexName: Specifies which index to query (defined in table creation)
    # The LSI allows us to query by artist + album instead of artist + song
    response = table.query(
        IndexName='album_index',  # Use the LSI we created in music.py
        KeyConditionExpression=Key('artist').eq(artist) & 
                               Key('album').eq(album)
    )
    return response['Items']

if __name__ == '__main__':
    """
    Main execution block - demonstrates different query patterns
    
    Uncomment different function calls to test various query operations:
    1. Query by artist only (partition key query)
    2. Query specific song (partition + sort key query)  
    3. Query by album using LSI (partition key + LSI sort key query)
    """
    
    print("DynamoDB Query Examples")
    print("=" * 50)
    
    # Example 1: Query all songs by an artist
    print("\n1. All songs by Lady Gaga:")
    try:
        gaga_songs = query_artist_songs("Lady Gaga")
        for song in gaga_songs:
            print(f"   - {song['song']} ({song['album']}, {song['year']})")
    except Exception as err:
        print(f"   Error querying Lady Gaga songs: {err}")
    
    # Example 2: Query specific song information
    # Uncomment to test:
    # print("\n2. Specific song info - Taylor Swift's Cardigan:")
    # try:
    #     cardigan_info = query_song_info("Taylor Swift", "Cardigan")
    #     if cardigan_info:
    #         song = cardigan_info[0]
    #         print(f"   Song: {song['song']}")
    #         print(f"   Album: {song['album']}")
    #         print(f"   Year: {song['year']}")
    #     else:
    #         print("   Song not found")
    # except Exception as err:
    #     print(f"   Error querying specific song: {err}")
    
    # Example 3: Query songs from specific album using LSI
    # Uncomment to test:
    # print("\n3. All Taylor Swift songs from Folklore album:")
    # try:
    #     folklore_songs = query_album_songs("Taylor Swift", "Folklore")
    #     for song in folklore_songs:
    #         featured = f" (feat. {', '.join(song['feat'])})" if 'feat' in song else ""
    #         print(f"   - {song['song']}{featured}")
    # except Exception as err:
    #     print(f"   Error querying album songs: {err}")
    
    print("\nQuery operations completed!")
    
    # Additional Notes for Students:
    # - query() is more efficient than scan() for retrieving specific data
    # - Always use KeyConditionExpression for queries (not FilterExpression for keys)
    # - LSI queries count against the same partition's capacity
    # - Consider using Global Secondary Index (GSI) for different partition keys
    
