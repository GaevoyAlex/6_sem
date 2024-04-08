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

class CreateEventScreen extends StatefulWidget {
  final void Function(Event event) onEventCreated;

  const CreateEventScreen({Key? key, required this.onEventCreated})
      : super(key: key);

  @override
  State<CreateEventScreen> createState() => _CreateEventScreenState();
}

class _CreateEventScreenState extends State<CreateEventScreen> {
  final titleController = TextEditingController();
  final descriptionController = TextEditingController();
  final dateController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    ThemeData theme = Theme.of(context);

    return Scaffold(
      appBar: AppBar(
        title: Text("Создать мероприятие"),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          children: [
            TextField(
              controller: titleController,
              decoration: InputDecoration(
                labelText: "Название мероприятия",
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.title),
              ),
              style: theme.textTheme.headline6,
            ),
            SizedBox(
              height: 10,
            ),
            TextField(
              controller: dateController,
              decoration: InputDecoration(
                labelText: "Дата мероприятия",
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.title),
              ),
              style: theme.textTheme.headline6,
            ),
            SizedBox(
              height: 10,
            ),
            TextField(
              controller: descriptionController,
              decoration: InputDecoration(
                labelText: "Описание мероприятия",
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.description),
              ),
              maxLines: 10,
              style: theme.textTheme.bodyText1,
            ),
            SizedBox(
              height: 20,
            ),
            GestureDetector(
              onTap: () {
                String title = titleController.text;
                String description = descriptionController.text;
                String date = dateController.text;

                Event event = Event(
                  title: title,
                  description: description,
                  date: date,
                );

                widget.onEventCreated(event);
                Navigator.pop(context);

                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text("Мероприятие успешно создано"),
                    backgroundColor: Colors.green,
                  ),
                );
              },
              child: Padding(
                padding: const EdgeInsets.only(left: 100, right: 100),
                child: Container(
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
                      colors: <Color>[
                        Color(0xffac5ce1),
                        Color(0xfff360d6),
                        Color(0xffbe00ff),
                      ],
                      tileMode: TileMode.decal,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(width: 1),
                  ),
                  alignment: Alignment.center,
                  child: Padding(
                    padding: const EdgeInsets.only(top: 20, bottom: 20),
                    child: Text(
                      'Создать',
                      style: TextStyle(
                        fontSize: 20,
                        color: CupertinoColors.white,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
