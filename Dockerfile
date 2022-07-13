FROM srd8/telethon-keto:alpine

#clonning repo 
RUN git clone https://github.com/srd8/Telethon-keto
#working directory 
WORKDIR /root/telethon

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Arab/bin:$PATH"

CMD ["python3","-m","Arab"]
