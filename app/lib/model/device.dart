class Device {
  int color;
  int isOn;
  int isConnected;
  String ip;
  String name;
  double brightness;

  Device({
    required this.ip,
    this.name = "Unknown",
    this.color = 0xFF000000,
    this.brightness = 0.0,
    this.isOn = 0,
    this.isConnected = 0
  });

  Map<String, dynamic> toMap() {
    return {
      'ip': ip,
      'name': name,
      'color': color,
      'brightness': brightness,
      'isOn': isOn,
      'isConnected': isConnected,
    };
  }

  @override
  String toString() {
    return 'Device {'
        'ip: $ip, '
        'name: $name, '
        'color: $color, '
        'brightness: $brightness, '
        'isOn: $isOn, '
        'isConnected: $isConnected}';
  }

  Device copyWith({
    int? color,
    int? isOn,
    int? isConnected,
    String? name,
    double? brightness
  }) {
    return Device(
      ip: ip,
      name: name ?? this.name,
      color: color ?? this.color,
      brightness: brightness ?? this.brightness,
      isOn: isOn ?? this.isOn,
      isConnected: isConnected ?? this.isConnected
    );
  }
}
