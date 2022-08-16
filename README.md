NSAPH EPA Package Description
=============================

Toolkit for downloading and preprocessing of data provided by EPA

Handles the following types of data: 

* EPA AQS Data hosted at https://www.epa.gov/aqs and EPA AirNow data 
  from https://docs.airnowapi.org/webservices
    * [Pipeline](src/cwl/aqs.cwl)
* AirNow contains real-time up-to-date pollution data but is less reliable
  than AQS
    * [Pipeline](src/cwl/airnow.cwl)
           

For details see:

* [Usage](doc/usage.md)
* [Main AQS class](src/python/epa/aqs.py) 
  and its [configuration](src/python/epa/aqs_ds_def.py)
* [Main AirNow class](src/python/epa/airnow.py)
  and its [configuration](src/python/epa/airnow_ds_def.py)
* [AQS Pipeline](src/cwl/aqs.cwl)
* [AirNow Pipeline](src/cwl/airnow.cwl)

Also, see additional modules:

* [GIS Annotator](src/python/epa/airnow_gis.py)
* [AirNow Downloader](src/python/epa/airnow_downloader.py)
* [AirNow workspace Initializer](src/python/epa/airnow_setup.py)

[NSAPH-EPA Documentation](https://nsaph-data-platform.github.io/nsaph-platform-docs/common/epa/)
[Full Platform Documentation](https://nsaph-data-platform.github.io/nsaph-platform-docs/home.html)
