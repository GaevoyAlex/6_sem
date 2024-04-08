import 'package:flutter/material.dart';

class MyBottomBar extends StatelessWidget {
  // Создаем константы для индексов страниц
  static const int PAGE_ONE = 0;
  static const int PAGE_TWO = 1;
  static const int PAGE_THREE = 2;

  const MyBottomBar({super.key});

  // Создаем функцию для перехода на нужную страницу по индексу
  void navigateToPage(BuildContext context, int index) {
    switch (index) {
      case PAGE_ONE:
        Navigator.pushNamed(context, "/homePage");
        break;
      case PAGE_TWO:
        Navigator.pushNamed(context, "/profilePage");
        break;
      case PAGE_THREE:
        Navigator.pushNamed(context, "/createEventPage");
        break;
      default:
        break;
    }
  }

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      // Создаем список элементов ботом бара с иконками и подписями
      items: [
        BottomNavigationBarItem(
          icon: Icon(Icons.home,color: Colors.purple,),
          label: "Home",
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.plus_one,color: Colors.purple,),
          label: "Create",
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.person,color: Colors.purple,),
          label: "Profile",
        ),
      ],
      // Обрабатываем нажатие на элемент ботом бара
      onTap: (index) {
        navigateToPage(context, index);
      },
    );
  }
}
