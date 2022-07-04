FROM ubuntu:18.04

RUN apt update -y \
        && apt upgrade -y
RUN apt install python3.6 python3-pip -y
RUN python3.6 -m pip install -U discord.py python-dotenv

RUN mkdir /usr/local/DiscordVerification
WORKDIR /usr/local/DiscordVerification
ADD . /usr/local/DiscordVerification/

ENTRYPOINT [ "python3.6", "-u", "/usr/local/DiscordVerification/index.py" ]