from config import *
import pytest
import requests


class TestYD:
    def setup_method(self):
        self.headers = {'Authorization': TOKEN}


    @pytest.mark.parametrize(
        'param, folder_name, status_code',
        (
                ('path', 'Python', 201),    #параметры проверки, что папка создалась
                ('path', 'Python', 409),    #параметры проверки, что папка существует
                ('put', 'Python', 400),     #параметры проверки с некорректными данными
        )
    )
    def test_create_folder(self, param, folder_name, status_code):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {param: folder_name}
        response = requests.put(url, params=params, headers=self.headers)

        assert response.status_code == status_code
