## Demo

- configure AWS credentials for S3 bucket: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
- run `dvc repro`. This command will run pipelines to train models
- run `docker build --build-arg pythonImage=python:3.8 --build-arg pythonSlimImage=python:3.8 -f Server.CI.Dockerfile -t basicec/nlp:latest .`
- run `docker-compose up` - this will run server

## Project hints

- `pip freeze > requirements.txt` - update requirements
- Use [dvc](https://dvc.org/) to manage versions of dataset
    - `dvc pull` - to download current dataset and models