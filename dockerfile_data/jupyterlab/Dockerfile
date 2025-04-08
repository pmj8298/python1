# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintainer="pmj8298@naver.com"

RUN apt update -y && \
    apt install -y sudo passwd openssh-server wget && \ 
    apt install -y nano net-tools && \ 
    apt install -y iputils-ping openjdk-8-jdk python3-pip && \
    apt clean && \ 
    rm -rf /var/lib/apt/lists/*

# 계정생성 및 세팅
RUN groupadd pkmj && useradd -m -d /home/pkmj -s /bin/bash -g pkmj -G sudo pkmj && \
    echo "pkmj:1234" | chpasswd && \
    mkdir -p /home/pkmj/.ssh && \
    chown -R pkmj:pkmj /home/pkmj && \
    echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkmj/.bashrc && \
    echo "export PATH=$PATH:/home/pkmj/.local/bin" >> /home/pkmj/.bashrc && \
    chown pkmj:pkmj /home/pkmj/.bashrc && \
    mkdir -p /var/run/sshd && \
    echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config 

# 사용자 변경
USER pkmj

# 작업환경 변경
WORKDIR /home/pkmj

# pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

# ssh 서버 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root --FileContentsManager.delete_to_trash=False"]