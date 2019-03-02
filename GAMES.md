
# Games

This computer is not just for work and programming. You have two main
video game platforms that you use: Steam for modern games, and Mednafen
for old Nintendo ROMs. Additionally, you still play
*Race for the Galaxy* on the computer. Each of these is installed
slightly differently.

## Steam

Download and install through the website. Easy. Done.

Once you have Steam installed, you'll also want to download the games
you want to play. Steam recently introduced the ability to play some
Windows games on Linux, so you aren't even restricted as much there. You
should not download and install the Windows version of Steam through any
method, since it is not necessary.

## Mednafen

*This has not been rewritten yet*

[Mednafen](http://mednafen.fobby.net/releases/), a multi-system
emulator. Install it with:

    apt install libsndfile1-dev libsdl1.2-dev
    ./configure && make -j 9 && sudo make install

Your two SNES controllers can be used for the input. You'll want to
check that the input can actually be read (for all required controllers)
with:

    sudo chmod 666 /dev/input/js0
    jstest /dev/input/js0

to make sure everything is registering. After installing, you need to
edit the config file (`~/.mednafen/mednafen.cfg`) so that `sounddevice`
is `sexyal-literal-default`. The sound seems to be staticy for the first
minute or two, but calms down after. You will probably have to
reconfigure the controller buttons as well:

1.  Plug in all controllers tha you wish to use
2.  Starting with the first controller, hit `alt+shift+1` and follow the
    prompts for button presses
3.  Additional controllers are handled with `alt-shift+X`, up to your
    maximum port number or four

You can also switch between fullscreen and windowed by pressing
`Alt+Enter`.

## Race for the Galaxy

There is a computer version of the card game available at
[RFTG](http://keldon.net/rftg/). This version includes the
*Alien Artifacts* expansion, but not *Xeno Invasion*. Due to some legal
changes with serving RFTG online, I don't expect this version to be
updated.

1.  Download the source code from the website and expand it:

        tar xvf rftg-0.9.4.tar.bz2

2.  Install the GTK dependency:

        apt install libgtk2.0-dev

3.  From within the expanded directory, compile and install the game:

        ./configure && make -j 9 && sudo make install
