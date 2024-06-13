# Django zero to hero
- Thanks to [CodeWithHarry](https://www.youtube.com/@CodeWithHarry)
- tutorial [link](https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=1)

#### working process
- create venv and activate

#### Text Utils

1. after each html change --> refresh

2. why new line automatically gone?
    - it happening because of html p tag
    - so use pre tag --> without br tag it can print /n


#### request method
- get: go though via url 
    - --> render desire page
    - --> default for form
    - --> all data added into urls
    - --> its tough to handle big data input for get requst
    - --> here coming post method

- post: do not showed in url
    - --> big data handling
    - --> confidential info
    - --> here coming csrf token for post request
    - --> csrf: unique codes that can help protect web applications from unauthorized requests when included in POST requests


#### append slash problem
- just romove trailing slash from path
    - example: path('analyze', views.analyze, name='analyze')


#### why newline not removed?
- to carry newline '\r' also used
- so check \r also