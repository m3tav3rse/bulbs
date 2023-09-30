bool isHexString(String input) {
  if (input.length != 6) {
    return false;
  }

  for (int i in input.toUpperCase().codeUnits) {
    if (i < 47 || i > 70 || (i > 57 && i < 65)) {
      return false;
    }
  }

  return true;
}

int hexToInt(String hex) {
  if (hex[0] == "#") {
    hex = hex.substring(1, 7);
  }

  return int.parse(hex, radix: 16) + 0xFF000000;
}

String intToHex(int value) {
  return (value & 0xFFFFFF).toRadixString(16).padLeft(6, '0').toLowerCase();
}
