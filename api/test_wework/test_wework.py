import json

import pytest
import requests


class TestWework:
    @pytest.fixture()
    def get_token(self):
        res=requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe6db0f80d8a1d222&corpsecret=f9HCV-usX3XwhdZrQyERnaiH1TEnDuformBqQ6U-ktQ')
        self.token=res.json()['access_token']
    def test_creat(self,get_token):

        res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',
                          json={
                                    "userid": "littlegoblin1",
                                    "name": "你是我的小妖2",
                                    "mobile": "13800138001",
                                    "department": [2]})
        print(res.json())
        assert res.json()['errmsg']=='created'
    def test_get(self,get_token):
        userid='littlegoblin1'
        res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}')
        print(res.json())
    def test_update(self,get_token):
        res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}',
                          json={
                                    "userid": "littlegoblin1",
                                    "name": "李四",
                                    "department": [2],
                                    "mobile": "13800000010"})
        print(res.json())
    def test_delete(self,get_token):
        userid='littlegoblin1'
        res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}')
        print(res.json())
