import boto3
import requests

r=requests.get("")

client=boto3.client('rekognition',region_name='',aws_access_key_id = "",aws_secret_access_key = "")

resp=client.detect_faces(Image={'Bytes':r.content},Attributes=['ALL'])
#print(resp)

for i in resp["FaceDetails"]:
  print("The person is a "+str(i["Gender"]["Value"]+" with a confidence of "+str(i["Gender"]["Confidence"])))
  print("The person's age is approximately "+str(i["AgeRange"]))
