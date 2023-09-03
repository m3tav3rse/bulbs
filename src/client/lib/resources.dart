import 'package:flutter/material.dart';

class R {
  static R? _instance;
  static BuildContext? _context;

  R._internal(BuildContext context) {
    _instance = this;
    _context = context;
  }

  factory R(BuildContext context) {
    return _instance ?? R._internal(context);
  }

  Strings get strings {
    Locale locale = Localizations.localeOf(_context!);

    switch (locale.languageCode) {
      default:
        return Strings();
    }
  }
}

abstract class StringsImplementation {
  String get title;
  String get navigationLabelDevices;
  String get navigationLabelScenes;
  String get floatingButtonLabelDevice;
  String get floatingButtonLabelScene;
  String get on;
  String get off;
  String get online;
  String get offline;
  String get downloadDoneOk;
  String get deviceListEmpty;
  String get deviceItemButtonEdit;
  String get deviceAddScreenTitle;
  String get deviceAddFormSubmit;
  String get deviceAddFormEmpty;
  String get deviceAddFormIpLabel;
  String get deviceAddFormNameLabel;
  String get deviceEditScreenTitle;
  String get deviceEditNameLabel;
  String get deviceEditPowerLabel;
  String get deviceEditColorLabel;
  String get deviceEditBrightnessLabel;
  String get sceneAddScreenTitle;
}

class Strings implements StringsImplementation {
  @override
  String get title => 'Bulbs';
  @override
  String get navigationLabelDevices => 'Devices';
  @override
  String get navigationLabelScenes => 'Scenes';
  @override
  String get floatingButtonLabelDevice => 'Device';
  @override
  String get floatingButtonLabelScene => 'Scene';
  @override
  String get on => 'On';
  @override
  String get off => 'Off';
  @override
  String get online => 'Online';
  @override
  String get offline => 'Offline';
  @override
  String get downloadDoneOk => 'Devices has been updated';
  @override
  String get deviceListEmpty => 'No devices available';
  @override
  String get deviceItemButtonEdit => 'Edit';
  @override
  String get deviceAddScreenTitle => 'Add device';
  @override
  String get deviceAddFormEmpty => 'Fill out this field';
  @override
  String get deviceAddFormSubmit => 'Add';
  @override
  String get deviceAddFormIpLabel => 'IP';
  @override
  String get deviceAddFormNameLabel => 'Name';
  @override
  String get deviceEditScreenTitle => 'Edit device';
  @override
  String get deviceEditNameLabel => 'Name';
  @override
  String get deviceEditPowerLabel => 'Power';
  @override
  String get deviceEditColorLabel => 'Color';
  @override
  String get deviceEditBrightnessLabel => 'Brightness';
  @override
  String get sceneAddScreenTitle => 'Add scene';
}
