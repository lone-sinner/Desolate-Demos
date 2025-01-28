import base64

hex_string = "I will bring the change"  # Example hex: "hello world"
byte_data = bytes.fromhex(hex_string)
answer = base64.b64encode(byte_data)
print(answer)
print(byte_data)  # Output: b'hello world'

