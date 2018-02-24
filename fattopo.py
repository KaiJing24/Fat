def __init__( self ):
    "Create custom topo."
# Initialize topology
    Topo.__init__( self )
# Add hosts and switches
    Host1 = self.addHost( 'h1' )
    Host2= self.addHost( 'h2' )
    Host3 = self.addHost( 'h3' )
    Host4 = self.addHost( 'h4' )
    Host5 = self.addHost( 'h5' )
    Host6 = self.addHost( 'h6' )
    Host7 = self.addHost( 'h7' )
    Host8 = self.addHost( 'h8' )
    leftbSwitch = self.addSwitch( 's1' )
    rightbSwitch = self.addSwitch( 's2' )
    toplSwitch = self.addSwitch('s3')
    toprSwitch = self.addSwitch('s4')
# Add links
    self.addLink( toplSwitch, leftbSwitch )
    self.addLink( toplSwitch, rightbSwitch )
    self.addLink( toprSwitch, leftbSwitch )
    self.addLink( toprSwitch, rightbSwitch )
    self.addLink( leftbSwitch, Host1 )
    self.addLink( leftbSwitch, Host2 )
    self.addLink( leftbSwitch, Host3 )
    self.addLink( leftbSwitch, Host4 )
    self.addLink( rightbSwitch, Host5 )
    self.addLink( rightbSwitch, Host6 )
    self.addLink( rightbSwitch, Host7 )
    self.addLink( rightbSwitch, Host8 )
topos = { 'mytopo': ( lambda: MyTopo() ) }
