#Importing necessary modules
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify

#Generating private key (RsaKey object) of key length of 1024 bits
private_key = RSA.generate(2048)
#Generating the public key (RsaKey object) from the private key
public_key = private_key.publickey()
print(private_key, public_key)

private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()
print(type(private_pem), type(public_pem))
print(private_pem)
print(len(public_pem))
print(len("-----BEGIN PUBLIC KEY-----MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBgrnAvScgDvGgWNUywJhY3hZNpAVpuydUU72+uVO8Vcjx//ASyJTS0HAN+7484gRu0Z1v2nrk6QpMVJhAZP9h2KdEzHArOlfPxpnLuAqRjuArhZj3DMhh0n6loCtt+1QO/bwnJ+E27B4kGEAYFpk8Z8l/Aj72PsE3wbElqgR7PligCPqGIMxEPta0o1sCs7HrWXGRu3DFsY1Tbr3sPuI5Y1OXGOODHBrj2ZkdFkHNGKcgFT1Q4Jblab3t/Ux8OvZ8+Vr65Oy8AstsNdLo8l2opaemqLGL1QJ4aBtgTKK/mytbE5KF+dQOiF/0udTSlfZXVO1lopcZ3lHJSox70qn0NAgMBAAE=-----END PUBLIC KEY-----"))