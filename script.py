import Android
import time

sensor = Mobile.Device("MyDevice").Sensors(0);
values = sensor.Values;
Log.Message(values.Value0);
Delay(1000);
Log.Message(values.Value0); # still the old value

def ListSensors():

  Mobile.SetCurrent("Nexus 7")
  for i in range (0,  Mobile.Device().SensorsCount):
    sensor = Mobile.Device().Sensor[i]
    Log.AppendFolder("Sensor " + IntToStr(i) + ": " + sensor.Name)
    Log.Message(sensor.Type)
    Log.Message("Value0: " + VarToStr(sensor.Values.Value0))
    Log.Message("Value1: " + VarToStr(sensor.Values.Value1))
    Log.Message("Value2: " + VarToStr(sensor.Values.Value2))
    Log.PopLogFolder()

