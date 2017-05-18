## Finding prime factors on the OctaPi

To complete this section of the resource, you will need to have [built an OctaPi](rpi-python-build-an-octapi)

1. Download the [code for the OctaPi](resources/factor_efficient.py) and save it onto your OctaPi client machine

1. With your OctaPi, OctaPi client machine and wireless router fully powered up and connected, open a terminal on the OctaPi client machine

    ![Open a terminal](images/terminal.png)

1. Run the code by typing the following command:

    ```bash
    python3 factor_efficient.py 2396059349 1000
    ```

### Explanation

The OctaPi program follows the same principle as the stand alone program, searching for the prime factors in chunks. The big difference is that **dispy** is used to distribute the chunks between the cores on the OctaPi. Searching through each chunk is considered a **job**, and as each job is completed (but unsuccessful in finding the prime factors), another job is fed to the cluster.

You can imagine the job of the OctaPi like sorting through a big pile of mail looking for a particular letter. The post is divided up into equally sized piles. Each processor is given a pile to look through, and when it finishes searching through that pile, it receives another pile to check. It is easy to see that the job is finished much more quickly by having multiple processors looking through piles in parallel than it is to have one processor looking through the piles one after another.
