# Linux Installs

Ther are some utilities that don't make sense to install on other
machine types, so I am breaking those notes out here. This is pretty raw
since I am not going through a Linux (re-)installation at this point, so
currently is just parts of my original `README.md` file extracted out.

## Additional Installs

Since Linux is free, you need to install some drivers for things like
DVD playback and mp3 decoding:

```bash
apt install ubuntu-restricted-extras libdvdread4
sudo /usr/share/doc/libdvdread4/install-css.sh
```

Once you have those, you can grab a few more important programs:

```bash
apt install skype audacious luckybackup texlive-full pavucontrol
        soundconverter

For `luckybackup`, you'll need to set up the actual backup location and
make sure that there aren't weird file duplicates from copying things
over.
