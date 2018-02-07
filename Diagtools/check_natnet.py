import natnetclient as natnet

client = natnet.NatClient()
RightLED = client.rigid_bodies['LED']


print(RightLED.position)