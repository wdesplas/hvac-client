# hvac-client for cloudfoundry
A simple client coded in python that test he is able to setting up entry into a Hashicorp vault 

## Installation process :
Edit the manifest with the proper vault services provided by your cloudfoundry

Then
```
cf push
```

## Call the apps

```
curl <host>:/v1/health | jq .
```

will  return json file  with all the request and specifically the data content list like:
```
{
  "auth": null,
  "renewable": false,
  "lease_duration": 3600,
  "request_id": "de82b273-59ce-0522-17ce-f4deb4656af4",
  "data": {
    "creation_time": "2019-05-29 13:02:47",
    "lease": "1h",
    "baz": "bar",
    "random_uuid": "049ca680-af0f-430d-b1e5-64ece3aa2174"
  },
  "warnings": null,
  "wrap_info": null,
  "lease_id": ""
}
```

Note that the random_uuid and the creation_time must change in each request.
