import boto3

dynamodb = boto3.resource('dynamodb')

TableName = dynamodb.Table('PYgameTesting')

item_data = {
    'Class': '1C',
    'StudentID': '122',
    'Score': 0,
    'Ranking': 1
}

response = TableName.put_item(Item= item_data)

print(f"Put Item succeeded:\n{response}")
