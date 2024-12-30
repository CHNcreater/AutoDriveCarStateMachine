# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import cv2
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from typing import List

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

from dataprovider.dp_camera import CameraDataProvider
from lib.ocr_image_preprocess import preprocess_image_for_ocr
from configuration import Configuration

class ObjectDetectionTextRecognition:
    def __init__(self):
        self.camera = CameraDataProvider()
        self.configuration = Configuration()
        self.api_key = self.configuration.get("ocr", "ALIBABA_CLOUD_ACCESS_KEY_ID")
        self.api_secret = self.configuration.get("ocr", "ALIBABA_CLOUD_ACCESS_KEY_SECRET")

    def capture_image(self):
        return self.camera.get_image()

    def run(self):
        self.camera.display_image()

    def create_client(self) -> ocr_api20210707Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=self.api_key,
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=self.api_secret
        )
        # Endpoint 请参考 https://api.aliyun.com/product/ocr-api
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = ObjectDetectionTextRecognition().create_client()
        image_content = preprocess_image_for_ocr(args[0])
        _, encoded_image = cv2.imencode('.jpg', image_content)
        recognize_basic_request = ocr_api_20210707_models.RecognizeBasicRequest(
            need_rotate=False,
            body=encoded_image.tobytes()
            # body=open(args[0], 'rb').read()
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.recognize_basic_with_options(recognize_basic_request, util_models.RuntimeOptions())
            print(response.body)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = ObjectDetectionTextRecognition.create_client()
        recognize_basic_request = ocr_api_20210707_models.RecognizeBasicRequest(
            url='your_value',
            need_rotate=False
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.recognize_basic_with_options_async(recognize_basic_request, util_models.RuntimeOptions())
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


# if __name__ == '__main__':
#     import time
#     start_time = time.time()
#     ObjectDetectionTextRecognition.main(sys.argv[1:])
#     end_time = time.time()
#     print(f"Program running time: {end_time - start_time} seconds")