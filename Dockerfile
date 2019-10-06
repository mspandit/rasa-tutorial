FROM ubuntu:latest
RUN apt-get update
# https://rasa.com/docs/rasa/user-guide/installation/
RUN apt-get install -y gcc python3 curl python3-distutils python3-dev python3-pip emacs language-pack-en
# https://github.com/RasaHQ/rasa/issues/4545#issuecomment-537510394
RUN pip3 install rasa==1.3.3 rasa-x --extra-index-url https://pypi.rasa.com/simple
# https://askubuntu.com/a/749780
ADD files files
WORKDIR files
RUN LC_ALL="en_US.UTF-8" rasa init --no-prompt
