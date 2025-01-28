import base64

hex_string = "48656C6C6F20776F726C64"  # Example hex: "hello world"
byte_data = bytes.fromhex(hex_string)
answer = base64.b64encode(byte_data)
print(answer)
print(byte_data)  # Output: b'hello world'

