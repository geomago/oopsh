ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}
RUN apt-get update -y
RUN apt-get install -yy --no-install-recommends --no-install-suggests fish tcsh zsh

# Nushell isn't packaged for Debian: install the official release binary.
ARG NU_VERSION=0.116.1
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "$arch" in \
        amd64) target='x86_64-unknown-linux-gnu' ;; \
        arm64) target='aarch64-unknown-linux-gnu' ;; \
        *) echo "unsupported arch $arch" >&2; exit 1 ;; \
    esac; \
    url="https://github.com/nushell/nushell/releases/download/${NU_VERSION}/nu-${NU_VERSION}-${target}.tar.gz"; \
    curl -fsSL "$url" -o /tmp/nu.tar.gz; \
    tar -xzf /tmp/nu.tar.gz -C /tmp; \
    install -m 0755 /tmp/nu-${NU_VERSION}-${target}/nu /usr/local/bin/nu; \
    rm -rf /tmp/nu.tar.gz /tmp/nu-${NU_VERSION}-${target}; \
    nu --version

RUN pip install --upgrade pip
COPY . /src
RUN pip install /src
