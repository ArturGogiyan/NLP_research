## Demo

- pull docker image: `docker pull basicec/nlp:latest`
- run docker image: `docker run -p 4242:4242 basicec/nlp:latest`
- try: `curl 'http://localhost:4242/echo?echo=Hello'`

## Project hints

- `pip freeze > requirements.txt` - update requirements
- Use [dvc](https://dvc.org/) to manage versions of dataset
    - `dvc pull` - to download current dataset and models