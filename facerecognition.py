import boto3
import io


class FaceRecognition:
    s3 = boto3.resource('s3')
    rekognition = boto3.client('rekognition', region_name='eu-west-1')
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')

    def upload_img(self, image, name):
        stream = io.BytesIO()
        image.save(stream, format="JPEG")
        file = stream.getvalue()
        object = self.s3.Object('blue-faces', 'index/' + name + ".jpeg")
        object.put(Body=file,
                         Metadata={'FullName': name}
                         )
        print("Sending face to database complete.")

    def compare_img(self, image):
        stream = io.BytesIO()
        image.save(stream, format="JPEG")
        image_binary = stream.getvalue()
        try:
            response = self.rekognition.search_faces_by_image(
                CollectionId='face_collection',
                Image={'Bytes': image_binary}
            )
            if response['FaceMatches']:
                face = self.dynamodb.get_item(
                    TableName='face_collection',
                    Key={'RekognitionId': {'S': response['FaceMatches'][0]['Face']['FaceId']}}
                )

                if 'Item' in face:
                    print(face['Item']['FullName']['S'], response['FaceMatches'][0]['Face']['Confidence'])
                    return face['Item']['FullName']['S']
                else:
                    print('No match found in face database.')
                    return None
            else:
                print("Face matches empty.")
                return None
        except:
            print("No face Found in the Image.")
            exit(1)