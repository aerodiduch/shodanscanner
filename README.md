
# shodanscanner

Bulk scanner of IPs through Shodan, dumping data to an Excel file including location, ISP, CVEs, among others.

> Warning. This a WIP project. I'm constantly making new changes. Some things may not work as intented.

# Installation

There is two ways to install and use `shodanscanner`

## Using virtual enviroments

If you want to use `shodanscanner` inside a python's virtual enviroment:

```
git clone https://github.com/aerodiduch/shodanscanner
cd shodanscanner
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python shodanscanner.py
```

Then, everytime you use the tool you have to activate the virtual enviroment and then use the tool, like this:

```
cd shodanscanner
venv/Scripts/activate
python shodanscanner.py ...
```


## Normal installation

If you don't mind about isolating dependencies:

```
git clone https://github.com/aerodiduch/shodanscanner
cd shodanscanner
pip install -r requirements.txt
python shodanscanner.py ...
```

# Usage
## Setting up API KEY

In order to use `shodanscanner` you need a Shodan's API KEY. You can find it on https://account.shodan.io/. 

When running `shodanscanner` for the first time, a setup function will run.

`python shodanscanner.py`

```
[!!!] No API KEY detected.

This will be prompted only one time to set API KEY.
A .env file will be created containing it.
You will find your Shodan API KEY on https://account.shodan.io/

You can change it later editing the .env file created on this directory.
If no valid API KEY is provided, shodanscanner can not make requests through Shodan API.

[!] Paste your API KEY:
```

You just need to paste your API KEY and now you can freely use `shodanscanner`. 

This will create a `.env` file which will store your API KEY and load it every time you execute `shodanscanner`. You can edit this file to replace your API KEY if needed.

## Help command

Executing `shodanscanner` without parameters or by passing `-h` flag will output the following:

```
usage: shodanscanner [-h] [-f FILE] [-t TARGET] [-o OUTPUT]

Simple script to bulk scan IPs on Shodan

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing IP address to scan. Input must be one IP per line.
  -t TARGET, --target TARGET
                        Scan a single target, e.g: -t 200.100.20.10
  -o OUTPUT, --output OUTPUT
                        Name of the output file without extension. Default value is "results".

made by aerodiduch. https://github.com/aerodiduch
```

## Usage example

You need a file containing a list of IPs, containing one per line.
> `my_ip_list.txt`
```
108.141.106.44
221.245.33.2
190.64.250.30
178.97.75.163
61.54.54.98
```

Then, you execute `shodanscanner` passing the `-f` flag with the directory of your file.

> Note: You can pass `-o` flag to specify output filename. It is **not** necessary to add `.xlsx` extension, since `shodanscanner` does it for you. In case output filename is not provided, it defaults to `results`.

`python shodanscanner.py -f my_ip_list.txt -o ip_data`

```
-> Ready to scan X hosts...

100%|██████████████████████| 15/15 [00:21<00:00,  1.29s/it] 

-> Finished scan. Results dumped to "ip_data.xlsx"

No results found for: IP1, IP2...
```


# Authors

Pending

# Contribution

Pending

