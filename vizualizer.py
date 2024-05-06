import struct

filename = 'generated/random.wav'

with open(filename, 'rb') as file:
    # Read the RIFF header
    riff, size, fformat = struct.unpack('4sI4s', file.read(12))
    print(f"RIFF header: {riff}")
    print(f"Size: {size}")
    print(f"Format: {fformat}")

    # Read the fmt subchunk
    subchunk1, subchunk1_size = struct.unpack('4sI', file.read(8))
    audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('HHIIHH', file.read(16))
    print(f"FMT Subchunk: {subchunk1}")
    print(f"Subchunk1 Size: {subchunk1_size}")
    print(f"Audio Format: {audio_format}")
    print(f"Num Channels: {num_channels}")
    print(f"Sample Rate: {sample_rate}")
    print(f"Byte Rate: {byte_rate}")
    print(f"Block Align: {block_align}")
    print(f"Bits Per Sample: {bits_per_sample}")

    # If you want to see the "data" subchunk, you could continue reading bytes,
    # but be aware that the actual size might differ depending on the file.
    # This would be the next step:
    # Read the beginning of the data subchunk
    data_chunk_header = file.read(8)
    subchunk2, subchunk2_size = struct.unpack('4sI', data_chunk_header)
    print(f"Data Subchunk: {subchunk2}")
    print(f"Subchunk2 Size: {subchunk2_size}")


