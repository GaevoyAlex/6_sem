import 'package:exhibition_app/Screens/FirstScreen.dart';
import 'package:exhibition_app/Screens/creators_Screens/CreateEventScreen.dart';
import 'package:exhibition_app/Screens/creators_Screens/ListOfEventsScreen.dart';
import 'package:exhibition_app/Screens/creators_Screens/ProfileCtSctreen.dart';
import 'package:flutter/material.dart';

import 'Screens/Auth_Sc/AuthCtScreen.dart';
import 'Screens/Auth_Sc/AuthUsScreen.dart';
import 'Screens/FirstScreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final key = UniqueKey();
    return MaterialApp(key: key, initialRoute: '/createEventPage', routes: {
      '/': (context) => FirstScreen(),
      '/authUsers': (context) => AuthUsScreen(),
      '/authCreators': (context) => AuthCtScreen(),
      '/homePage': (context) => ListOfEventsScreen(),
      '/profilePage': (context) => ProfileCtScreen(),
      '/createEventPage': (context) => CreateEventScreen(
            onEventCreated: (event) {
              // обработка созданного мероприятия
            },
          ),
    });
  }
}
