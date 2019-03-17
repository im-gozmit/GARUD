import Android
import time

Mobile.Device('MyDevice').GPS.Location

def PostGPSLocation():
  Mobile.SetCurrent('MyDevice')
  # Check if GPS is enabled
  if Mobile.Device().GPS.GPSEnabled:
    # Obtain location data
    Longt = Mobile.Device().GPS.Location.Longitude
    Lat = Mobile.Device().GPS.Location.Latitude
    # Output the location data
    Log.Message('The device location is:')
    if Mobile.Device().OSType == 'Android':
      Log.Message('Longitude: ' + IntToStr(Longt))
      Log.Message('Latitude: ' + IntToStr(Lat))
      Log.Message('Altitude: ' + VarToStr(Mobile.Device().GPS.Location.Altitude))
      Log.Message('Accuracy: '+ VarToStr(Mobile.Device().GPS.Location.Accuracy))
    elif Mobile.Device().OSType == 'iOS':
      Log.Message('Longitude: ' + IntToStr(Longt))
      Log.Message('Latitude: ' + IntToStr(Lat))
      Log.Message('Altitude: ' + VarToStr(Mobile.Device().GPS.Location.Altitude))
      Log.Message('Speed: ' + VarToStr(Mobile.Device().GPS.Location.Speed))
      Log.Message('Horizontal Accuracy: ' + VarToStr(Mobile.Device().GPS.Location.HorizontalAccuracy))
      Log.Message('Vertical Accuracy: ' + VarToStr(Mobile.Device().GPS.Location.VerticalAccuracy))
    # Open Google Maps in the browser and pass the coordinates as URL parameters
    Browsers.Item[Browsers.btIExplorer].Run('http://maps.google.com/maps?q=loc:' + IntToStr(Lat) + ',' + IntToStr(Longt))



def MockGPSLocation():
  Mobile.SetCurrent('MyDevice')
  # Check if GPS is enabled
  if Mobile.Device().GPS.GPSEnabled:
    # Enable the "Allow mock locations" property
    Mobile.Device().GPS.AllowMockLocations = True
    # Obtain current location data
    Longt = Mobile.Device().GPS.Location.Longitude
    Lat = Mobile.Device().GPS.Location.Latitude
    # Output the location data
    Log.Message('The current device location is:')
    PostLocationData(Mobile.Device())
    # Open Google Maps in the browser and pass the current coordinates as URL parameters
    Browsers.Item[Browsers.btIExplorer].Run('http://maps.google.com/maps?q=loc:' + aqConvert.VarToStr(Lat) + ',' + aqConvert.VarToStr(Longt))
    # Change the coordinates
    Longt = Longt + 0.005
    Lat = Lat + 0.005
    # Specify a mock location
    if Mobile.Device().OSType == 'Android':
      Mobile.Device().GPS.SetLocation(Longt, Lat, Mobile.Device().GPS.Location.Altitude, Mobile.Device().GPS.Location.Accuracy)
    else:
      Mobile.Device().GPS.SetLocation(Longt, Lat)
    # Output the new location data
    Log.Message('The device mock location is:')
    PostLocationData(Mobile.Device())
    # Open a new tab in the browser
    Sys.Browser('iexplore').BrowserWindow(0).Keys('[Hold]^t[Release]')
    Delay(1000)
    # Open the new location in Google Maps
    Sys.Browser('iexplore').WaitPage('*about*').ToUrl('http://maps.google.com/maps?q=loc:' + aqConvert.VarToStr(Lat) + ',' + aqConvert.VarToStr(Longt))
    # Disable mock locations
    Mobile.Device().GPS.AllowMockLocations = False

# A helper function that posts the location data to the test log
def PostLocationData(aDevice):
  if aDevice != None:
    if aDevice.OSType == 'Android':
      Log.Message('Longitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Longitude))
      Log.Message('Latitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Latitude))
      Log.Message('Altitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Altitude))
      Log.Message('Accuracy: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Accuracy))
    elif aDevice.OSType == 'iOS':
      Log.Message('Longitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Longitude))
      Log.Message('Latitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Latitude))
      Log.Message('Altitude: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Altitude))
      Log.Message('Speed: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Speed))
      Log.Message('Course: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.Course))
      Log.Message('Horizontal Accuracy: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.HorizontalAccuracy))
      Log.Message('Vertical Accuracy: ' + aqConvert.VarToStr(Mobile.Device().GPS.Location.VerticalAccuracy))

