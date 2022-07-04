# VerificationBot v1.0

## Run with Docker
### Requirements
Docker

### Installation
1. Clone the repository:

     `git clone https://github.com/RileyCalhoun/VerificationBot && cd VerificationBot`

2. Build the image:

    `docker build -t verificationbot .`

3. Run the container:

    `docker run -d --name verificationbot verificationbot:latest`

## Run without Docker
### Requirements
Pyhon 3, Pip

### Installation
1. Clone the repository:
     
     `git clone https://github.com/RileyCalhoun/VerificationBot && cd VerificationBot`

2. Install the necessary dependencies:
    
    `python3 -m pip install -U discord.py python-dotenv`

3. Run the program:
    
    `python3 ./index.py`