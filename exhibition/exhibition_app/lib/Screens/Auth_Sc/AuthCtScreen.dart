import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http; // Импортируем библиотеку http для отправки запросов

class AuthCtScreen extends StatefulWidget {
  const AuthCtScreen({Key? key}) : super(key: key);

  @override
  State<AuthCtScreen> createState() => _AuthCtScreenState();
}

class _AuthCtScreenState extends State<AuthCtScreen> {
  // Создаем контроллеры для управления текстовыми полями
  final loginController = TextEditingController();
  final passwordController = TextEditingController();

  // Создаем функцию для отправки http запроса post с логином и паролем
  Future<void> sendRequest() async {
    // Получаем логин и пароль из текстовых полей
    String login = loginController.text;
    String password = passwordController.text;

    // Создаем url для api
    String url = "http://127.0.0.1:8000/creator/auth/";

    // Создаем тело запроса с логином и паролем
    Map<String, String> body = {
      "login": login,
      "password": password,
    };

    http.Response response = await http.post(Uri.parse(url), body: body);

    if (response.statusCode == 200) {
      Navigator.pushNamed(context, "/otherPage");
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text("Логин или пароль неверный"),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
          padding: const EdgeInsets.only(right: 40,left: 40),
          child: Column(
            children: [
              SizedBox(height: 270,),
              Text('Creators'),
              Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(width: 0.5)
                ),
                child: TextField(
                  controller: loginController,
                  decoration: InputDecoration(
                    border: InputBorder.none,
                    labelText: "Логин",
                  ),
                ),
              ),
          SizedBox(height: 20,),
          Container(
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20),
                border: Border.all(width: 0.5)
            ),
            child: TextField(
                controller: passwordController,
                decoration: InputDecoration(
                  border: InputBorder.none,
                  labelText: "Пароль",
                ),
                obscureText: true, // Скрываем вводимый текст
              ),),

              SizedBox(height: 20,),
            GestureDetector(
              //sendRequest
              onTap:
                  () {
                Navigator.pushNamed(context, '/homePage');
                },
              child: Padding(
                padding: const EdgeInsets.only(left: 100,right: 100),
                child: Container(
                  decoration: BoxDecoration(
                      gradient: const LinearGradient(
                        colors:<Color>[
                          Color(0xffbb5ce1),
                          Color(0xfff360d6),
                          Color(0xffff6be6),
                        ], // Gradient from https://learnui.design/tools/gradient-generator.html
                        tileMode: TileMode.decal, ),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(width: 1)
                  ),
                  alignment: Alignment.center,
                  child: Padding(
                    padding: const EdgeInsets.only(top: 20,bottom: 20),
                    child: Text('Log In',style: TextStyle(fontSize: 20,color: CupertinoColors.white),),
                  ),),
              ),
            ),
            ],
          ),
        ),

    );
  }
}

