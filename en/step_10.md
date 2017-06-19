## Finding prime factors on the OctaPi

To complete this section of the resource, you will need to have [built an OctaPi](rpi-python-build-an-octapi).

- Download the [code for the OctaPi](resources/factor_efficient.py) and save it onto your OctaPi client machine.

- When your OctaPi, the OctaPi client machine, and the wireless router are fully powered up and connected, open a terminal on the OctaPi client machine.

    ![Open a terminal](images/terminal.png)

- Change to the directory where you saved the code using the `cd` command.

- Run the code by typing the following command. You will notice that the arguments passed to the OctaPi (`2396059349` and `1000`) are the same ones we used in the previous step - they are the semi-prime we wish to find the factors of and the chunk size.

    ```bash
    python3 factor_efficient.py 2396059349 1000
    ```

### Explanation

The OctaPi program follows the same principle as the stand-alone program by searching for the prime factors in chunks. The big difference is that **dispy** is used to distribute the chunks between the processors of the OctaPi.

Searching through each chunk is considered a **job**. Each processor is given a job to do, and when it finishes doing that job, if the prime factors were not found, another job is fed to the processor. It is easy to see why the program runs much more quickly with multiple processors working in parallel than it does when one processor must complete the jobs one after another.

You can imagine the program running on the OctaPi as though it were a team of people sorting through a big pile of mail looking for a particular letter. The post is divided up into equally-sized piles, which represent the jobs. Using the OctaPi is like having lots of people searching simultaneously through different piles of mail, whereas a standalone processor is like having one person who must search through all of the piles one by one.
