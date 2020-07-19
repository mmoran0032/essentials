# Installing Windows Subsystem for Linux

I am enumerating the steps I've taken to install the *Windows Subsystem for Linux* (WSL) on my new laptop, starting on 2020-07-18. I am going to enumerate what steps I took, and where I found the information to take those steps.

## Steps

1.  While running PowerShell as an admin, execute the following:
    ```
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    ```
    This step provides for WSL to be activated, but it is not useable yet. Note that, given the current OS version of my laptop, this is WSL1, not WSL2. From [ComputerHope][1].

2.  Reboot and go to the [Windows Store][2] showing the available kernels. I am installing Ubuntu since I used it previously and it is more closely aligned with my existing Linux Mint installation. WSL can now be started, either by launching Ubuntu from the Start menu, or by running `bash` in PowerShell.

## Next Steps

At this point, you should have an active Linux environment, so any other steps would be similar to setting up your usual Linux environments (e.g. installing and updating tools, cloning repos, downloading additional software). There are a few things to note:

- It doesn't seem like you can do `git` stuff within the Windows side of things, so you need to do all of that on the Linux side. A [Gist][3] gives some information on ways to align some of the work so that you don't have to worry as much about two filesystems.
- You need to set up VSCode/VSCodium to work in WSL, following the steps outlined on [VScode's website][4]

[1]: https://www.computerhope.com/issues/ch001879.htm
[2]: https://aka.ms/wslstore
[3]: https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da
[4]: https://code.visualstudio.com/docs/remote/wsl
