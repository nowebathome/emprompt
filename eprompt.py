#!/usr/bin/python
#-*-coding: UTF-8-*-

'''
 eprompt.py
 Simple python terminal simulator based on Elliot's terminal
 Version 0.1, lot of known bugs.
 I recommend that you test it in a virtual machine, since it can delete your bash command history.

 AUTHOR
 
 No Web at Home
 nowebathome AT gmail DOT com
 http://www.cybrary.it/members/nowebathome
 http://creator.wonderhowto.com/nowebathome/
 
 LICENSE

 This program is a free software, you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, version 3 or later.
'''

import os
import sys
import readline 
import rlcompleter 
import atexit 
from commands import getoutput
from socket import gethostname

class SimpleCompleter(object):
    
    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s 
                                for s in self.options
                                if s and s.startswith(text)]
            else:
                self.matches = self.options[:]
        
        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response

# Register our completer function
readline.set_completer(SimpleCompleter(['acpi_available', 'agetty',
'apm_available', 'badblocks', 'blkdiscard', 'blkid', 'blockdev',
'bridge', 'capsh', 'cfdisk', 'cgdisk', 'chcpu', 'crda',
'cryptdisks_start','cryptdisks_stop', 'cryptsetup',
'cryptsetup-reencrypt', 'ctrlaltdel','debugfs', 'depmod', 'dhclient',
'dhclient-script', 'dmeventd', 'dmsetup', 'dosfsck', 'dosfslabel',
'dumpe2fs', 'e2fsck', 'e2image', 'e2label', 'e2undo', 'ethtool',
'fatlabel', 'fdisk', 'findfs', 'fixparts', 'fsadm', 'fsck',
'fsck.cramfs', 'fsck.ext2', 'fsck.ext3', 'fsck.ext4', 'fsck.ext4dev',
'fsck.fat', 'fsck.minix', 'fsck.msdos', 'fsck.nfs', 'fsck.vfat',
'fsfreeze', 'fstab-decode', 'fstrim', 'gdisk', 'getcap', 'getpcaps',
'getty', 'halt', 'hdparm', 'hwclock', 'ifconfig', 'ifdown', 'ifenslave',
'ifenslave-2.6', 'ifquery', 'ifup', 'init', 'insmod', 'insserv',
'installkernel', 'ip', 'ip6tables', 'ip6tables-restore',
'ip6tables-save', 'ipmaddr', 'iptables', 'iptables-restore',
'iptables-save', 'iptunnel', 'isosize', 'iw', 'iwconfig', 'iwevent',
'iwgetid', 'iwlist', 'iwpriv', 'iwspy', 'kbdrate', 'killall5',
'ldconfig', 'ldconfig.real', 'logsave', 'losetup', 'lsmod', 'lvchange',
'lvconvert', 'lvcreate', 'lvdisplay', 'lvextend', 'lvm', 'lvmchange',
'lvmconf', 'lvmdiskscan', 'lvmdump', 'lvmetad', 'lvmsadc', 'lvmsar',
'lvreduce', 'lvremove', 'lvrename', 'lvresize', 'lvs', 'lvscan',
'mii-tool', 'mkdosfs', 'mke2fs', 'mkfs', 'mkfs.bfs', 'mkfs.cramfs',
'mkfs.ext2', 'mkfs.ext3', 'mkfs.ext4', 'mkfs.ext4dev', 'mkfs.fat',
'mkfs.minix', 'mkfs.msdos', 'mkfs.ntfs', 'mkfs.vfat','mkhomedir_helper',
'mkntfs', 'mkswap', 'modinfo', 'modprobe', 'mount.fuse',
'mount.lowntfs-3g', 'mount.nfs', 'mount.nfs4', 'mount.ntfs',
'mount.ntfs-3g', 'nameif', 'ntfsclone', 'ntfscp', 'ntfslabel',
'ntfsresize', 'ntfsundelete', 'on_ac_power', 'osd_login', 'pam_tally',
'pam_tally2', 'parted', 'partprobe', 'pivot_root', 'plipconfig',
'poweroff', 'pvchange', 'pvck', 'pvcreate', 'pvdisplay', 'pvmove',
'pvremove', 'pvresize', 'pvs', 'pvscan', 'rarp', 'raw', 'rcvboxdrv',
'reboot', 'regdbdump', 'resize2fs', 'rmmod', 'route', 'rpcbind',
'rpc.statd', 'rtacct', 'rtmon', 'runlevel', 'runuser', 'setcap',
'sfdisk', 'sgdisk', 'shadowconfig', 'showmount', 'shutdown','slattach',
'sm-notify', 'start-stop-daemon', 'sulogin', 'swaplabel', 'swapoff',
'swapon', 'switch_root', 'sysctl', 'tc', 'telinit', 'tune2fs',
'udevadm', 'udevd', 'umount.nfs', 'umount.nfs4', 'umount.udisks',
'umount.udisks2', 'unix_chkpwd', 'unix_update', 'vconfig',
'veritysetup', 'vgcfgbackup', 'vgcfgrestore', 'vgchange', 'vgck',
'vgconvert', 'vgcreate', 'vgdisplay', 'vgexport', 'vgextend',
'vgimport', 'vgimportclone', 'vgmerge', 'vgmknodes', 'vgreduce',
'vgremove', 'vgrename', 'vgs', 'vgscan', 'vgsplit', 'wipefs',
'wpa_action', 'wpa_cli', 'wpa_supplicant', 'xtables-multi', 'amanha',
'amanhatxt', 'bash', 'bunzip2', 'busybox', 'bzcat', 'bzcmp', 'bzdiff',
'bzegrep','bzexe','bzfgrep','bzgrep','bzip2','bzip2recover','bzless',
'bzmore', 'cat','chacl','chgrp','chmod','chown', 'chvt', 'cp', 'cpio',
'dash', 'date', 'dd', 'df', 'dir','dmesg','dnsdomainname','domainname',
'dumpkeys', 'echo', 'egrep', 'false', 'fgconsole', 'fgrep', 'findmnt',
'fuser','fusermount', 'getfacl', 'grep', 'gunzip', 'gzexe', 'gzip',
'hciconfig','hostname', 'ip', 'journalctl', 'kbd_mode', 'kill', 'kmod',
'less', 'lessecho','lessfile', 'lesskey', 'lesspipe', 'ln', 'loadkeys',
'login', 'loginctl','lowntfs-3g', 'ls', 'lsblk', 'lsmod', 'machinectl',
'mkdir', 'mknod','mktemp', 'more', 'mount', 'mountpoint','mt','mt-gnu',
'mv', 'nano', 'nc','nc.traditional','netcat','netstat','nisdomainname',
'ntfs-3g','ntfs-3g.probe','ntfs-3g.secaudit','ntfs-3g.usermap',
'ntfscat', 'ntfscluster', 'ntfscmp', 'ntfsfallocate','ntfsfix',
'ntfsinfo', 'ntfsls', 'ntfsmove', 'ntfstruncate', 'ntfswipe', 'open',
'openvt', 'pidof','ping', 'ping6', 'ps', 'pwd', 'rbash', 'readlink',
'rm', 'rmdir', 'rnano', 'run-parts', 'sed', 'sendprobe', 'setfacl',
'setfont','setupcon','sh','sh.distrib','sleep','ss','stty','su','sync',
'systemctl', 'systemd','systemd-ask-password', 'systemd-escape',
'systemd-inhibit','systemd-machine-id-setup', 'systemd-notify',
'systemd-tmpfiles','systemd-tty-ask-password-agent', 'tailf', 'tar',
'tempfile', 'touch','true','udevadm','ulockmgr_server','umount','uname',
 'uncompress','unicode_start', 'usleep', 'vdir', 'vmmouse_detect',
 'wdctl', 'which','ypdomainname', 'zcat', 'zcmp','zdiff', 'zegrep',
 'zfgrep', 'zforce', 'zgrep', 'zless', 'zmore', 'znew']).complete)

# Use the tab key for completion
readline.parse_and_bind('tab: complete')

histfile = os.path.join(os.environ['HOME'], '.bash_history') 
try: 
	readline.read_history_file(histfile) 
except IOError: 
	pass 
atexit.register(readline.write_history_file, histfile)


#Add more commands here
ignore_list=["vim", "ls", "--help", "man", "cat", "more", "less", "|"]

while True:
	
	#setting the propmt	
	username = os.environ['USER']
	hostname = gethostname()
	homedir = os.path.expanduser('~')
	pwd = os.getcwd()
	pwd = pwd.replace(homedir, '~', 1)
	
	#Modify to your own color here
	prompt= "\033[01;31m"+username+"@"+hostname+"\033[00m"+":"+"\033[94m"+pwd+"\033[00m"+"# "
	#prompt= "\033[34mroot@elliot$: \033[00m"
	
	command=raw_input(prompt)
	
	# Since each os.system("comand") opens a new shell terminal,
	# you can't actually cd.
	if command.split(" ")[0]=="cd":
		try:
			c=command.split(" ")[1]
			os.chdir(c)
		except:
			print "No such file or directory"
	
	else:
		x=0

		while x < len(command.split(" ")):
			if command.split(" ")[x] in ignore_list:
				os.system(command)
				break
			x+=1
		else:
			command+=" > tempfile"
			os.system(command)
			f=open("tempfile", "r")
			q=f.readlines()
			for line in q:
				sys.stdout.write(prompt+line)
			f.close()

