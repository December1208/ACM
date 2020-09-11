import requests
import datetime
import time


class WxappletGeneraLog:
    headers = {'authorization':'Bearer eyJ0eXAiOiJqd3QiLCJhbGciOiJFZERTQSIsImtpZCI6Ii1nVHE4bEl3ZF9RbHhMVlVjM3RtM2RMU0RHWT0ifQ.eyJvaWQiOiI1ZjNiYjYxNmMzMzIzZGRmNGJmM2VmNmYiLCJ0aWQiOiJnQUFBQUFCZldZTUdSSGdaYnF4N19XLWtueXJuOEtueGI2NnJxMmRSeGdKRldOVU9USWdMRHp5NUhjVzYyT0h2VG41ZzdzbFhGZE81Y1M2YnRpVjZsWEdrVERTNTNuaGc5SF9oTHlOb0NveUktNHlncWphVEZSTExQNFNpem1YRjduX1cwYi1EckZ0aCIsImdyb3VwcyI6NCwic3ViIjoiNWYzYmI2MTZjMzMyM2RkZjRiZjNlZjcxIiwiZXhwIjoxNTk5Nzg4MTY2fQ.lpZMhduHIsX78eJ8gX657nLscYRwtVG-ApTicnUCkGTvQVMFpk0STX_iVYgsUxqGezlFpBBPzVnKbMdYp-s9Bg'}

    def generate_browse(self, position: str, tag: str):
        url = "https://api.gllue.net/vision/applet/browse_position"
        origin = {
            "scene": 1001,
            "sharetag": tag
        }
        params = {
            "position": position,
            "origin": origin
        }
        response = requests.post(
            url=url, json=params, headers=self.headers
        )

    def generate_share(self, position: str, tag: str):
        url = 'https://api.gllue.net/vision/applet/share_position'
        origin = {
            "scene": 1001,
            "sharetag": tag
        }
        params = {
            "position": position,
            "origin": origin
        }
        response = requests.post(
            url=url, json=params, headers=self.headers
        )

    def generate_apply(self, position: str, tag: str):
        url = 'https://api.gllue.net/vision/applet/apply_position'
        origin = {
            "scene": 1001,
            "sharetag": tag
        }
        params = {
            "position": position,
            "origin": origin
        }
        response = requests.post(
            url=url, json=params, headers=self.headers
        )

    def generate_stay(self, tag: str):
        url = "https://api.gllue.net/vision/applet/stay"
        origin = {
            "scene": 1001,
            "sharetag": tag
        }
        start = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        end = (datetime.datetime.now() + datetime.timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        target = "{\"page\":\"positionDetail\", \"id\":2}"
        response = requests.post(
            url=url,
            json={
                "target": target,
                "start": start,
                "end": end,
                "total": 7,
                "origin": origin
            },
            headers=self.headers
        )


if __name__ == '__main__':

    log = WxappletGeneraLog()
    for i in range(2):
        log.generate_browse(str(i+1), "f393a012")
        log.generate_share(str(i+1), "f393a012")
        log.generate_apply(str(i+1), "f393a012")
        log.generate_stay("f393a012")
