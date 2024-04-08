import 'package:exhibition_app/Screens/creators_Screens/CreateEventScreen.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Event {
  final String title;
  final String description;
  final String date;

  Event({
    required this.title,
    required this.description,
    required this.date,
  });
}

class ListOfEventsScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _ListOfEventsScreenState();
}

class _ListOfEventsScreenState extends State<ListOfEventsScreen> {
  List<Event> events = [];

void updateEventList(Event event) {
  setState(() {
    events.add(event);
  });
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Мероприятия'),
      ),
      body: ListView.builder(
        itemCount: events.length,
        itemBuilder: (context, index) {
          Event event = events[index];
          return ListTile(
            title: Text(event.title),
            subtitle: Text(event.date),
            onTap: () {
              // Действия при нажатии на мероприятие
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          final result = await Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => CreateEventScreen(
                  onEventCreated: (event) {
                    // обработка созданного мероприятия
                  },
                ),
              ));
          // Обработка результата
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
