FROM telethon-keto:alpine

#clonning repo 
RUN git clone https:https://github.com/Srd8/telethon-keto.git
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
