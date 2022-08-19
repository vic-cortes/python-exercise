# Python Excersie

Repo to revierwe python experience. Retrieves information from a given `url`.


## How to run it?

### Development

1. Build `dev` image with `docker build . -t python-exercise-dev --target=dev`
2. Set `ENVIRONMENT="dev"` in `.env` file.
3. Run `docker-compose up`

### Production

1. Build `prd` image with `docker build . -t python-exercise-prd --target=production`
2. Set `ENVIRONMENT="prd"` in `.env` file.
3. Run `docker-compose up`

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