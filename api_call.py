import requests
import os
import json
import shutil


def download_file(img_link, audio_link, type, index):
    folder_path = 'DescribeImage/' + type
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    pic_response = requests.get(img_link, stream=True)
    with open(folder_path + '/' + str(index) + '.jpg', 'wb') as img_file:
        shutil.copyfileobj(pic_response.raw, img_file)

    audio_response = requests.get(audio_link, stream=True)
    with open(folder_path + str(index) + '.mp3', 'wb') as audio_file:
        shutil.copyfileobj(audio_response.raw, audio_file)
    del pic_response, audio_response
    
url = "https://ptestudy.com/pteadmin/api/question/questionResNovalid.php?handle=questionList"

for i in range(1, 275):
    post_result = requests.post(url, data={"pageSize":1,"currentPage":i, "type":33, "free":1}).content
    resp = json.loads(post_result)
    img_link = resp['data'][0]['qimage']
    audio_link = resp['data'][0]['qaudio']
    chart_type = resp['data'][0]['keywords']
    download_file(img_link, audio_link, chart_type, i)

