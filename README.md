# aurora-forecast
Notes: All of data fetch from https://www.swpc.noaa.gov/products/aurora-30-minute-forecast.
The code works with chatGPT.

Using Python to draw aurora forecast data.

step 1: Use the 'aurora_forecast_download.py' script to download all of the aurora data from the specified source: "https://services.swpc.noaa.gov/images/animations/ovation/north/" or "https://services.swpc.noaa.gov/images/animations/ovation/south/"  

step 2: Utilize 'aurora_forecast_player_repeat.py' to play all the JPG files in the './downloaded_files' directory on repeat.



https://github.com/bigheadG/aurora-forecast/assets/2010446/06d83fab-ac7c-4efb-ae99-ca47fd14e6b6

======================================================================================================


          

# Solar wind: URL: https://services.swpc.noaa.gov/images/animations/enlil/
## replace URL and Download file: run aurora_forecast_download.py 
      For solar wind, you only need to replace the 
      url = "https://services.swpc.noaa.gov/images/animations/ovation/north/" and 
      download_files = 'downloaded_files' in aurora_forcast_download.py with 
      url = "https://services.swpc.noaa.gov/images/animations/enlil/" and 
      download_files = 'downloaded_enlil_files' .
      
## playback: run aurora_forecast_player_repeat.py 
 Run aurora_forcast_player_repeat.py (replaced: directory = "./downloaded_enlil_files/") you can see the beautiful solar wind predict map as following video.
 

https://github.com/bigheadG/aurora-forecast/assets/2010446/9aab4966-0802-4130-81f1-92c439d1fc59


## Solar Wind Forecast Playback: solarWind_forecast.py

          Need to use aurora_forecast_download.py download solar wind data first.
               please modified:
                    url = "https://services.swpc.noaa.gov/images/animations/enlil/"
                    download_files = 'downloaded_enlil_files' .


Aurora/Solar Wind information source: NOAA
