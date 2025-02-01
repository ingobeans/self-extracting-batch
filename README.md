# self extracting batch

tool to create batch files that contain a zip file which is automatically decoded and extracted in to the scripts directory when ran.
doesn't have a cap on zip size afaik (only tried on zips about 2mb in size)

to try the example: `python self_extracting_batch.py example/input.bat example/yo.zip example/output.bat`
