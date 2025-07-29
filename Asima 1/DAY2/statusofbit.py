num = int(input("Enter a number: "))
pos = int(input("Enter the bit position to check: "))

res = 'ON' if num & (1 << pos) else 'OFF'
print(f'{pos} bit on number {num} is {res}')

# Explanation (for learning)
print("\n--- Explanation ---")
print(f"Binary of num: {bin(num)[2:].zfill(8)}")
print(f"1 << {pos} = {bin(1 << pos)[2:].zfill(8)}")
print(f"{bin(num)[2:].zfill(8)} AND {bin(1 << pos)[2:].zfill(8)} = {bin(num & (1 << pos))[2:].zfill(8)}")
