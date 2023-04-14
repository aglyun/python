# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import asyncio
import sys

from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


a = "你阿里云的AccessKey ID"
b = "你阿里云的AccessKey Secret"


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=a,
            # 必填，您的 AccessKey Secret,
            access_key_secret=b
        )
        # 访问的域名
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=args[0],
            sign_name=args[1],
            template_code=args[2],
            template_param=args[3]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.send_sms_with_options(send_sms_request, runtime)
            print("发送成功")
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
            print("main发送失败", error)


    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 工程代码泄露可能会导致AccessKey泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=args[0],
            sign_name=args[1],
            template_code=args[2],
            template_param=args[3]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.send_sms_with_options_async(send_sms_request, runtime)

        except Exception as error:
            # 如有需要，请打印 error
            print(error)
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    lb = ["手机号", "归墟来信", "SMS_270375137", '{"code":"999999"}']
    Sample.main(lb)    # 传入列表即可调用
    print("发送成功")
