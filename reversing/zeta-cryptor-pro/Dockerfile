FROM ubuntu:18.04 AS build

RUN apt-get update && apt-get install -y libsodium-dev protobuf-compiler libnl-route-3-dev pkg-config flex bison libprotobuf-dev git make python3 python3-pip
RUN pip3 install pynacl
RUN mkdir /build
RUN git clone https://github.com/google/nsjail.git /build/nsjail
RUN cd /build/nsjail && make
COPY src /build/src
RUN cd /build/src && ./build.sh && python3 sign_binary.py

FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip libsodium23 libprotobuf10 libnl-route-3-200
RUN pip3 install pynacl
RUN mkdir -p /home/zetacryptorpro
COPY --from=build /build/nsjail/nsjail /bin/nsjail
COPY --from=build /build/src/challenge_signed /home/zetacryptorpro/zeta-cryptor-pro
COPY --from=build /build/src/license.dat /home/zetacryptorpro/license.dat
COPY server/run.sh /init.sh
COPY server/server.py /home/zetacryptorpro/server.py

CMD ["./init.sh"]  
