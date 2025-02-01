import sys, base64

if len(sys.argv) != 4:
    print("incorrect args. usage: python self_extracting_batch.py <input batch> <input zip> <output batch>")

start = '''@echo off
more +{length} %0 > "%~dp0\\data.b64"
certutil -decode "%~dp0\\data.b64" "%~dp0\\data.zip"
tar -xvzf "%~dp0\\data.zip"
del "%~dp0\\data.b64"
del "%~dp0\\data.zip"
'''

end = '''
exit
'''

with open(sys.argv[1],"r",encoding="utf-8") as f:
    input_batch = f.read()
    
with open(sys.argv[2],"rb") as f:
    input_zip = base64.b64encode(f.read())

length = len((start+input_batch+end).split("\n"))-1
output = start.format(length=length) + input_batch + end

with open(sys.argv[3],"w",encoding="utf-8") as f:
    f.write(output)
    
with open(sys.argv[3],"ab") as f:
    f.write(input_zip)
    