import requests
import time

def send_device_reading(url, file_path, payload):
    try:
        with open(file_path, 'rb') as file:
            files = {'image': (file_path, file)}
            data = payload

            #send the post request
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()

            #print if success
            print("Success:", response.status_code)
            print("Response content:", response.text)
    except response.exceptions.HTTPError as err:
        print("Error:", err)
    except Exception as err:
        print("Error:", err)

send_device_reading('http://127.0.0.1:8000/food_pic_processor/device_entries/', 'test_images/test_image_1.jpg', {'user': '1', 'diary': '1', 'meal': '1', 'ingredient': '1', 'quantity_grams': '550'})

time.sleep(10)

send_device_reading('http://127.0.0.1:8000/food_pic_processor/device_entries/', 'test_images/test_image_1', {'quantity_grams': '500'})
