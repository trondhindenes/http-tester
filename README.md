# HTTP-tester

Simple util for testing urls and reporting errors

## How it works
Specify a url and optionally a wait time between each test. Http-tester will ping the provided url over and over, while keeping track of how many failures there's been

```
╰─ docker run trondhindenes/http-tester --wait-secs 0.5 https://www.google.com
2022-03-02 08:49:39.380833 status code was 200 failure count: 0
2022-03-02 08:49:43.141515 status code was 200 failure count: 0
2022-03-02 08:49:46.926415 status code was 200 failure count: 0
2022-03-02 08:49:47.540901 status code was 200 failure count: 0
2022-03-02 08:49:48.171477 status code was 200 failure count: 0
```


## How to build:
```
docker build -t trondhindenes/http-tester:latest . &&
docker push trondhindenes/http-tester:latest
```
