import requests
import pytest
import re
import random

import yaml


def ceart_list():
    """
    生成测试数据
    :return:
    """
    list = [(str(random.randint(11111, 99999)), str(random.randint(17100000000, 17999999999)), '波波') for x in range(2)]
    return list
class TestWework:
    @pytest.fixture(scope="session")
    def token(self):
        requests_params = {
            "corpid": "wwe6db0f80d8a1d222",
            "corpsecret": "f9HCV-usX3XwhdZrQyERnaiH1TEnDuformBqQ6U-ktQ"
        }
        res = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=requests_params)
        return res.json()['access_token']

    # def test_token(self):
    #     """
    #     获取token
    #      https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
    #       注：此处标注大写的单词ID和SECRET，为需要替换的变量，根据实际获取值更新。其它接口也采用相同的标注，不再说明。
    #     :return:
    #     """
    #     res=requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe6db0f80d8a1d222&corpsecret=f9HCV-usX3XwhdZrQyERnaiH1TEnDuformBqQ6U-ktQ')
    #     print(res.status_code)
    #     return res.json()['access_token']

    # def ceart_list():
    #     list = [(random.randint(111111, 999999), "aodi", str(random.randint(13800000000, 13999999999))) for x in range(2)] token, userid, mobile, name="星咖特购"
    # @pytest.mark.parametrize("userid,mobile,name",("bibi1","13520073055","小破孩"))
    def test_create(self, token, userid, mobile, name):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        requests_body = {
            "userid": userid,
            "name": name,
            "alias": "jackzhang",
            "mobile": mobile,
            "department": [1, 3]}
        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}',
                            json=requests_body)
        return res.json()

    def test_get(self, token, userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}')
        return res.json()

    def test_update(self, token, userid, name, mobile, department=None):
        """
        请求方式：POST（HTTPS）
         请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        if department == None:
            department = [1]
        requests_body = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile}
        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}',
                            json=requests_body)
        return res.json()

    def test_delete(self, token, userid='32909'):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        requests_params = {
            "access_token": token,
            "userid": userid}
        res = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=requests_params)
        # print(res.json())
        return res.json()
    @pytest.mark.parametrize("userid,mobile,name",ceart_list())
    def test_wework(self, token, userid, mobile, name):
        """
        整体测试
        :param token:
        :return:
        """
        try:
            assert self.test_create(token, userid, mobile, name)['errmsg'] == 'created'
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                assert self.test_create(token, userid, mobile,name) == 'created'
        # assert self.test_create(token, userid,mobile,name)['errmsg'] == 'created'
        assert self.test_get(token, userid)['errmsg'] == 'ok'
        assert self.test_update(token, userid, '伍佰1', '150010145677')['errmsg'] == 'updated'
        assert self.test_delete(token, userid)['errmsg'] == 'deleted'
        assert self.test_get(token, userid)['errcode'] == 60111

    def test_yaml(self):
        print(yaml.safe_load(open("date.yaml")))
