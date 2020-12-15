import requests
import pytest
import random
@pytest.mark.run(order=1)
def test_bad():

    res=requests.get('http://www.baidu.com')
    print(res.status_code)
def test_creatlist():
    list=[(random.randint(11111, 99999), "波波", str(random.randint(17100000000, 17999999999))) for i in range(3)]
    print(list)
def test_url():
    res=requests.get('http://www.baidu.com')
    print(res.status_code)