# lanraragi-api

a Python library for [LANraragi](https://github.com/Difegue/LANraragi) API.

> Many thanks to the author of this wonderful manga server app.

All the APIs are from [the official LANraragi document](https://sugoi.gitbook.io/lanraragi/api-documentation/getting-started). 

# Demo

```python
from lanraragi_api import LANrargiAPI
from lanraragi_api.common.entity import Archive

lgg_apikey = ''
lgg_server = 'http://127.0.0.1:3000'
api = LANrargiAPI(lgg_apikey, lgg_server)

archives: list[Archive] = api.archive.get_all_archives()
print(archives[0])
```