from weather import Weather
weather = Weather()

location = weather.lookup_by_location('roorkee')
condition = location.condition()
print(condition)