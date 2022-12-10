
# shodanscanner

Bulk scanner of IPs through Shodan, dumping data to an Excel file including location, ISP, CVEs, among others.

> Warning. This a WIP project. I'm constantly making new changes. Some things may not work as intented.

# Usage

This is a `WIP`. In a future many things will change and there is setup feature on the way. 

## Using virtual enviroments

If you want to use ShodanScanner inside a python's virtual enviroment:

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python shodanscanner.py -f FILE -o OUTPUT
```

Then, everytime you use the tool you have to activate the virtual enviroment and then use the tool, like this:

```
venv/Scripts/activate
python shodanscanner.py ...
```


## "Easier" installation

If you don't mind about isolating dependencies:

```
pip install -r requirements.txt
python shodanscanner.py -f ...
```

# Authors

Pending

# Contribution

Pending

