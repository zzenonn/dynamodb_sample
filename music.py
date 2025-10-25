#!/usr/bin/env python3
"""
DynamoDB Table Creation and Management

This module demonstrates how to create and delete DynamoDB tables with:
- Composite primary keys (partition key + sort key)
- Local Secondary Indexes (LSI) for alternative query patterns
- Pay-per-request billing for cost optimization

Learning Objectives:
- Understand DynamoDB table structure and key concepts
- Learn how to define attribute types and key schemas
- Implement Local Secondary Indexes for flexible querying
"""

import boto3

def create_table(ddb_table_name, partition_key, sort_key, lsi):
    """
    Creates a DynamoDB table with a composite primary key and Local Secondary Index.
    
    Key Concepts Explained:
    - Partition Key (HASH): Determines which partition the item is stored in
    - Sort Key (RANGE): Sorts items within the same partition
    - LSI: Allows querying by partition key + different sort attribute
    
    Args:
        ddb_table_name (str): Name of the DynamoDB table to create
        partition_key (str): Primary partition key attribute name
        sort_key (str): Primary sort key attribute name  
        lsi (str): Local Secondary Index sort key attribute name
        
    Returns:
        boto3.resources.base.ServiceResource: DynamoDB table resource
    """
    
    # Step 1: Create DynamoDB resource client
    # This establishes connection to DynamoDB service in specified region
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Step 2: Define attribute definitions
    # Only attributes used in keys or indexes need to be defined
    # 'S' = String data type (other options: 'N' for Number, 'B' for Binary)
    attribute_definitions = [
        {'AttributeName': partition_key, 'AttributeType': 'S'},  # Artist name
        {'AttributeName': sort_key, 'AttributeType': 'S'},      # Song title
        {'AttributeName': lsi, 'AttributeType': 'S'}            # Album name
    ]
    
    # Step 3: Define primary key schema
    # HASH = partition key (determines data distribution)
    # RANGE = sort key (enables range queries within partition)
    key_schema = [
        {'AttributeName': partition_key, 'KeyType': 'HASH'},    # artist
        {'AttributeName': sort_key, 'KeyType': 'RANGE'}        # song
    ]
                  
    # Step 4: Configure Local Secondary Index
    # LSI shares same partition key but uses different sort key
    # Enables queries like "find all songs by artist X in album Y"
    local_secondary_indexes = [{
        'IndexName': 'album_index',
        'KeySchema': [
            {'AttributeName': partition_key, 'KeyType': 'HASH'},  # Same partition key
            {'AttributeName': lsi, 'KeyType': 'RANGE'}           # Different sort key (album)
        ],
        'Projection': {'ProjectionType': 'ALL'},  # Include all attributes in index
    }]
    
    try:
        # Step 5: Create the DynamoDB table
        # PAY_PER_REQUEST: Only pay for actual read/write operations
        # Alternative: PROVISIONED (pre-allocated capacity)
        table = dynamodb.create_table(
            TableName=ddb_table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            BillingMode='PAY_PER_REQUEST',
            LocalSecondaryIndexes=local_secondary_indexes
        )
        
        print(f"Table '{ddb_table_name}' creation initiated successfully")
        print("Table is being created... This may take a few moments")
        return table
        
    except Exception as err:
        print(f"Table '{ddb_table_name}' could not be created")
        print(f"Error details: {err}")
        return None

def delete_table(name):
    """
    Deletes a DynamoDB table and all its data.
    
    WARNING: This operation is irreversible!
    
    Args:
        name (str): Name of the table to delete
    """
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table(name)
        table.delete()
        print(f"Table '{name}' deletion initiated")
        print("Table is being deleted... This may take a few moments")
    except Exception as err:
        print(f"Failed to delete table '{name}': {err}")

if __name__ == '__main__':
    """
    Main execution block - demonstrates table creation
    
    This creates a music table with:
    - Primary key: artist (partition) + song (sort)
    - LSI: artist (partition) + album (sort) for album-based queries
    """
    print("Creating DynamoDB music table...")
    music_table = create_table("music", "artist", "song", "album")
    
    # Uncomment the line below to delete the table
    # WARNING: This will permanently delete all data!
    # delete_table("music")
