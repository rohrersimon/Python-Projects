import sys

def decode(flag):
  """Decodes the flag string."""
  result = ''
  for i in range(0, len(flag), 2):
    byte1 = ord(flag[i])
    byte2 = ord(flag[i + 1])
    result += chr((byte1 << 8) + byte2)
  return result

if __name__ == '__main__':
  flag = sys.stdin.read().strip()
  print(decode(flag))