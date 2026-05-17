# Use a lightweight Linux base image
FROM alpine:latest

# Install useful networking and system tools to demonstrate knowledge
RUN apk update && apk add --no-cache \
    curl \
    wget \
    git \
    htop \
    tree \
    neofetch

# Set a working directory inside the container
WORKDIR /home/assignment

# Create a dummy file to interact with later
RUN echo "Welcome to the Docker Assignment Environment!" > readme.txt

# Default command to keep the container alive and open a shell
CMD ["/bin/sh"]