import 'package:flutter/material.dart';

class TextIcon extends StatelessWidget {
  const TextIcon({
    super.key,
    required this.text,
    required this.icon,
    this.iconColor
  });

  final String text;
  final IconData icon;
  final Color? iconColor;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        Icon(icon, color: iconColor),
        const SizedBox(width: 5.0),
        Text(text)
      ]
    );
  }
}
