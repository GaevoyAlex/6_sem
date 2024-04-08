import 'package:exhibition_app/Screens/creators_Screens/widgets/HomePage_Wdg.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http; // Импортируем библиотеку http

class ProfileCtScreen extends StatefulWidget {
  const ProfileCtScreen({Key? key}) : super(key: key);

  @override
  State<ProfileCtScreen> createState() => _ProfileCtScreenState();
}

class _ProfileCtScreenState extends State<ProfileCtScreen> {
  // Создаем список с данными для мероприятий
  final List<String> events = [
    "Выставка картин",
    "Концерт рок-группы",
    "Семинар по программированию",
    "Фестиваль кино",
    "Мастер-класс по фотографии",
  ];

  // Создаем функцию, которая удаляет мероприятие из списка по индексу
  void deleteEvent(int index) {
    // Удаляем мероприятие из списка
    events.removeAt(index);

    // Показываем сообщение об удалении
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text("Мероприятие успешно удалено"),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Профиль пользователя"),
      ),
      body: Padding(
        padding: EdgeInsets.all(10), // Отступы для тела страницы
        child: Column(
          children: [
            // Иконка профиля
            CircleAvatar(
              radius: 50,
              backgroundImage: AssetImage('assets/image/profile.jpg'),
            ),
            SizedBox(
              height: 10, // Расстояние между иконкой и фио
            ),
            // ФИО
            Text(
              "Иван Иванов",
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(
              height: 10, // Расстояние между фио и почтой
            ),
            // Почта
            Text(
              "ivanov@mail.com",
              style: TextStyle(
                fontSize: 18,
                color: Colors.grey,
              ),
            ),
            SizedBox(
              height: 10, // Расстояние между почтой и кнопкой
            ),
            // Кнопка выйти из аккаунта
            ElevatedButton(
              onPressed: () {
                // Выполняем действие выхода из аккаунта
              },
              child: Text("Выйти из аккаунта"),
            ),
            SizedBox(
              height: 10, // Расстояние между кнопкой и списком
            ),
            // Список мероприятий с кнопкой удалить
            Expanded(
              child: ListView.builder(
                itemCount: events.length, // Количество элементов в списке
                itemBuilder: (context, index) {
                  return Container(
                    margin: EdgeInsets.all(10), // Отступы для контейнера
                    padding: EdgeInsets.all(10), // Отступы для текста
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(width: 0.3),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        // Текст с названием мероприятия
                        Text(events[index]),
                        // Текстовая кнопка с действием удалить
                        TextButton(
                          onPressed: () {
                            // Вызываем функцию удаления по индексу
                            deleteEvent(index);
                          },
                          child: Text("Удалить"),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: MyBottomBar(),
    );
  }
}
