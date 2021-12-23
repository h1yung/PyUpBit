def compress(data):
    """
    Compresses the given attribute data using word-aligned hybrid compression

    Args:
        data : list
            A list of bits where the i-th element represents if the i-th record takes this value for this attribute
            For example, if this represents the bitvector for attribute A=1, then the vector [0, 1, 0] represents
            that only the second record has a value of 1 for attribute A.

    Returns:
        compressed_data : str
            The compressed version of the data
    """
    compressed = ""
    # Take in 31 bits, compress and add signal bit and add to compressed list, update previous list using counter as marker
    # three conditions: if 31 bits are all 0, if 31 bits are all 1, or if 31 bits are mixed,
    # if mixed add 31 bits to full list and add signal bit, else add signal bit and if next 31 bits are all same with same
    # bit number update count of previous marked by counter and check if type is same as previous_bit_bunch
    zero_count, one_count = 0, 0
    temp_fence = 0
    fence_pointers = []
    while len(data) != 0:
        idx = min(31, len(data))
        bits = data[:idx]
        if idx != len(data) and not any(bits):
            if one_count != 0:
                compressed += format(one_count, "030b")
                fence_pointers.append(temp_fence)
                temp_fence += 31 * one_count
                one_count = 0
            if zero_count == 0:
                compressed += "1"
                compressed += "0"
            zero_count += 1
        elif idx != len(data) and all(bits):
            if zero_count != 0:
                compressed += format(zero_count, "030b")
                fence_pointers.append(temp_fence)
                temp_fence += 31 * zero_count
                zero_count = 0
            if one_count == 0:
                compressed += "1"
                compressed += "1"
            one_count += 1
        else:
            assert(min(zero_count, one_count) == 0)
            if zero_count or one_count:
                compressed += format(max(zero_count, one_count), "030b")
                if zero_count != 0:
                    temp_fence += 31 * zero_count
                if one_count != 0:
                    temp_fence += 31 * one_count
                zero_count, one_count = 0, 0
            compressed += "0"
            compressed += "".join(str(b) for b in bits)
            fence_pointers.append(temp_fence)
            temp_fence += 31
        data = data[idx:]
    if zero_count or one_count:
        assert(min(zero_count, one_count) == 0)
        compressed += format(max(zero_count, one_count), "030b")
        fence_pointers.append(temp_fence)
    return compressed, fence_pointers

def decompress(compressed):
    """
    Decompress the given compressed bitvector

    Args:
        compressed : str
            The compressed version of the data

    Returns:
        data : list
            The decompressed data
    """
    data = []
    while len(compressed) != 0:
        idx = min(32, len(compressed))
        bits = compressed[:idx]
        compressed = compressed[idx:]
        flag = bits[0]
        if flag == '0':
            data += [int(x) for x in list(bits[1:])]
        else:
            fill = int(bits[1])
            count = int(bits[2:], 2)
            data += [fill] * 31 * count
    return data

#Possibly add function to return full list or maybe just use compress for everything except update_count.
