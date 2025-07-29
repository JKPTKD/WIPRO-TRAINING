num = int(input("Enter the number: "))

pos = int(input("Enter the bit position to work on: "))
def bitstate(num, pos):
    return (num >> pos) & 1

def bittoggle(num, pos):
    return num ^ (1 << pos)

def nibbletoggle(num, pos):
    nibble_start = (pos // 4) * 4
    nibble_mask = 0b1111 << nibble_start
    return num ^ nibble_mask

def leftrotate(num, nbits, bit_size=32):
    nbits %= bit_size
    return ((num << nbits) | (num >> (bit_size - nbits))) & ((1 << bit_size) - 1)

def rightrotate(num, nbits, bit_size=32):
    nbits %= bit_size
    return ((num >> nbits) | (num << (bit_size - nbits))) & ((1 << bit_size) - 1)

print("\n--- Results ---")
print(f"Binary representation of {num}: {bin(num)}")


state = bitstate(num, pos)
print(f"Bit at position {pos}: {state}")


bt = bittoggle(num, pos)
print(f"Number after toggling bit {pos}: {bt} (Binary: {bin(bt)})")


nt = nibbletoggle(num, pos)
print(f"Number after toggling nibble containing bit {pos}: {nt} (Binary: {bin(nt)})")


nbits = int(input("\nEnter number of bits to left rotate: "))
lr = leftrotate(num, nbits)
print(f"Number after left rotating by {nbits} bits: {lr} (Binary: {bin(lr)})")


nbits2 = int(input("Enter number of bits to right rotate: "))
rr = rightrotate(num, nbits2)
print(f"Number after right rotating by {nbits2} bits: {rr} (Binary: {bin(rr)})")
