#!/usr/bin/env python3
"""
DynamoDB Data Insertion Example

This module demonstrates how to insert data into DynamoDB tables using:
- put_item() method for individual item insertion
- Batch operations for multiple items
- Proper data structure formatting for DynamoDB

Learning Objectives:
- Understand DynamoDB item structure and data types
- Learn how to insert items with varying attributes
- Practice batch data operations
- Handle optional attributes (like 'feat' for featured artists)
"""

import boto3

if __name__ == '__main__':
    """
    Main execution block - demonstrates data insertion into DynamoDB
    
    Key Concepts:
    - Items can have different attributes (schema-less design)
    - Primary key attributes (artist, song) must be present in every item
    - Additional attributes can vary between items
    """
    
    # Step 1: Create DynamoDB resource connection
    # Note: Region should match where your table was created
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    
    # Step 2: Get reference to existing table
    # This assumes the 'music' table already exists (created by music.py)
    music_table = dynamodb.Table('music')
    
    # Step 3: Define sample data
    # Each dictionary represents one item (row) in the table
    # Notice how some items have 'feat' attribute while others don't
    songs = [
        {
            'artist': 'Taylor Swift',    # Partition key - required
            'song': 'Cardigan',         # Sort key - required  
            'album': 'Folklore',        # Additional attribute
            'year': 2020                # Additional attribute
        },
        {
            'artist': 'Taylor Swift',
            'song': 'The 1',
            'album': 'Folklore',
            'year': 2020
        },
        {
            'artist': 'Taylor Swift',
            'song': 'Exile',
            'album': 'Folklore',
            'feat': ['Bon Iver'],       # Optional attribute - list of featured artists
            'year': 2020
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Stupid Love',
            'album': 'Chromatica',
            'feat': ['지수', '제니', '로제', '리사'],  # K-pop collaboration example
            'year': 2020
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Sour Candy',
            'album': 'Chromatica',
            'feat': ['지수', '제니', '로제', '리사'],
            'year': 2020
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Stupid Love',      # Note: Duplicate entry (same artist + song)
            'album': 'Chromatica',      # This will overwrite the previous entry
            'year': 2020
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Rain on Me',
            'album': 'Chromatica',
            'feat': ['Ariana Grande'],
            'year': 2020
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Perfect Illusion',
            'album': 'Joane',           # Different album for same artist
            'year': 2016
        },
        {
            'artist': 'Lady Gaga',
            'song': 'Million Reasons',
            'album': 'Joane',
            'year': 2016
        }
    ]
    
    # Step 4: Insert each item into the table
    # Using put_item() method - creates new item or replaces existing item
    print("Inserting songs into DynamoDB table...")
    
    for song in songs:
        try:
            # put_item() performs an "upsert" operation:
            # - If item doesn't exist: creates new item
            # - If item exists (same partition + sort key): replaces entire item
            response = music_table.put_item(Item=song)
            
            print(f"Inserted: {song['artist']} - {song['song']}")
            
        except Exception as err:
            print(f"Failed to insert {song['artist']} - {song['song']}: {err}")
    
    print("Data insertion completed!")
