import os, io
from numpy import random
from google.cloud import vision
from google.cloud.vision import types
from draw_vertice import drawVertices
import pandas as pd

# google credential
credential_path ="json File path"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = vision.ImageAnnotatorClient()

# -----------------Text Detection in Image----------------------
# def detect_text(file_path):
#     try:
#         with io.open(image_path,'rb') as image_file:
#             content = image_file.read()

#                 # create image instances
#         image = vision.types.Image(content=content)

#                 #to create response and json
#         response = client.text_detection(image=image)
#         texts = response.text_annotations

#         df = pd.DataFrame(columns=['locale','description'])

#         for text in texts:
#             df = df.append(
#                 dict(locale=text.locale,
#                     description=text.description
#                 ),
#                 ignore_index=True
#             )
#         return df
#         # print('Text Detection in images:')
#         # print(df['description'][0])
#     except Exception as e:
#         print(e)

# file_name = 'label.png'
# image_path = f'.\VisionApiDemo\images\{file_name}'


# -------------------------Handwritten Text-------------------------

# file_name = 'one.jpg'
# image_path = f'.\VisionApiDemo\images\{file_name}'



# with io.open(image_path,'rb') as image_file:
#     content = image_file.read()

# image = vision.types.Image(content=content)
# response = client.document_text_detection(image=image)
# docText = response.full_text_annotation.text
# print(docText)

# ---------------------------Labels Detections----------------------
# def detect_labels(file_path):
#     try:
#         with io.open(file_path,'rb') as image_file:
#             content = image_file.read()

#         image = vision.types.Image(content=content)
#         response = client.label_detection(image=image)
#         labels = response.label_annotations

#         df = pd.DataFrame(columns=['description','score','topicality'])

#         for label in labels:
#             df= df.append(
#                 dict(
#                     description=label.description,
#                     score = label.score,
#                     topicality =label.topicality
#                 ),
#                 ignore_index=True
#             )
#         return df
#     except Exception as e:
#         print(e)

# file_name = 'pict.png'
# image_path = f'.\VisionApiDemo\images\{file_name}'
# print('\nDetect the Labels from Given Images:\n ')
# print(detect_labels(image_path))

#----------------------------Landmark Detections---------------------

# def detect_landmark(file_path):
#     try:
#         with io.open(file_path,'rb') as image_file:
#             content = image_file.read()

#         image = vision.types.Image(content=content)
#         response = client.landmark_detection(image=image)
#         landmarks = response.landmark_annotations

#         df = pd.DataFrame(columns=['description', 'locations', 'score'])
#         for landmark in landmarks:
#             df = df.append(
#                 dict(
#                     description=landmark.description,
#                     locations=landmark.locations,
#                     score=landmark.sco
#                     ),
#                     ignore_index=True
#                 )
#         return df
#     except Exception as e:
#         print(e)


# file_name = 'all.jpg'
# image_path = f'.\VisionApiDemo\images\{file_name}'
# print('\nDetect the Landmarks from Given Images:\n ')
# print(detect_landmark(image_path))

# ---------------------------Logo Detections--------------------------


# def detect_logo(file_path):
#     try:
#         with io.open(file_path, 'rb') as image_file:
#             content = image_file.read()

#         image = vision.types.Image(content=content)
#         response = client.logo_detection(image=image)
#         logos = response.logo_annotations

#         for logo in logos:
#             print('Logo Description:', logo.description)
#             print('Confidence Score:', logo.score)
#             print('-'*50)
#             vertices = logo.bounding_poly.vertices
#             print('Vertices Values {0}'.format(vertices))
#             drawVertices(content, vertices, logo.description)
#     except Exception as e:
#         print(e)

# file_name = 'all.jpg'
# image_path = f'.\VisionApiDemo\images\{file_name}'

# print('\nDetect the Logo from Given Images:\n ')
# print(detect_logo(image_path)

# ------------------------------Face Detections-----------------------------

# file_name= 'geet.jpg'
# image_path = f'.\VisionApiDemo\images\{file_name}'

# with io.open(image_path, 'rb') as image_file:
#     content = image_file.read()

# image = vision.types.Image(content=content)
# response = client.face_detection(image=image)
# faceAnnotations = response.face_annotations

# likehood = ('Unknown', 'Very Unlikely', 'Unlikely', 'Possibly', 'Likely', 'Very Likely')

# print('Faces:')
# for face in faceAnnotations:
#     print('Detection Confidence {0}'.format(face.detection_confidence))
#     print('Angry likelyhood: {0}'.format(likehood[face.anger_likelihood]))
#     print('Joy likelyhood: {0}'.format(likehood[face.joy_likelihood]))
#     print('Sorrow likelyhood: {0}'.format(likehood[face.sorrow_likelihood]))
#     print('Surprised ikelihood: {0}'.format(likehood[face.surprise_likelihood]))
#     print('Headwear likelyhood: {0}'.format(likehood[face.headwear_likelihood]))

#     face_vertices = ['({0},{1})'.format(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
#     print('Face bound: {0}'.format(', '.join(face_vertices)))
#     print('')

    