import 'package:client/resources.dart';
import 'package:client/view/device_add_form.dart';
import 'package:flutter/material.dart';

class DeviceAddScreen extends StatelessWidget {
  const DeviceAddScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(R(context).strings.deviceAddScreenTitle),
      ),
      body: const DeviceAddForm()
    );
  }
}
