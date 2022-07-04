# VerificationBot v1.0

## Run with Docker
### Requirements
Docker

### Installation
1. Clone the repository:

     `git clone https://github.com/RileyCalhoun/VerificationBot && cd VerificationBot`

2. Create a `.env` file and put your bot token inside as `BOT_TOKEN`

3. Build the image:

    `docker build -t verificationbot .`

4. Run the container:

    `docker run -d --name verificationbot verificationbot:latest`

## Run without Docker
### Requirements
Pyhon 3, Pip

### Installation
1. Clone the repository:
     
     `git clone https://github.com/RileyCalhoun/VerificationBot && cd VerificationBot`

2. Create a `.env` file and put your bot token inside as `BOT_TOKEN`

3. Install the necessary dependencies:
    
    `python3 -m pip install -U discord.py python-dotenv`

4. Run the program:
    
    `python3 ./index.py`