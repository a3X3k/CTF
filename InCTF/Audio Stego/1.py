import wave

file="1.wav"

"""This takes the filepath and decodes the hidden data and returns it"""
song = wave.open(file, mode='rb')

# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

# Convert byte array back to string
message = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))

# Cut off at the filler characters
decoded = message.split("###")[0]

song.close()

print(decoded)
