import 'package:flutter/material.dart';
import 'package:client/resources.dart';

class SceneAddScreen extends StatelessWidget {
  const SceneAddScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(R(context).strings.sceneAddScreenTitle),
      ),
      body: Container()
    );
  }
}
