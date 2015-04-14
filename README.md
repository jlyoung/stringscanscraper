# stringscanscraper
stringscanscraper is a web application and API that will accept a search term and a list of urls as input.
stringscanscraper will search each url in the input list for the search term. 
It will then return a subset of the orignal list of urls which contain the search term.

### Prerequisites
The following are required to run this application:
* [Python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing.html)

### Installation
Clone this github repository:

```
git clone https://github.com/jlyoung/stringscanscraper.git
```

Install the required python modules

```
pip install -r requirements.txt
```

### Starting the API service
Startup the application by running the following on your command line:
```
python api.py
```

### Using the API
The REST API has one end-point `/matches`.
`/matches` accepts an `HTTP POST` which must contain: 
* a search term
  * `searchterm=Terms you're searching for`
* a list of urls to search
  * `urls=http://url1.com`  
  * `urls=http://url2.com`

An example curl command querying the API is below:

```
curl --data-urlencode "searchterm=all rights" --data-urlencode "urls=http://www.seavalshop.com/" --data-urlencode "urls=http://keenprint.com/" --data-urlencode "urls=https://womply.com/" --data-urlencode "urls=http://utrack.tv/" --data-urlencode "urls=http://helloivee.com/" http://127.0.0.1:5000/matches
```

The output will return a JSON object containing 2 keys:
* The search term
  * `searchterm`
* A list of urls containing the search term
  * `matches`

Example output:

```
{
    "matches": [
        "http://keenprint.com/", 
        "http://helloivee.com/"
    ], 
    "searchterm": "all rights"
}
```
