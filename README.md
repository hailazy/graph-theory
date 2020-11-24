# graph-theory
## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [docker](https://www.docker.com/get-started) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/haimap/graph-theory.git

# Go into the repository
$ cd graph-theory

# Build a Docker container
$ docker build -t coderbungbu/graph_theory .

# Run the app
$ docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app \
  coderbungbu/graph_theory
```

Note: If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.