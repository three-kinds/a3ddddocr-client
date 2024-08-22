# -*- coding: utf-8 -*-
import base64
from a3ddddocr_client import OCRClient


def get_base64(filename: str) -> str:
    with open(filename, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


if __name__ == '__main__':
    client = OCRClient(host="http://127.0.0.1:8000/")

    ocr_result = client.ocr(filename="./images/ocr.jpeg")
    print(f'ocr_result: {ocr_result}')

    slide_match_result = client.slide_match(target_filename="./images/target.png", background_filename="./images/backgroud.png")
    print(f'slide_match_result: {slide_match_result}')

    detection_result = client.detection(filename="./images/detection.png")
    print(f'detection_result: {detection_result}')

    print(f'BASE64')

    ocr_result = client.ocr(base64_image=get_base64("./images/ocr.jpeg"))
    print(f'ocr_result: {ocr_result}')

    slide_match_result = client.slide_match(base64_target=get_base64("./images/target.png"), base64_background=get_base64("./images/backgroud.png"))
    print(f'slide_match_result: {slide_match_result}')

    detection_result = client.detection(base64_image=get_base64("./images/detection.png"))
    print(f'detection_result: {detection_result}')
