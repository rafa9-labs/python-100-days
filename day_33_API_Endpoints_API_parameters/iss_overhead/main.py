import requests
import math
from datetime import datetime
from datetime import timezone
my_email =  "rafa.plamdeala@gmail.com"
recp_email = "jonnydeep2323@outlook.com"
my_password = "qpir kfww ocfi dpku"


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1]
sunset = data["results"]["sunset"].split("T")[1]

# time_now = datetime.now()

sunrise_time = datetime.strptime(sunrise, "%H:%M:%S%z").timetz()
sunset_time = datetime.strptime(sunset, "%H:%M:%S%z").timetz()
now_time = datetime.now(timezone.utc).timetz()

def check_nighttime(sunrise_time, sunset_time, now_time):
    if sunset_time <= now_time < sunrise_time:
        return True
    else:
        print("Its day time.. you won't be able to see it.")
        return False
    
def check_if_close(iss_lat, iss_lng, cur_lat, cur_lng, proximity=5):
    # lat_min, lat_max = math.floor(cur_lat), math.ceil(cur_lat)
    # lng_min, lng_max = math.floor(cur_lng), math.ceil(cur_lng)
    # if lat_min <= iss_lat <= lat_max and lng_min <= iss_lng <= lng_max:
    if cur_lat - proximity <= iss_lat <= cur_lat + proximity and cur_lng - proximity <= iss_lng <= cur_lng + proximity:
        print("Look at the sky the ISS is above you.")
        return True
    else:
        print("ISS is not above you.")
        return False
       
# if check_nighttime(sunrise_time, sunset_time, now_time):
#     check_if_close(iss_latitude, iss_longitude, iss_latitude, iss_longitude) 
    
def send_email():
    import smtplib

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recp_email,
        msg="Subject: ISS NOTIFICATION\n\n Look at the sky the ISS is above you."
    )
    connection.close()
    
    
def execute_every60():
    import time
    while True:
        if check_nighttime(sunrise_time, sunset_time, now_time):
            if check_if_close(iss_latitude, iss_longitude, MY_LAT, MY_LONG):
        # if check_if_close(iss_latitude, iss_longitude, iss_latitude, iss_longitude):
                send_email()
        time.sleep(60)

execute_every60()
        
# def main() -> None:
#     if check_nighttime():
#         check_if_close()
#     pass


# if __name__ == "__main__":
#     main()
    



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



