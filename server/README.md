# Rainbow server

Web wrapper for Python modules. It generates a REST API from your Python class.

It can be used with [Rainbow client](https://github.com/bqlabs/rainbow-client/).

## Installation

```bash
git clone https://github.com/bqlabs/rainbow-server.git
cd rainbow-server
python setup.py install
```

## Execute

Put your Python module path in: ~/.rainbow/rainbow.conf and execute the server:

```bash
rainbow
```

### Daemonize

```bash
sudo cp daemon /etc/init.d/rainbow
sudo chmod 755 /etc/init.d/rainbow
```

```bash
sudo /etc/init.d/rainbow {start|stop}
```

### Start on boot

Configure ~/.rainbow/rainbow.conf for `root` user:

```bash
sudo su
vi ~/.rainbow/rainbow.conf  # Put your Python module path here
```

Add the rainbow service:

```bash
update-rc.d rainbow defaults
reboot
```
