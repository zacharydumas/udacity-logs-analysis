# Logreader.py
This is an application to summarize logs from a fictional website for the Udacity full stack developer nanodegree. 
It answers the questions:
* What are the top three articles on the site?
* What are the current view counts for the authors featured on the site?
* On which dates the the users encounter errors on more than 1% of connections?

------------------------------
## Prerequisites
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
** Install the version for your operating system. You do not need to launch VirtualBox after running it
* [Vagrant](https://www.vagrantup.com/downloads.html)
** Install the version for your operating system.
** If the installer asks you to grant network permissions or make a firewall exeption, be sure to allow this.
* Install the VM configuration.
** Download [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
** Unzip the file and `cd` into its directory and `cd` into the vagrant directory.
** run the command `vagrant up` to install the Linux virtual machine.
* [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
** Unzip newsdata.sql and copy it into the `vagrant` directory, which is shared with your virtual machine.
** `cd` into the `vagrant` directory and run the command `psql -d news -f newsdata.sql` to populate the database.
------------------------------
## Installation
Logreader.py should be placed in the "vagrant" directory, which is shared with your virtual machine.

-----------------------------------
## Usage
* `cd` to the location of your Vagrant VM.
* log into vagrant with `vagrant ssh`.
* `cd` to the location of your `vagrant` directory.
* run logreader with 
	`python logreader.py` 
	or 
	`./logreader.py`.

------------------------------------
## Authors
Zachary Dumas - https://github.com/zacharydumas

----------------------------------
## Acknowledgements
Installation instructions for prerequisites comes from [Udacity](https://www.udacity.com/)