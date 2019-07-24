# lazy-debugging
## Tools for the laziest of the lazy

#### Sick of searching stackoverflow for you problems? Try this out:
_requires chromedriver_
```python
from search import search_error

try:
    ## I dont have this installed
    import boto3
except Exception as e:
    search_error(e)
```
#### Which opens the below image in a new chrome window:

![Demo](/images/search_errorDEMO.PNG)
