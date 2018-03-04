from weather import Weather
weather = Weather()

location = weather.lookup_by_location('delhi')
condition = location.condition()
print(condition)