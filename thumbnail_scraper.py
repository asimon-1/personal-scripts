import shutil

import requests

responsecode = 200
stagenum = 1
while True:
    url = f"https://www.smashbros.com/assets_v2/img/stage/stage_addition_img{stagenum}.jpg"
    response = requests.get(url, stream=True)
    responsecode = response.status_code
    if responsecode == 200:
        print(f"Received response for stage {stagenum}")
        with open(f"stage_thumb_addition{stagenum}.jpg", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        stagenum += 1
    else:
        break
