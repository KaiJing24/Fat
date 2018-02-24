"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        SwitchA = self.addSwitch( 's1' )
        SwitchB = self.addSwitch( 's2' )
        SwitchC = self.addSwitch( 's3' )
        SwitchD = self.addSwitch( 's4' )
        SwitchE = self.addSwitch( 's5' )

        # Add links
        self.addLink( leftHost, SwitchA )
        self.addLink( SwitchD, rightHost )
        self.addLink( SwitchA, SwitchB )
        self.addLink( SwitchA, SwitchC )
        self.addLink( SwitchD, SwitchB )
        self.addLink( SwitchD, SwitchC )
        self.addLink( SwitchE, SwitchB )
        self.addLink( SwitchE, SwitchC )
        self.addLink( SwitchE, SwitchD )
        self.addLink( leftSwitch, rightSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
