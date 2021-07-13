[![Build Status](https://travis-ci.org/tomac/yersinia.svg?branch=master)](https://travis-ci.org/tomac/yersinia)

Spanning Tree
-------------

#1: DOS attack sending conf BPDUs

    Let's send some conf BPDUs claiming be root!!! By sending continously conf BPDU with root pathcost 0, randomly
    generated bridge id (and therefore the same root id), and some default values for other fields, we try to 
    annoy the switches close to us, causing a DoS when trying to parse and recalculate their STP engines.

    Source MAC: randomly generated.
    Destination MAC: 01:80:c2:00:00:00
    Bridge ID: 8000:source_mac
    Root ID: 8000:source_mac
    Hello time: 2
    Forward delay: 15
    Max age: 20
    Root pathcost: 0

    <output from the cisco log>
    01:20:26: STP: VLAN0001 heard root 32768-d1bf.6d60.097b on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-9ac6.0f72.7118 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-85a3.3662.43dc on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-3d84.bc1c.918e on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-b2e2.1a12.dbb4 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-4ba6.2d45.5844 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-deb0.4f14.7288 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-4879.8036.0e24 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-2776.e340.9222 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-299e.de76.c07d on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-d38b.bc5b.e90d on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-78ee.0205.afdb on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-b32b.e969.81b1 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-b16b.c428.88a3 on Fa0/8
    01:20:26: STP: VLAN0001 heard root 32768-dd01.1436.9044 on Fa0/8
    </output>


#2: DOS attack sending tcn BPDUs

    This attack sends continously tcn BPDUs causing the root switch to send conf BPDUs acknowledging the change. 
    Besides, the root switch will send topology change notifications to the members of the tree, and they will
    have to recalculate their STP engine to learn the new change.

    Source MAC: randomly generated.
    Destination MAC: 01:80:c2:00:00:00

    <output from the cisco log>
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    01:35:39: STP: VLAN0001 Topology Change rcvd on Fa0/8
    </output>


#3: NONDOS attack Claiming Root Role

    Now our aim is to get the root role of the tree. How can we accomplish this issue? Just listening to the network
    to find out which one is the root role, and start sending conf BPDU with lower priority to become root.

    Source MAC: same one as the sniffed BPDU.
    Destination MAC: same one as the sniffed BPDU.
    Bridge ID: the sniffed one slightly modified to have a lower priority
    Root ID: 8000: same as bridge id.
    Hello time: same one as the sniffed BPDU.
    Forward delay: same one as the sniffed BPDU.
    Max age: same one as the sniffed BPDU.
    Root pathcost: same one as the sniffed BPDU.

    <output from the cisco log>
    01:58:48: STP: VLAN0001 heard root 32769-000e.84d4.2280 on Fa0/8
    01:58:48:     supersedes 32769-000e.84d5.2280
    01:58:48: STP: VLAN0001 new root is 32769, 000e.84d4.2280 on port Fa0/8, cost 19
    </output>


#4 NONDOS attack Claiming a non-root role

   We pretend to be another weird switch playing with STP and praising our root id :)


#5 DOS attack causing eternal root elections

    By sending config BPDUs autodecrementing their priority, we can cause infinite root elections in the STP tree.
    It would be something similar to recount the election's votes to determine the winner (do you remember Florida?)

    <output from the cisco log>
    00:20:21: STP: VLAN0001 heard root 32769-000e.84d4.2280 on Fa0/9
    00:20:21:     supersedes 32769-000e.84d5.2280
    00:20:21: STP: VLAN0001 new root is 32769, 000e.84d4.2280 on port Fa0/9, cost 19
    00:20:23: STP: VLAN0001 heard root 32769-000e.84d3.2280 on Fa0/9
    00:20:23:     supersedes 32769-000e.84d4.2280
    00:20:23: STP: VLAN0001 new root is 32769, 000e.84d3.2280 on port Fa0/9, cost 19
    00:20:25: STP: VLAN0001 heard root 32769-000e.84d2.2280 on Fa0/9
    00:20:25:     supersedes 32769-000e.84d3.2280
    00:20:25: STP: VLAN0001 new root is 32769, 000e.84d2.2280 on port Fa0/9, cost 19
    00:20:27: STP: VLAN0001 heard root 32769-000e.84d1.2280 on Fa0/9
    00:20:27:     supersedes 32769-000e.84d2.2280
    00:20:27: STP: VLAN0001 new root is 32769, 000e.84d1.2280 on port Fa0/9, cost 19
    00:20:29: STP: VLAN0001 heard root 32769-000e.84d0.2280 on Fa0/9
    00:20:29:     supersedes 32769-000e.84d1.2280
    00:20:29: STP: VLAN0001 new root is 32769, 000e.84d0.2280 on port Fa0/9, cost 19
    00:20:31: STP: VLAN0001 heard root 32769-000e.84cf.2280 on Fa0/9
    00:20:31:     supersedes 32769-000e.84d0.2280
    00:20:31: STP: VLAN0001 new root is 32769, 000e.84cf.2280 on port Fa0/9, cost 19
    00:20:33: STP: VLAN0001 heard root 32769-000e.84ce.2280 on Fa0/9
    00:20:33:     supersedes 32769-000e.84cf.2280
    00:20:33: STP: VLAN0001 new root is 32769, 000e.84ce.2280 on port Fa0/9, cost 19
    00:20:35: STP: VLAN0001 heard root 32769-000e.84cd.2280 on Fa0/9
    00:20:35:     supersedes 32769-000e.84ce.2280
    00:20:35: STP: VLAN0001 new root is 32769, 000e.84cd.2280 on port Fa0/9, cost 19
    00:20:37: STP: VLAN0001 heard root 32769-000e.84cc.2280 on Fa0/9
    00:20:37:     supersedes 32769-000e.84cd.2280
    00:20:37: STP: VLAN0001 new root is 32769, 000e.84cc.2280 on port Fa0/9, cost 19
    00:20:39: STP: VLAN0001 heard root 32769-000e.84cb.2280 on Fa0/9
    00:20:39:     supersedes 32769-000e.84cc.2280
    00:20:39: STP: VLAN0001 new root is 32769, 000e.84cb.2280 on port Fa0/9, cost 19
    </output>


#6 DOS Attack causing root dissapearance

    This time we try to exhaust the root election proccess. We manage to become root in the STP tree,
    but we stop sending config BPDUs until it reaches max_age seconds (usually 20), forcing a new 
    election proccess.

    <output from the cisco log>
    02:02:43: STP: VLAN0001 heard root 32769-000e.84d4.2280 on Fa0/9
    02:02:43:     supersedes 32769-000e.84d5.2280
    02:02:43: STP: VLAN0001 new root is 32769, 000e.84d4.2280 on port Fa0/9, cost 19
    02:03:03: STP: VLAN0001 we are the spanning tree root
    02:03:04: STP: VLAN0001 heard root 32769-000e.84d4.2280 on Fa0/9
    02:03:04:     supersedes 32769-000e.84d5.2280
    02:03:04: STP: VLAN0001 new root is 32769, 000e.84d4.2280 on port Fa0/9, cost 19
    02:03:04: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:06: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:08: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:10: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:12: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:14: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:16: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:18: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:20: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:22: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:24: STP: VLAN0001 we are the spanning tree root
    02:03:24: STP: VLAN0001 heard root 32769-000e.84d4.2280 on Fa0/9
    02:03:24:     supersedes 32769-000e.84d5.2280
    02:03:24: STP: VLAN0001 new root is 32769, 000e.84d4.2280 on port Fa0/9, cost 19
    02:03:24: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:26: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:28: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:30: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:32: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:34: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:36: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:38: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:40: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:42: STP: VLAN0001 sent Topology Change Notice on Fa0/9
    02:03:44: STP: VLAN0001 we are the spanning tree root
    </output>


Mitigations (Cisco only)
------------------------

- Use port security and disable STP in those ports that don't require STP.
For information about port security, please check the following url:
http://www.cisco.com/en/US/products/hw/switches/ps628/products_configuration_guide_chapter09186a0080150bcd.html

- If you are using the portfast feature in your STP configuration, enable also the BPDU guard for avoiding these
attacks when the port automatically enters the forwarding state:
http://www.cisco.com/warp/public/473/65.html

- Use the root guard feature for avoiding rogue devices to become root:
http://www.cisco.com/en/US/tech/tk389/tk621/technologies_tech_note09186a00800ae96b.shtml


Further reading
---------------

- Guillermo Marro's nice Master Thesis:
http://seclab.cs.ucdavis.edu/papers/Marro_masters_thesis.pdf

- Oleg K. Artemjev, Vladislav V. Myasnyankin. Fun with the Spanning Tree Protocol
http://phrack.org/issues/61/12.html



CDP 
---

Cisco devices have always spoken a different language to communicate among them,
to tell everybody that they are alive and which nifty features they have. CDP
stands for Cisco Discovery Protocol. By means of this particular language, Cisco
devices set up a virtual world where everyone is happy and ther is no crime at
all. Or at least it seems to be this way, since many network administrators
aren't worried for CDP yet. Although some of information that can be sent in a
CDP packet is still undocumented (CDP is a propietary protocol and it seems that
Cisco does not want to give details about it), at least one old attack (that it
is still valid) is known, and there is a public implementation (FX did it!).

This attack is a DoS trying to exhaust the device memory so that it can't
allocate more memory for any device process. How can we do it? Simply sending
CDP packets with bogus data simulating real Cisco devices. The target device
will begin to allocate memory in its CDP table to save the new neighbor
information, but without knowing that it is going to have thousands or millions
of new friends.

Other attack implemented in the current code is the ability to set up a new
virtual Cisco device that it is designated only for make a little mess, trying
to confuse network administrators.

Screenshot of the attack running:

Output of a Cisco 2503 router:

    athens#sh mem
                   Head   Total(b)    Used(b)    Free(b)  Lowest(b) Largest(b)
    Processor     4873C    3893444    3893444          0          0          0
    I/O          400000    2097152    2097088         64         64         64

    <log>
    %SCHED-3-THRASHING: Process thrashing on watched queue 'CDP packets' (count 57).
    -Process= "CDP Protocol", ipl= 6, pid= 9
    -Traceback= 3159232 31594DE 3201660
    %LANCE-5-COLL: Unit 0, excessive collisions. TDR=7
    %SCHED-3-THRASHING: Process thrashing on watched queue 'CDP packets' (count 57).
    -Process= "CDP Protocol", ipl= 6, pid= 9
    -Traceback= 3159232 31594DE 3201660
    %SYS-2-MALLOCFAIL: Memory allocation of 100 bytes failed from 0x3201B3E, pool Processor, alignment 0
    -Process= "CDP Protocol", ipl= 0, pid= 9
    -Traceback= 314E8A4 314FA06 3201B46 32016C8
    %SCHED-3-THRASHING: Process thrashing on watched queue 'CDP packets' (count 57).
    -Process= "CDP Protocol", ipl= 6, pid= 9
    -Traceback= 3159232 31594DE 3201660
    %SYS-2-MALLOCFAIL: Memory allocation of 100 bytes failed from 0x3201B3E, pool Processor, alignment 0
    -Process= "CDP Protocol", ipl= 0, pid= 9
    -Traceback= 314E8A4 314FA06 3201B46 32016C8
    %SYS-2-MALLOCFAIL: Memory allocation of 100 bytes failed from 0x3201B3E, pool Processor, alignment 0
    -Process= "CDP Protocol", ipl= 0, pid= 9
    -Traceback= 314E8A4 314FA06 3201B46 32016C8
    </log>

And a couple of minutes later after killing the attack, the router surprisingly gets halted for several seconds, 
and then kicks you out of the terminal :)

    <log>
    %SYS-3-CPUHOG: Task ran for 16884 msec (69/69), Process = Exec, PC = 3158D42
    -Traceback= 3158CEE 3158D4A 30F7330 30F742A 30FF3A4 30FEF76 30FEF1C 3116860
    </log>


Output of a Cisco 2950 switch:

    00:06:08: %SYS-2-MALLOCFAIL: Memory allocation of 224 bytes failed from 0x800118D0, alignment 0
    Pool: Processor  Free: 0  Cause: Not enough free memory
    Alternate Pool: I/O  Free: 32  Cause: Not enough free memory

    -Process= "CDP Protocol", ipl= 0, pid= 26
    -Traceback= 801DFC30 801E1DD8 800118D8 80011218 801D932C 801D9318
    00:06:08:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:09:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:10:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:11:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:12:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:13:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:14:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:15:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:16:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:17:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:18:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:19:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:20:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:21:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:22:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:23:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:38: %SYS-2-MALLOCFAIL: Memory allocation of 140 bytes failed from 0x801E28BC, alignment 0
    Pool: Processor  Free: 0  Cause: Not enough free memory
    Alternate Pool: I/O  Free: 32  Cause: Not enough free memory

    -Process= "Calhoun Statistics Process", ipl= 0, pid= 21
    -Traceback= 801DFC30 801E1DD8 801E28C4 801F13BC 801F1470 802F7C90 802F9190 802F9788 801D932C 801D9318
    00:06:38:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:39:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:40:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:41:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:42:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:44:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:45:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:46:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:47:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:48:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:49:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:50:  ../src-calhoun/strata_stats.c at line 137: can't not push event list
    00:06:59: %SYS-3-CPUHOG: Task ran for 2076 msec (11/10), process = Net Background, PC = 801ABD40.
    -Traceback= 801ABD48 801D932C 801D9318

And then, the CDP process is totally down, even when we stop the attack. No more CDP babies...
