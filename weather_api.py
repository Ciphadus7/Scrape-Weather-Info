import requests

def get_weather_single(city_name, API_KEY=''):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    content = r.json()
    city = city_name
    temps = content['main']
    temperature = temps['temp']
    condition = content['weather'][0]['description']
    with open('dataSingle.txt', 'w') as file:
        file.write("City - Temperature - Condition\n")
        file.write(f"{city} - {temperature} - {condition}")
        print('Text file has been created.(dataSingle.txt)')
        file.close()




def get_weather(city_name, API_KEY=''):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{city_name} {dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

    print('Text file has been appended.(data.txt)')



def main():
    while True:
        print("Would you like to look at the current weather(1) or the forecast for the next 5 days(2)? ")
        which = input("Enter (1) or (2) --> ")
        if which == '1':
            city =  input('Please enter a city\'s name: ')
            get_weather_single(city)
        elif which == '2':
            city =  input('Please enter a city\'s name: ')
            get_weather(city)
        elif KeyboardInterrupt:
            print('Closing script..Have a good day.')
            exit
        else:
            print('Please enter either (1) or (2).')
        
        goAgane = input('Would you like to execute the script again?(yes/no)\n-->').lower()
        if goAgane == 'yes':
            continue
        else:
            break
    



main()