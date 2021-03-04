from pathlib import Path
from queue import Queue

modules = {}

directory = {}

queue = {
    'staging': Queue(),
    'year': Queue(),
    'month': Queue(),
    'location': Queue()
}

# Raw media dumps are here
staging = Path('staging')

# Sort staging queue by year
for media in queue['staging']:
    pass

# Sort year queue by month
for media in queue['year']:
    pass

# Sort into geotag vs no-tag
for media in queue['month']:
    if ['geotag' in media.metadata:
        queue['location'].put(media)
# if geotag() is False:...