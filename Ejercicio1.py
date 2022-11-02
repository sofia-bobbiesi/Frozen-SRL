import requests
class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}")
            data = response.json()
            temp = data["main"]["temp"]
            return temp > 300
        except Exception as e:
            print(e)
            return False