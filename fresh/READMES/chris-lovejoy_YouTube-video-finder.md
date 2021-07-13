# Valuable-YouTube-Video-Finder

## The project
The purpose of this project is to enable users to find valuable YouTube videos of their interest independent of YouTube's recommendation system. For a more detailed explanation of the project, it's purpose and how it was made, see this [post on Medium](https://towardsdatascience.com/i-created-my-own-youtube-algorithm-to-stop-me-wasting-time-afd170f4ca3a).

## Setup

### YouTube-API-Key
You will need to acquire a YouTube v3 API key, which you can do so easily [here](https://console.developers.google.com/cloud-resource-manager). A helpful video outlining the process can be found [here](https://www.youtube.com/watch?v=-QMg39gK624). After obtaining the API key, enter it as a string into the [config.yaml file](https://github.com/chris-lovejoy/YouTube-video-finder/blob/master/config.yaml).

### Packages
All requirements are contained within [requirements.txt](https://github.com/chris-lovejoy/YouTube-video-finder/blob/master/requirements.txt).

To install them, execute the following from the root directory:
```
pip install -r requirements.txt
```

## Execution
After configuring config.yaml and installing requirements, the function can be executed from the command line using:

```
python3 main.py 'search term 1' 'search term 2'
```

The default search period is 7 days, but this can be modified with the '--search-period' argument.

For example:

```
python3 main.py 'machine learning' 'medical school' --search-period 10
```

This will call the [**main.py function**](https://github.com/chris-lovejoy/YouTube-video-finder/blob/master/main.py) and output will be printed into the console.
