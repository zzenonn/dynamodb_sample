#!/usr/bin/env python3
import boto3

def create_table(
        ddb_table_name,
        partition_key,
        sort_key,
        lsi
        ):

    dynamodb = boto3.resource('dynamodb')

    # The variables below transform the arguments into the parameters expected by dynamodb.create_table.

    table_name = ddb_table_name
    
    attribute_definitions = [
        {'AttributeName': partition_key, 'AttributeType': 'S'},
        {'AttributeName': sort_key, 'AttributeType': 'S'},
        {'AttributeName': lsi, 'AttributeType': 'S'}
        ]
    
    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}, 
                  {'AttributeName': sort_key, 'KeyType': 'RANGE'}]
                  
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    
    local_secondary_indexes = [{
            'IndexName': 'album_index',
            'KeySchema': [
                {'AttributeName': partition_key, 'KeyType': 'HASH'},
                {'AttributeName': lsi, 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'ALL'},
    }]
    
    try:
        # Create a DynamoDB table with the parameters provided
        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      LocalSecondaryIndexes=local_secondary_indexes
                                      )
        return table
    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))
        
def delete_table(name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(name)
    table.delete()

if __name__ == '__main__':
    music_table = create_table("music", "artist", "song", "album")
    
    # delete_table("music")
