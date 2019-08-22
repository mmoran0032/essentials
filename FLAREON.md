
# Flare-ON Challenge

To further my understanding of how common security practices and
workflows are done, I'm setting up the prerequisites to do similar
analyses on my machine. The initial purpose of this work is to take part
in the [Flare-ON 2019](https://2019.flare-on.com/) "capture the flag"
(CTF) contest, running in August and September 2019.

Flare-ON has 12 total challenges, taking place over 6 weeks.

## Steps

The steps outlined below are those taken to create my environment. These
steps roughly follow the outline provided on [MalwareTech][1] and with
help from Aaron *et al.* to get the FlareVM set up.

1. Set up VirtualBox.

   Install VirtualBox by running the following:

       apt update
       apt install virtualbox virtualbox-qt

   Once installed, launch VirtualBox and create a new image. For this
   first image, I am using:

   - Windows 7 (32-bit) installation
   - 1024 MB RAM
   - fixed-size VDI hard disk (32 GB)

   All other settings are the default.

1. Download a Microsoft Edge virtual machine from [Microsoft][2].

   I selected the "IE11 on Winy (x86)" version for VirtualBox. Once
   downloaded, extract the file and launch the extracted `*.ova` file.
   You should see the "Import Virtual Applicance" pane in VirtualBox.
   The defaults should be fine. Click "Import" to create the image.

   Note that the installation instructions linked on the page are not
   helpful, at least they didn't seem helpful to me. It also looks like
   the image created before doesn't matter...?

   I'm going to be taking snapshots throughout this entire process. Take
   the first one here just in case the FlareVM installation doesn't go
   well.

1. Start the image and install FlareVM.

   Follow the steps outlined on [Fireeye's blog][3] from within the VM
   to create the environment. FlareVM has a *ton* of preinstalled
   utilities, so it should be a one-stop-shop for what you need.

   Use `PowerShell` to install everything from the source. Basically,
   follow the steps on the blog and watch the progress. While
   installing, there was one step that seemed to hang, but the
   installation appeared to be successful.

At this point, the environment should be set up with all of your
necessary tools installed. Get to work!

[1]: https://www.malwaretech.com/2017/11/creating-a-simple-free-malware-analysis-environment.html
[2]: https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/
[3]: https://www.fireeye.com/blog/threat-research/2018/11/flare-vm-update.html
