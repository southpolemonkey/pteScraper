import requests
import os
import json
import shutil


def download_file(audio_link, index):
    folder_path = 'WriteFromDictation/'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    audio_response = requests.get(audio_link, stream=True)
    with open(folder_path + str(index) + '.mp3', 'wb') as audio_file:
        shutil.copyfileobj(audio_response.raw, audio_file)
    del audio_response


url = "https://ptestudy.com/pteadmin/api/question/questionResNovalid.php?handle=questionList"
f = open('wfd.txt', 'w')
for i in range(1, 393):
    post_result = requests.post(url, data={"pageSize":1,"currentPage":i, "type":18, "free":1}).content
    resp = json.loads(post_result)
    audio_link = resp['data'][0]['qaudio']
    text = resp['data'][0]['keywords'].split('.')[1]
    try:
        f.write(text + '\n')
    except UnicodeEncodeError:
        f.write(str(i) + '\n')
    download_file(audio_link, i)
    print(f'No.{i} has finished')
f.close()
