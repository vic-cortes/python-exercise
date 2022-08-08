# Python Excersie

Repo to revierwe python experience. Retrieves information from a given `url`.


## How to run it?

Run the following command to build and deploy the service

```sh
docker-compose up
```

## Endpoints Availables

- `<base_url>/api/retrieve/metadata`


### Example

```bash
curl --location --request POST 'http://127.0.0.1:5000/api/retrieve/metadata' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://stackoverflow.com/"
}'
```


#### Response 200

```json
{
    "data": {
        "description_tag": "<meta content=\"Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge, and build their careers.\" name=\"description\"/>",
        "favicon_tag": "<link rel=\"shortcut icon\" href=\"https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196\"/>&#13;\n        ",
        "title_tag": "<title>Stack Overflow - Where Developers Learn, Share, &amp; Build Careers</title>"
    },
    "status": "SUCCESS",
    "url": "https://stackoverflow.com/"
}
```